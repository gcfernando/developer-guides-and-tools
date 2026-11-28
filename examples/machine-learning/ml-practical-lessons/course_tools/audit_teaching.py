"""Inventory every teaching heading, example and figure without claiming learner success.

Run after authoring and building. --write records the current inventory; otherwise
the command checks the recorded inventory against the actual authored sources.
Only the Python standard library is needed.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "course-review" / "teaching-coverage.csv"
SUMMARY = REPORT.with_suffix(".json")
SKIP = {".venv", "__pycache__", ".git", "node_modules"}
FIELDS = [
    "unit_id", "file", "line", "kind", "title", "lesson", "teaching_source",
    "python_files", "data_files", "expected_outputs", "visual_files",
    "source_sha256", "structural_state", "learner_evidence",
]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sources():
    """Include all learner guides and all lesson/project instructions, not history."""
    paths = list(ROOT.glob("*.md"))
    paths += list((ROOT / "lessons").rglob("*.md"))
    paths += list((ROOT / "projects").rglob("*.md"))
    return sorted(p for p in paths if p.name != "AGENTS.md" and not SKIP.intersection(p.parts))


def inventory():
    rows = []
    errors = []
    ids = [int(p.name[:3]) for p in (ROOT / "lessons").iterdir()
           if p.is_dir() and re.match(r"\d{3}-", p.name)]
    if sorted(ids) != list(range(1, 448)):
        errors.append("The numbered lesson folders must contain each ID from 001 to 447 exactly once.")
    author_path = ROOT / "course_tools" / "author_teaching.py"
    profiles = {}
    profile_names = {}
    if author_path.is_file():
        spec = importlib.util.spec_from_file_location("course_teaching_profiles", author_path)
        author = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(author)
        profiles = author.PROFILES
        profile_names = author.LESSON_PROFILES
        for lesson_id in range(1, 448):
            profile = profiles.get(profile_names.get(lesson_id), {})
            for field in ("ready", "meaning", "use", "example", "caution", "task", "answer"):
                if not profile.get(field, "").strip():
                    errors.append(f"Lesson {lesson_id:03}: concept profile lacks {field}")
        workbook = (ROOT / "Data-Science-and-Machine-Learning.md").read_text(encoding="utf-8")
        attached = [int(x) for x in re.findall(r"<!-- workbook-teaching:(\d+):start -->", workbook)]
        if sorted(attached) != list(range(1, 448)):
            errors.append("Workbook must include exactly one teaching note for every numbered entry.")
    for path in sources():
        text = path.read_text(encoding="utf-8")
        name = relative(path)
        folder = path.parent
        lesson = folder.name if "lessons" in path.parts else ""
        if path.name == "README.md" and re.match(r"\d{3}-", lesson):
            if text.count("<!-- teaching-note:start -->") != 1 or text.count("<!-- teaching-note:end -->") != 1:
                errors.append(f"{name}: needs exactly one self-contained concept teaching note")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        teaching = name
        # Workbook headings link to self-contained lesson instructions immediately
        # below the heading. This mapping records the real nearby ZIP, not a guess.
        headings = []
        fenced = False
        language = ""
        fence_start = 0
        code_lines = []
        blocks = []
        figures = []
        lines = text.splitlines()
        for number, line in enumerate(lines, 1):
            fence = re.match(r"^\s*(```+|~~~+)(.*)$", line)
            if fence:
                if not fenced:
                    fenced = True
                    language = fence.group(2).strip().split(" ")[0]
                    fence_start = number
                    code_lines = []
                else:
                    fenced = False
                    blocks.append((fence_start, language or "text", "\n".join(code_lines)))
                continue
            if fenced:
                code_lines.append(line)
                continue
            heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if heading:
                headings.append((number, len(heading.group(1)), heading.group(2)))
            for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", line):
                target = match.group(2).split("#", 1)[0]
                figures.append((number, match.group(1), target))
                if not target.startswith(("http:", "https:", "data:")) and not (folder / target).is_file():
                    errors.append(f"{name}:{number}: missing figure {target}")
        if fenced:
            errors.append(f"{name}: unclosed code fence")

        def append(number, kind, title, teaching_source, selected_folder=folder, visual=""):
            rows.append(dict(zip(FIELDS, [
                f"{name}:{number}:{kind}", name, str(number), kind, title, lesson,
                teaching_source,
                ";".join(relative(p) for p in sorted(selected_folder.glob("*.py"))),
                ";".join(relative(p) for p in sorted(selected_folder.glob("*.csv"))),
                ";".join(relative(p) for p in sorted(selected_folder.glob("*output*.txt"))),
                visual or ";".join(relative(p) for p in sorted(selected_folder.glob("*.png"))),
                digest, "concept profile present; structural checks passed" if re.match(r"\d{3}-", lesson) else "source inspected; application review required", "not observed",
            ])))

        for index, (number, depth, title) in enumerate(headings):
            end = next((n for n, d, _ in headings[index + 1:] if d <= depth), len(lines) + 1)
            body = "\n".join(lines[number:end - 1])
            selected = folder
            mapped = teaching
            if path.name == "Data-Science-and-Machine-Learning.md":
                links = re.findall(r"sample_code_folder/([\w-]+)\.zip", body)
                if links:
                    linked = ROOT / "lessons" / links[0]
                    if linked.is_dir():
                        selected = linked
                        mapped = relative(linked / "README.md")
            append(number, "heading", title, mapped, selected)
        for number, language, code in blocks:
            if language in {"python", "py"}:
                try:
                    ast.parse(code)
                except SyntaxError as error:
                    errors.append(f"{name}:{number}: Python extract syntax: {error.msg}")
            append(number, "code:" + language, f"{language} block", teaching)
        for number, label, target in figures:
            if not label.strip():
                errors.append(f"{name}:{number}: image lacks a text description")
            append(number, "figure occurrence", label, teaching, visual=target)

    # Account for downloadable scripts and figures even if not embedded in prose.
    for base, pattern, kind in [("lessons", "*.py", "runnable source"), ("projects", "*.py", "runnable source"),
                                ("workbook-figures", "*.png", "visual asset")]:
        for path in sorted((ROOT / base).rglob(pattern)):
            if SKIP.intersection(path.parts):
                continue
            name = relative(path)
            readme = path.parent / "README.md"
            rows.append(dict(zip(FIELDS, [
                name, name, "1", kind, path.name,
                path.parent.name if base == "lessons" else "",
                relative(readme) if readme.exists() else "Data-Science-and-Machine-Learning.md",
                name if kind == "runnable source" else "", "", "",
                name if kind == "visual asset" else "", hashlib.sha256(path.read_bytes()).hexdigest(),
                "source inspected; application review required", "not observed",
            ])))
    for base in ("lessons", "projects"):
        for path in sorted((ROOT / base).rglob("*.csv")):
            if SKIP.intersection(path.parts):
                continue
            name = relative(path)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            with path.open(encoding="utf-8-sig", newline="") as handle:
                records = list(csv.reader(handle))
            if not records:
                errors.append(f"{name}: data table is empty")
                continue
            for number, record in enumerate(records[1:], 2):
                if len(record) != len(records[0]):
                    errors.append(f"{name}:{number}: row does not match the column count")
            for index, field in enumerate(records[0], 1):
                rows.append(dict(zip(FIELDS, [
                    f"{name}:field:{index}", name, "1", "data field", field,
                    path.parent.name if base == "lessons" else "",
                    relative(path.parent / "README.md") if (path.parent / "README.md").exists() else "INDEPENDENT-PROJECT.md",
                    "", name, "", "", digest,
                    "schema checked; meaning reviewed with its teaching unit", "not observed",
                ])))
    return rows, errors


def csv_text(rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="record current source coverage")
    args = parser.parse_args()
    rows, errors = inventory()
    text = csv_text(rows)
    summary = {
        "scope": "Every authored learner heading, code block, figure occurrence, lesson/project Python source and data field, and workbook figure",
        "source_documents": len(sources()),
        "units": len(rows),
        "kinds": dict(sorted(Counter(row["kind"] for row in rows).items())),
        "numbered_lesson_folders": len([p for p in (ROOT / "lessons").iterdir() if p.is_dir() and re.match(r"\d{3}-", p.name)]),
        "missing_sources_or_syntax_problems": errors,
        "meaning_of_coverage": "Inventory is evidence of scope, not proof of teaching quality, accessibility or learner understanding.",
        "learner_study": "Not performed. Use TEACHING.md to record observed application and delayed checks.",
        "source_inventory_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }
    if errors:
        print("\n".join(errors[:40]))
        raise SystemExit(f"{len(errors)} teaching source problems")
    if args.write:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
        SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    elif not REPORT.exists() or REPORT.read_text(encoding="utf-8") != text:
        raise SystemExit("Teaching inventory changed. Review it, then run python course_tools/audit_teaching.py --write.")
    print(f"Teaching scope: {len(rows)} units across {len(sources())} documents; 447 numbered lessons accounted for.")


if __name__ == "__main__":
    main()
