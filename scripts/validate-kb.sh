#!/usr/bin/env bash
# validate-kb.sh — Mechanical enforcement for the Sharp Matrix Knowledge Base
#
# Checks:
#   1. Files listed in AGENTS.md tree exist on disk
#   2. Markdown cross-reference links resolve
#   3. Supabase project IDs are consistent
#   4. Docs staleness (not updated in 90+ days)
#
# Usage: ./scripts/validate-kb.sh [--fix-links]
# Exit code: 0 = all checks pass, 1 = failures found

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs"
AGENTS_MD="$REPO_ROOT/AGENTS.md"
ERRORS=0
WARNINGS=0

RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
NC='\033[0m'

error() { echo -e "${RED}ERROR${NC}: $1"; ERRORS=$((ERRORS + 1)); }
warn()  { echo -e "${YELLOW}WARN${NC}:  $1"; WARNINGS=$((WARNINGS + 1)); }
ok()    { echo -e "${GREEN}OK${NC}:    $1"; }

echo "=== Sharp Matrix KB Validation ==="
echo "Repo: $REPO_ROOT"
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# ---------------------------------------------------------------
# Check 1: Files referenced in AGENTS.md exist
# ---------------------------------------------------------------
echo "--- Check 1: AGENTS.md file references ---"

AGENTS_REFS=$(grep -oP '`docs/[^`]+`' "$AGENTS_MD" | tr -d '`' || true)
AGENTS_REFS="$AGENTS_REFS $(grep -oP '`scripts/[^`]+`' "$AGENTS_MD" | tr -d '`' || true)"

AGENTS_COUNT=0
AGENTS_MISSING=0
for ref in $AGENTS_REFS; do
    full_path="$REPO_ROOT/$ref"
    AGENTS_COUNT=$((AGENTS_COUNT + 1))
    if [ ! -e "$full_path" ]; then
        error "AGENTS.md references '$ref' but file does not exist"
        AGENTS_MISSING=$((AGENTS_MISSING + 1))
    fi
done

if [ "$AGENTS_MISSING" -eq 0 ]; then
    ok "All $AGENTS_COUNT file references in AGENTS.md resolve"
fi
echo ""

# ---------------------------------------------------------------
# Check 2: Markdown link validation
# ---------------------------------------------------------------
echo "--- Check 2: Markdown cross-reference links ---"

LINK_COUNT=0
LINK_BROKEN=0

while IFS= read -r mdfile; do
    dir="$(dirname "$mdfile")"
    # Extract relative markdown links: [text](path.md) or [text](path.md#anchor)
    # Exclude lines that are inside backtick code spans (example/template references)
    links=$(grep -v '`\[' "$mdfile" | grep -oP '\]\((?!https?://|mailto:)[^)#]+' | sed 's/\](//' || true)

    for link in $links; do
        # Skip empty or anchor-only
        [ -z "$link" ] && continue
        LINK_COUNT=$((LINK_COUNT + 1))

        target="$dir/$link"
        # Normalize path
        target=$(realpath -m "$target" 2>/dev/null || echo "$target")

        if [ ! -e "$target" ]; then
            error "Broken link in $(basename "$mdfile"): '$link' -> $target"
            LINK_BROKEN=$((LINK_BROKEN + 1))
        fi
    done
done < <(find "$DOCS_DIR" -name '*.md' -type f)

# Also check AGENTS.md itself
dir="$(dirname "$AGENTS_MD")"
links=$(grep -oP '\]\((?!https?://|mailto:)[^)#]+' "$AGENTS_MD" | sed 's/\](//' || true)
for link in $links; do
    [ -z "$link" ] && continue
    LINK_COUNT=$((LINK_COUNT + 1))
    target=$(realpath -m "$dir/$link" 2>/dev/null || echo "$dir/$link")
    if [ ! -e "$target" ]; then
        error "Broken link in AGENTS.md: '$link'"
        LINK_BROKEN=$((LINK_BROKEN + 1))
    fi
done

if [ "$LINK_BROKEN" -eq 0 ]; then
    ok "All $LINK_COUNT markdown links resolve"
fi
echo ""

# ---------------------------------------------------------------
# Check 3: Supabase project ID consistency
# ---------------------------------------------------------------
echo "--- Check 3: Supabase project ID consistency ---"

declare -A KNOWN_IDS=(
    ["xgubaguglsnokjyudgvc"]="Sharp Matrix SSO (identity only — see ADR-012)"
    ["wltuhltnwhudgkkdsvsr"]="HRMS"
    ["mydojctcewxrbwjckuyz"]="Matrix Pipeline"
    ["tiuansahlsgautkjsajk"]="Sharp Matrix Sandbox (not a production app DB)"
    ["ofzcokolkeejgqfjaszq"]="Matrix CDL"
    ["irjrcskfcyierdbefrpk"]="ITSM"
    ["retujkznogwplfrbniet"]="Matrix FM"
    ["yugymdytplmalumtmyct"]="CY Web Site"
    ["ibqheiuakfjoznqzrpfe"]="Lovable Source"
)

# Find all Supabase-like project IDs in docs (20-char lowercase alpha)
UNKNOWN_IDS=0
while IFS= read -r mdfile; do
    ids=$(grep -oP '[a-z]{20,25}\.supabase\.co' "$mdfile" | grep -oP '^[a-z]+' || true)
    for id in $ids; do
        if [ -z "${KNOWN_IDS[$id]+x}" ]; then
            warn "Unknown Supabase project ID '$id' in $(basename "$mdfile")"
            UNKNOWN_IDS=$((UNKNOWN_IDS + 1))
        fi
    done
done < <(find "$DOCS_DIR" -name '*.md' -type f)

# Also check for bare project IDs in backticks
while IFS= read -r mdfile; do
    ids=$(grep -oP '`[a-z]{20,25}`' "$mdfile" | tr -d '`' || true)
    for id in $ids; do
        if [ -n "${KNOWN_IDS[$id]+x}" ]; then
            : # Known ID, fine
        fi
    done
done < <(find "$DOCS_DIR" -name '*.md' -type f)

if [ "$UNKNOWN_IDS" -eq 0 ]; then
    ok "All Supabase project IDs in docs match known instances"
fi
echo ""

# ---------------------------------------------------------------
# Check 4: Doc staleness
# ---------------------------------------------------------------
echo "--- Check 4: Document staleness (90+ days) ---"

STALE_COUNT=0
NINETY_DAYS_AGO=$(date -d '90 days ago' +%s 2>/dev/null || date -v-90d +%s 2>/dev/null || echo 0)

if [ "$NINETY_DAYS_AGO" -gt 0 ]; then
    while IFS= read -r mdfile; do
        # Use git log for last modification date
        last_modified=$(git -C "$REPO_ROOT" log -1 --format='%ct' -- "$mdfile" 2>/dev/null || echo "")
        [ -z "$last_modified" ] && continue
        if [ "$last_modified" -gt 0 ] && [ "$last_modified" -lt "$NINETY_DAYS_AGO" ]; then
            rel_path="${mdfile#$REPO_ROOT/}"
            last_date=$(git -C "$REPO_ROOT" log -1 --format='%ci' -- "$mdfile" 2>/dev/null | cut -d' ' -f1)
            warn "Stale doc (last updated $last_date): $rel_path"
            STALE_COUNT=$((STALE_COUNT + 1))
        fi
    done < <(find "$DOCS_DIR" -name '*.md' -type f)

    if [ "$STALE_COUNT" -eq 0 ]; then
        ok "No stale documents found (all updated within 90 days)"
    else
        warn "$STALE_COUNT documents not updated in 90+ days"
    fi
else
    warn "Could not determine 90-day threshold (date command incompatible)"
fi
echo ""

# ---------------------------------------------------------------
# Summary
# ---------------------------------------------------------------
echo "=== Validation Summary ==="
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"

if [ "$ERRORS" -gt 0 ]; then
    echo -e "${RED}FAILED${NC} — $ERRORS error(s) found"
    exit 1
else
    echo -e "${GREEN}PASSED${NC} — no errors ($WARNINGS warning(s))"
    exit 0
fi
