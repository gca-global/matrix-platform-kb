#!/usr/bin/env bash
# Cut a new release: bumps VERSION file, folds RELEASE_NOTES Unreleased.
# Usage: scripts/release.sh patch|minor|major|X.Y.Z
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [ $# -ne 1 ]; then echo "Usage: $0 <version|patch|minor|major>" >&2; exit 1; fi
ARG="$1"
CURRENT=$(tr -d '[:space:]' < VERSION)
bump() {
  local part="$1"; IFS='.' read -r MA MI PA <<< "$CURRENT"
  case "$part" in major) echo "$((MA+1)).0.0";; minor) echo "${MA}.$((MI+1)).0";; patch) echo "${MA}.${MI}.$((PA+1))";; *) echo "$part";; esac
}
NEW=$(bump "$ARG")
TODAY=$(date -u +%Y-%m-%d)
PUSH="https://x-access-token:$(gh auth token)@github.com/sharpsir-group/matrix-platform-kb.git"
echo "Bumping $CURRENT -> $NEW ($TODAY)"
printf '%s\n' "$NEW" > VERSION
python3 - "$NEW" "$TODAY" <<'PY'
import sys, pathlib, re
new, today = sys.argv[1], sys.argv[2]
p = pathlib.Path("RELEASE_NOTES.md")
text = p.read_text()
pat = re.compile(r"^## Unreleased — [0-9]{4}-[0-9]{2}-[0-9]{2}\s*$", re.M)
if not pat.search(text):
    raise SystemExit("RELEASE_NOTES.md missing '## Unreleased — YYYY-MM-DD' section")
text2 = re.sub(r"(?m)^name:\s*.*$", f"name: v{new}", text, count=1)
text2 = re.sub(r"(?m)^version:\s*.*$", f"version: {new}", text2, count=1)
text2 = re.sub(r"(?m)^date:\s*.*$", f"date: {today}", text2, count=1)
text2 = pat.sub(f"## v{new} — {today} — ", text2, count=1)
p.write_text(text2)
print("Folded Unreleased → ## v%s — %s —  (fill in the title)" % (new, today))
PY
echo "Review RELEASE_NOTES.md and VERSION, then:"
echo "  git add RELEASE_NOTES.md VERSION"
echo "  git commit -m \"release: v$NEW — <title>\""
echo "  git tag -a v$NEW -m \"v$NEW — <title>\""
echo "  git push \"$PUSH\" main"
echo "  git push \"$PUSH\" v$NEW"
