#!/usr/bin/env bash
# Builds the review-practice repository with the GitHub Copilot review team.
# Run it from the folder that should contain review-practice, e.g. Documents:
#   bash setup-practice.sh
set -euo pipefail
command -v git >/dev/null || { echo "Git is not installed. Install it first."; exit 1; }
if [ -z "$(git config user.email || true)" ]; then echo "Run first: git config --global user.name \"Your Name\" and git config --global user.email \"you@example.com\""; exit 1; fi
DIR="${1:-review-practice}"
if [ -e "$DIR" ]; then echo "The folder $DIR already exists. Delete or rename it, then run this again."; exit 1; fi
mkdir "$DIR" && cd "$DIR"
git init -q -b main
w() { mkdir -p "$(dirname "$1")"; cat > "$1"; }
# 1. Starting code on main
w 'package.json' <<'END_OF_FILE'
{
  "name": "review-practice",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "test": "node --test"
  }
}
END_OF_FILE
w 'src/cart.js' <<'END_OF_FILE'
export function calculateTotal(items) {
  let total = 0;
  for (const item of items) {
    total += item.price * item.quantity;
  }
  return total;
}

export function applyDiscount(total, code) {
  if (code === "SAVE10") {
    return total - 10;
  }
  return total;
}
END_OF_FILE
w 'test/cart.test.js' <<'END_OF_FILE'
import { test } from "node:test";
import assert from "node:assert/strict";
import { calculateTotal, applyDiscount } from "../src/cart.js";

test("calculateTotal adds price times quantity", () => {
  const items = [{ price: 5, quantity: 2 }, { price: 3, quantity: 1 }];
  assert.equal(calculateTotal(items), 13);
});

test("SAVE10 takes 10 off", () => {
  assert.equal(applyDiscount(50, "SAVE10"), 40);
});
END_OF_FILE
git add . && git commit -q -m "Cart with SAVE10 discount"
# 2. The change to review, on a new branch
git switch -q -c feature/discount-codes
w 'src/cart.js' <<'END_OF_FILE'
export function calculateTotal(items) {
  let total = 0;
  for (const item of items) {
    total += item.price * item.quantity;
  }
  return total;
}

const PERCENT_CODES = { HALF: 50, STUDENT: 15 };

export function applyDiscount(total, code) {
  if (code === "SAVE10") {
    return total - 10;
  }
  if (code in PERCENT_CODES) {
    return total - total * PERCENT_CODES[code];
  }
  return total;
}

export function shippingCost(total) {
  if (total > 100) {
    return 0;
  }
  return 4.99;
}
END_OF_FILE
w 'src/checkout.js' <<'END_OF_FILE'
import { calculateTotal, applyDiscount, shippingCost } from "./cart.js";

export function checkout(items, code) {
  const subtotal = calculateTotal(items);
  const discounted = applyDiscount(subtotal, code);
  return discounted + shippingCost(discounted);
}
END_OF_FILE
git add src && git commit -q -m "Add percent codes, shipping and checkout"
# 3. The GitHub Copilot review team
w 'AGENTS.md' <<'END_OF_FILE'
# Repository: review-practice

## What this repository is
A small JavaScript shopping-cart library used to practise AI code review.
- Source code: src/
- Tests: test/  (run all tests with: npm test)
- The main branch is called main. Feature work happens on other branches.

## Rules for every agent
- During a review you only read and report. Never edit, create, delete,
  commit or push anything.
- Review only code changes of the current branch compared with main:
  git diff main...HEAD -- src test
- Always cite evidence as path:line, for example src/cart.js:17.
- Say "not verified" when you could not confirm something.
- Write in plain English. Keep reports short.
END_OF_FILE
w '.github/agents/review-lead.agent.md' <<'END_OF_FILE'
---
name: review-lead
description: Leads a full code review of the current branch by delegating to
  path-mapper and bug-hunter and merging their reports.
tools: ["agent", "read", "search", "execute"]
---

You are the code review lead. You coordinate; you never edit files.
Use the review-plan skill for every review.
Delegate mapping to the path mapper and bug finding to the bug hunter.
Pass each specialist the branch name and the list of changed files,
because they cannot see this conversation.
Run both specialists in parallel, wait for both, then merge their reports.
Call the custom agents named path-mapper and bug-hunter.
END_OF_FILE
w '.github/agents/path-mapper.agent.md' <<'END_OF_FILE'
---
name: path-mapper
description: Maps the functions and call paths a code change touches. Use for
  what changed, which paths are affected, or as part of a code review.
tools: ["read", "search", "execute"]
---

You map the code paths that a change touches. Use the map-code-paths skill.
Only read files and run read-only git commands. Never edit files.
Never judge code quality; only map.
END_OF_FILE
w '.github/agents/bug-hunter.agent.md' <<'END_OF_FILE'
---
name: bug-hunter
description: Finds bugs and missing tests in changed code. Use for find bugs,
  check correctness, check test coverage, or as part of a code review.
tools: ["read", "search", "execute"]
---

You find bugs and missing tests in changed code.
Use the find-bugs-and-test-gaps skill. You may run the test command npm test.
Never edit files. Cite every finding as path:line.
END_OF_FILE
w '.github/skills/review-plan/SKILL.md' <<'END_OF_FILE'
---
name: review-plan
description: Plans and runs a full code review of the current branch with two
  specialists, then merges their findings into one report. Use when the user
  asks to review a branch, a pull request, or their changes.
---

# Review plan (for the review lead)

1. Run `git diff --name-only main...HEAD -- src test` and
   `git diff --stat main...HEAD -- src test`. If nothing changed, say so and stop.
2. Start BOTH specialists at the same time and give each the same context:
   the branch name, the list of changed files, and the line
   "Compare with main using git diff main...HEAD -- src test".
   - path mapper: map the changed code paths.
   - bug hunter: find bugs and missing tests.
3. Wait until both reports have arrived. Do not guess what they will say.
4. Merge the reports. Remove duplicates. Keep each path:line reference.
5. Reply with exactly these sections:
   ## Summary            (2-3 sentences)
   ## Changed code paths (from the path mapper)
   ## Findings           (table: Severity | Location | Problem | Suggested fix)
   ## Missing tests      (bullet list)
   ## Verdict            (Approve, Approve with changes, or Request changes)
END_OF_FILE
w '.github/skills/map-code-paths/SKILL.md' <<'END_OF_FILE'
---
name: map-code-paths
description: Maps which functions and call paths a code change touches, from
  entry points to changed lines. Use when asked what changed, which code paths
  are affected, or what a diff touches.
---

# Map changed code paths

1. Run `git diff main...HEAD -- src test` to see every changed line.
2. For each changed or new function, find who calls it
   (search the code for the function name) and what it calls.
3. Write one line per path, from the entry point to the change, like:
   checkout() -> applyDiscount()  [src/checkout.js:5 -> src/cart.js:11]
4. Mark each path NEW, CHANGED or REMOVED.
5. List the files that use the changed code but were NOT changed.
6. Do not judge quality and do not suggest fixes. Only map.
END_OF_FILE
w '.github/skills/find-bugs-and-test-gaps/SKILL.md' <<'END_OF_FILE'
---
name: find-bugs-and-test-gaps
description: Finds likely bugs and missing tests in changed code, checking edge
  cases, wrong calculations and unhandled input. Use when asked to find bugs,
  check correctness, or check test coverage of a change.
---

# Find bugs and missing tests

1. Run `git diff main...HEAD -- src test` and read the full changed files.
2. Run the tests with `npm test` and note any failures.
3. For each changed function, check: wrong maths, negative or zero values,
   boundaries (> versus >=), unknown or unexpected input, and missing
   error handling.
4. For each changed function, check whether a test covers it. List every
   case that has no test.
5. Report a table: Severity (High/Medium/Low) | path:line | Problem |
   Example input that fails | Suggested fix.
6. Never edit files. Suggest fixes in words or short snippets only.
END_OF_FILE
git add -A && git commit -q -m "Add AI review team"
echo; echo "Done. review-practice is ready on branch feature/discount-codes:"; git log --oneline; echo; echo "Next: cd $DIR"
