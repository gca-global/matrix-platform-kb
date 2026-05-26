#!/usr/bin/env bash
# wiki-lint.sh — contract enforcer for the matrix-pipeline LLM Wiki.
# Runs on every PR touching matrix-platform-kb/docs/product-specs/matrix-pipeline/.
#
# Checks:
#   1. Frontmatter validity        — required keys present in every wiki/*.md
#   2. Orphan H2 anchors           — declared {#x} but no inbound link
#   3. FR-ID coverage parity       — FR-IDs in raw/ also appear in wiki/
#   4. Split-rule warnings         — pages > 600 lines, single H2 > 200 lines
#   5. log.md prefix consistency   — every entry starts with `## [YYYY-MM-DD] <action> | `
#
# Exit codes:
#   0  — all checks green
#   1  — at least one hard failure (1, 2, 3, 5)
#   (split-rule findings are warn-only and never fail the lint.)

set -euo pipefail

# Resolve subtree root: parent of the scripts/ directory containing this file.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RAW="$ROOT/raw/context-v2.md"
WIKI_DIR="$ROOT/wiki"
LOG="$ROOT/log.md"

FAILED=0
WARNED=0

red()    { printf '\033[0;31m%s\033[0m\n' "$*"; }
yellow() { printf '\033[0;33m%s\033[0m\n' "$*"; }
green()  { printf '\033[0;32m%s\033[0m\n' "$*"; }
bold()   { printf '\033[1m%s\033[0m\n' "$*"; }

fail() { red   "FAIL: $*"; FAILED=1; }
warn() { yellow "WARN: $*"; WARNED=1; }
ok()   { green "OK:   $*"; }

bold "── matrix-pipeline wiki-lint ───────────────────────────────"
bold "Root: $ROOT"
echo

# ─────────────────────────────────────────────────────────────
# 1. Frontmatter validity
# ─────────────────────────────────────────────────────────────
bold "[1/5] Frontmatter validity"
REQUIRED_KEYS=("title" "status" "source" "last_updated" "tags")

if [[ ! -d "$WIKI_DIR" ]]; then
  fail "wiki/ directory not found at $WIKI_DIR"
else
  for f in "$WIKI_DIR"/*.md; do
    [[ -f "$f" ]] || continue
    # frontmatter is the first --- … --- block; bail if the file does not start with ---
    FIRST_LINE="$(head -n 1 "$f")"
    if [[ "$FIRST_LINE" != "---" ]]; then
      fail "$(basename "$f"): missing leading '---' frontmatter delimiter"
      continue
    fi
    FM="$(awk '/^---$/{c++; next} c==1{print} c==2{exit}' "$f")"
    for key in "${REQUIRED_KEYS[@]}"; do
      if ! grep -qE "^${key}:" <<<"$FM"; then
        fail "$(basename "$f"): missing frontmatter key '$key'"
      fi
    done
  done
  # phases.md (lives at subtree root) follows the same anatomy
  if [[ -f "$ROOT/phases.md" ]]; then
    FIRST_LINE="$(head -n 1 "$ROOT/phases.md")"
    if [[ "$FIRST_LINE" != "---" ]]; then
      fail "phases.md: missing leading '---' frontmatter delimiter"
    else
      FM="$(awk '/^---$/{c++; next} c==1{print} c==2{exit}' "$ROOT/phases.md")"
      for key in "${REQUIRED_KEYS[@]}"; do
        if ! grep -qE "^${key}:" <<<"$FM"; then
          fail "phases.md: missing frontmatter key '$key'"
        fi
      done
    fi
  fi
fi
[[ $FAILED -eq 0 ]] && ok "frontmatter complete on all pages"
echo

# ─────────────────────────────────────────────────────────────
# 2. Orphan H2 anchors
#    Anchor declared as `## ... {#kebab-case}` but no inbound link
#    (`#kebab-case`) anywhere in the subtree.
# ─────────────────────────────────────────────────────────────
bold "[2/5] Orphan H2 anchors"
ORPHANS=0
while IFS= read -r -d '' file; do
  while IFS= read -r anchor; do
    # Look for inbound references to this anchor anywhere in the subtree (excluding raw/).
    if ! grep -RIn --exclude-dir=raw --exclude-dir=scripts "#${anchor}" "$ROOT" >/dev/null 2>&1; then
      warn "orphan anchor: $(basename "$file") #${anchor}"
      ORPHANS=$((ORPHANS+1))
    fi
  done < <(grep -oE '\{#[a-z0-9-]+\}' "$file" | tr -d '{}#')
done < <(find "$WIKI_DIR" "$ROOT/phases.md" "$ROOT/INDEX.md" -maxdepth 2 -name '*.md' -print0 2>/dev/null)
if [[ $ORPHANS -eq 0 ]]; then
  ok "no orphan anchors"
else
  warn "$ORPHANS orphan anchor(s) detected (warn-only)"
fi
echo

# ─────────────────────────────────────────────────────────────
# 3. FR-ID coverage parity
#    Every FR-XXX-NN id present in raw/ must also appear at least
#    once in wiki/ (it can be on any wiki page).
# ─────────────────────────────────────────────────────────────
bold "[3/5] FR-ID coverage parity (raw/ ↔ wiki/)"
if [[ ! -f "$RAW" ]]; then
  warn "raw/context-v2.md not present — skipping FR parity check"
else
  RAW_FRS="$(grep -oE 'FR-[A-Z]+(-[A-Z]+)*-[0-9]+' "$RAW" | sort -u || true)"
  WIKI_FRS="$(grep -RhoE 'FR-[A-Z]+(-[A-Z]+)*-[0-9]+' "$WIKI_DIR" 2>/dev/null | sort -u || true)"
  MISSING=0
  while IFS= read -r fr; do
    [[ -z "$fr" ]] && continue
    if ! grep -q "^${fr}$" <<<"$WIKI_FRS"; then
      fail "FR-ID present in raw/ but missing from wiki/: $fr"
      MISSING=$((MISSING+1))
    fi
  done <<<"$RAW_FRS"
  RAW_COUNT=$(grep -c . <<<"$RAW_FRS" || true)
  WIKI_COUNT=$(grep -c . <<<"$WIKI_FRS" || true)
  echo "    raw FR-IDs: $RAW_COUNT, wiki FR-IDs: $WIKI_COUNT"
  if [[ $MISSING -eq 0 ]]; then
    ok "every raw FR-ID is referenced in wiki/"
  fi
fi
echo

# ─────────────────────────────────────────────────────────────
# 4. Split-rule warnings (warn-only)
# ─────────────────────────────────────────────────────────────
bold "[4/5] Split-rule warnings (warn-only)"
SPLITS=0
for f in "$WIKI_DIR"/*.md "$ROOT/phases.md"; do
  [[ -f "$f" ]] || continue
  LINES=$(wc -l <"$f")
  if (( LINES > 600 )); then
    warn "page > 600 lines: $(basename "$f") ($LINES)"
    SPLITS=$((SPLITS+1))
  fi
  # Largest H2 section length: scan H2 boundaries, measure deltas.
  LARGEST_H2=$(awk '
    /^## / {
      if (start) { delta = NR - 1 - start; if (delta > max) { max = delta; maxhdr = hdr } }
      start = NR; hdr = $0
    }
    END {
      if (start) { delta = NR - start; if (delta > max) { max = delta; maxhdr = hdr } }
      print max, maxhdr
    }
  ' "$f")
  H2_LEN=$(echo "$LARGEST_H2" | awk '{print $1}')
  H2_HDR=$(echo "$LARGEST_H2" | cut -d' ' -f2-)
  if [[ "${H2_LEN:-0}" -gt 200 ]]; then
    warn "H2 > 200 lines: $(basename "$f") :: $H2_HDR ($H2_LEN lines)"
    SPLITS=$((SPLITS+1))
  fi
done
if [[ $SPLITS -eq 0 ]]; then
  ok "no split-rule triggers"
fi
echo

# ─────────────────────────────────────────────────────────────
# 5. log.md prefix consistency
# ─────────────────────────────────────────────────────────────
bold "[5/5] log.md prefix consistency"
if [[ ! -f "$LOG" ]]; then
  fail "log.md not found at $LOG"
else
  BAD=0
  while IFS= read -r line; do
    if ! [[ "$line" =~ ^##\ \[[0-9]{4}-[0-9]{2}-[0-9]{2}\]\ [a-z-]+\ \|\  ]]; then
      fail "log.md bad header: $line"
      BAD=$((BAD+1))
    fi
  done < <(grep -E '^## \[' "$LOG" || true)
  if [[ $BAD -eq 0 ]]; then
    ok "all log.md headers conform"
  fi
fi
echo

# ─────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────
bold "── Summary ─────────────────────────────────────────────────"
if [[ $FAILED -ne 0 ]]; then
  red "FAILED — fix the issues above before merging."
  exit 1
fi
if [[ $WARNED -ne 0 ]]; then
  yellow "WARNINGS — passing, but please review."
else
  green "All checks green."
fi
exit 0
