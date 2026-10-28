"""One-time import from the two supplied sibling folders; never edits those folders."""
from pathlib import Path
import csv
import hashlib
import html
import json
import posixpath
import re
import shutil
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT.parent
BASE = "https://gcfernando.github.io/developer-guides-and-tools"
REPO = "https://github.com/gcfernando/developer-guides-and-tools"
SOURCES = {"KnowledgeBase": "developer-guides-and-cheatsheets", "Other_Projects": "developer-tools-and-guides"}
MAPPING = {}

def register(source, old, new):
    MAPPING[f"{source}/{old}"] = new

guides = {
    "python_oop_guide.md": "docs/python/oop.md",
    "python_dunder.md": "docs/python/special-methods.md",
    "csharp_dotnet_oop_guide.md": "docs/csharp-dotnet/oop.md",
    "sql_complete_guide.md": "docs/databases/sql-server-and-mysql.md",
    "azure_cheatsheet.md": "docs/cloud/azure/engineering-cheat-sheet.md",
    "azure_resources_cheatsheet.md": "docs/cloud/azure/resource-reference.md",
    "docker_cheatsheet.md": "docs/containers/docker-cheat-sheet.md",
    "podman_cheatsheet.md": "docs/containers/podman-cheat-sheet.md",
    "git_cheatsheet.md": "docs/version-control/git-cheat-sheet.md",
    "local_ai_learning_lab.md": "docs/ai/local-ai-chat-lab.md",
}
for old, new in guides.items():
    register("KnowledgeBase", old, new)
for old, new in {
    "AGENTS.md": "codex/AGENTS.md", "CLAUDE.md": "claude/CLAUDE.md",
    "ENGINEERING.md": "shared/ENGINEERING.md", "copilot-instructions.md": "copilot/copilot-instructions.md",
    "gpt_custom_instruction.txt": "chatgpt/custom-instructions.txt",
}.items():
    register("KnowledgeBase", "ai-cli/" + old, "templates/ai-instructions/" + new)
register("KnowledgeBase", "ai-cli/configuration/config.toml", "examples/ai-clients/codex/config.example.toml")
register("KnowledgeBase", "ai-cli/configuration/settings.json", "examples/ai-clients/claude/settings.example.json")
register("KnowledgeBase", "ai-cli/configuration/copilot-config.json", "examples/ai-clients/copilot/README.md")

for old, new in {
    "Files/AI-Learning-Atlas-Complete.html": "apps/ai-learning-atlas/index.html",
    "Files/ai-learning-atlas.md": "apps/ai-learning-atlas/README.md",
    "Files/ai_coding_plugins_beginners_guide.md": "docs/ai/coding-addons.md",
    "Files/ai_coding_plugins_beginners_guide.html": "maintenance/migration/legacy/ai-coding-addons.html",
    "Files/Convert-LineEndings.ps1": "tools/powershell/convert-line-endings/Convert-LineEndings.ps1",
    "Files/compose.yml": "examples/containers/local-services/compose.yml",
    "Files/.wslconfig": "examples/wsl/.wslconfig.example",
    "Files/iptv_world_explorer_2026.md": "docs/media/iptv/playlists.md",
    "Files/images/open_media.png": "docs/media/iptv/images/open-media.png",
    "Files/images/tool_bar.png": "docs/media/iptv/images/tool-bar.png",
    "Files/images/your_tv.png": "docs/media/iptv/images/your-tv.png",
    "SystemMaintenance/SystemMaintenance.ps1": "tools/powershell/system-maintenance/SystemMaintenance.ps1",
    "SystemMaintenance/readme.md": "tools/powershell/system-maintenance/README.md",
    ".github/workflows/seo.yml": "maintenance/migration/legacy/static-reference-workflow.yml",
}.items():
    register("Other_Projects", old, new)
for file in (WORKSPACE / "Other_Projects/Linux_Commands").iterdir():
    register("Other_Projects", "Linux_Commands/" + file.name,
             "apps/linux-command-reference/" + ("README.md" if file.name == "readme.md" else file.name))
for source in SOURCES:
    for name in ["README.md", "documentation.md", "_config.yml"]:
        register(source, name, f"maintenance/migration/legacy/{source}/{name}")
    for name in ["_layouts/default.html", "assets/css/documentation.css", "assets/images/mark.svg"]:
        register(source, name, name)

PERMALINKS = {value: "/" + value.removeprefix("docs/").removesuffix(".md") + "/" for value in guides.values()}
PERMALINKS.update({
    "docs/ai/coding-addons.md": "/ai/coding-addons/guide/",
    "docs/media/iptv/playlists.md": "/media/iptv/",
    "apps/linux-command-reference/README.md": "/apps/linux-command-reference/guide/",
    "apps/ai-learning-atlas/README.md": "/apps/ai-learning-atlas/guide/",
    "tools/powershell/system-maintenance/README.md": "/utilities/windows-maintenance/",
})

def public_path(dest):
    if dest in PERMALINKS:
        return PERMALINKS[dest]
    if dest.endswith("/index.html"):
        return "/" + dest.removesuffix("index.html")
    return "/" + dest

def logical_destination(source, old):
    if old == "README.md": return "README.md"
    if old == "documentation.md": return "documentation.md"
    if old == "Files/ai_coding_plugins_beginners_guide.html": return "apps/ai-coding-addons/index.html"
    return MAPPING.get(f"{source}/{old}")

def resolve_old(source, path):
    path = unquote(path).lstrip("/")
    if not path or path in ["index.html", "README.html"]: return "README.md"
    if path in ["documentation", "documentation/", "documentation.html"]: return "documentation.md"
    if path in ["Linux_Commands/guide", "Linux_Commands/guide/"]: return "Linux_Commands/readme.md"
    if path in ["Files/ai-coding-addons-markdown", "Files/ai-coding-addons-markdown/"]: return "Files/ai_coding_plugins_beginners_guide.md"
    candidates = [path, path.rstrip("/") + "/index.html", path.rstrip("/") + "/readme.md", path.rstrip("/") + "/README.md"]
    if path.endswith(".html"): candidates.append(path[:-5] + ".md")
    if not Path(path).suffix: candidates.append(path.rstrip("/") + ".md")
    for candidate in candidates:
        if f"{source}/{candidate}" in MAPPING: return candidate
    return None

def rewrite_url(url, source, old, dest, is_html=False):
    url = html.unescape(url)
    if url.startswith(("#", "mailto:", "data:", "javascript:")): return url
    split = urlsplit(url)
    found_source, found_old = source, None
    if split.netloc == "gcfernando.github.io":
        for src, repo in SOURCES.items():
            if split.path == "/" + repo or split.path.startswith("/" + repo + "/"):
                found_source = src
                found_old = resolve_old(src, split.path[len(repo)+1:])
                break
    elif split.netloc in ["github.com", "raw.githubusercontent.com"]:
        for src, repo in SOURCES.items():
            prefix = "/gcfernando/" + repo
            if split.path.rstrip("/") in [prefix, prefix + ".git"]:
                return REPO + (".git" if split.path.endswith(".git") else "") + ("#" + split.fragment if split.fragment else "")
            for suffix in ["/blob/main/", "/tree/main/", "/main/"]:
                if split.path.startswith(prefix + suffix):
                    found_source = src
                    found_old = resolve_old(src, split.path[len(prefix+suffix):])
    elif split.scheme or split.netloc:
        return url
    else:
        oldpath = posixpath.normpath(posixpath.join(posixpath.dirname(old), split.path))
        found_old = resolve_old(source, oldpath)
        if not found_old and split.path in ["../", "../../", "./"]:
            found_old = "README.md"
    if not found_old: return url
    target = logical_destination(found_source, found_old)
    if not target: return url
    if is_html:
        if target == "README.md": target_url = BASE + "/"
        elif target == "documentation.md": target_url = BASE + "/documentation/"
        elif target.endswith(".md") and target not in PERMALINKS:
            target_url = REPO + "/blob/main/" + target
        else: target_url = BASE + public_path(target)
    else:
        target_url = posixpath.relpath(target, posixpath.dirname(dest) or ".")
    return target_url + ("?" + split.query if split.query else "") + ("#" + split.fragment if split.fragment else "")

def transform(text, source, old, dest):
    is_html = dest.endswith(".html")
    if is_html:
        text = re.sub(r'(\b(?:href|src)\s*=\s*[\"\'])([^\"\']+)([\"\'])',
            lambda m: m[1] + rewrite_url(m[2], source, old, dest, True) + m[3], text)
        for repo in SOURCES.values(): text = text.replace("https://gcfernando.github.io/" + repo + "/", BASE + "/")
    elif dest.endswith(".md"):
        text = re.sub(r'(\]\()([^\s\)]+)(\))', lambda m: m[1] + rewrite_url(m[2], source, old, dest) + m[3], text)
        text = re.sub(r'(\b(?:href|src)\s*=\s*[\"\'])([^\"\']+)([\"\'])',
            lambda m: m[1] + rewrite_url(m[2], source, old, dest) + m[3], text)
    if dest.endswith(".md") and dest in PERMALINKS:
        meta = f'layout: default\npermalink: {PERMALINKS[dest]}\n'
        if text.startswith("---\n"):
            end = text.find("\n---", 4)
            front = re.sub(r'^(?:layout|permalink|canonical_url|sitemap):.*\n?', '', text[4:end], flags=re.M)
            text = "---\n" + meta + front.rstrip() + "\n---" + text[end+4:]
        else:
            title = re.search(r'^# (.+)', text, re.M)
            clean = re.sub(r'[^\w\s#/.&:—-]', '', title[1]).strip() if title else Path(dest).stem
            text = "---\n" + meta + "title: " + json.dumps(clean, ensure_ascii=False) + "\n---\n\n" + text
    return text

def write(path, content):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")

def run():
    manifest = ROOT / "maintenance/migration/source-map.csv"
    if manifest.exists(): raise SystemExit("Import already completed; refusing to overwrite the merged tree.")
    source_files = [p for src in SOURCES for p in (WORKSPACE/src).rglob("*") if p.is_file()]
    assert set(MAPPING) == {p.relative_to(WORKSPACE).as_posix() for p in source_files}, "Incomplete source mapping"
    records = []
    for source_path in source_files:
        key = source_path.relative_to(WORKSPACE).as_posix()
        source, old = key.split("/", 1)
        dest = MAPPING[key]
        raw = source_path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        status = "copied"
        if old == "ai-cli/configuration/copilot-config.json":
            status = "excluded-personal-application-state"
        elif dest.startswith("maintenance/migration/legacy/"):
            target = ROOT/dest; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(raw)
            status = "archived-original"
        elif (ROOT/dest).exists():
            assert (ROOT/dest).read_bytes() == raw, "Nonidentical shared asset: " + key
            status = "deduplicated-identical"
        else:
            target = ROOT/dest; target.parent.mkdir(parents=True, exist_ok=True)
            if source_path.suffix.lower() in [".md", ".html"]:
                write(dest, transform(raw.decode("utf-8-sig").replace("\r\n", "\n"), source, old, dest))
                status = "migrated-links-and-metadata"
            else: target.write_bytes(raw)
        records.append([source, SOURCES[source], old, digest, len(raw), dest, status])
    with manifest.open("w", encoding="utf-8", newline="") as f:
        writer=csv.writer(f); writer.writerow(["source_folder","source_repository","source_path","source_sha256","source_bytes","destination","disposition"]); writer.writerows(records)
    urls=[]
    for key in MAPPING:
        src, old = key.split("/",1)
        dest=logical_destination(src,old)
        if old.endswith((".md",".html")) and not old.startswith("ai-cli/"):
            oldpage = "/" if old == "README.md" else "/documentation/" if old == "documentation.md" else "/Linux_Commands/guide/" if old == "Linux_Commands/readme.md" else "/Files/ai-coding-addons-markdown/" if old == "Files/ai_coding_plugins_beginners_guide.md" else "/"+old.removesuffix(".md")+(".html" if old.endswith(".md") else "")
            target = "/" if dest=="README.md" else "/documentation/" if dest=="documentation.md" else public_path(dest)
            urls.append(["https://gcfernando.github.io/"+SOURCES[src]+oldpage,BASE+target,"mapping-only; old-host redirect not deployed"])
    urls.append(["https://gcfernando.github.io/developer-tools-and-guides/Linux_Commands/",BASE+"/apps/linux-command-reference/","mapping-only; old-host redirect not deployed"])
    with (ROOT/"maintenance/migration/url-map.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f);w.writerow(["old_url","new_url","status"]);w.writerows(urls)
    write("maintenance/migration/page-routes.json",json.dumps(PERMALINKS, indent=2) + "\n")
    print(f"Imported {len(records)} files. Originals preserved. Manifest: {manifest}")

if __name__ == "__main__": run()
