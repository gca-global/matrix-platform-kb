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

AGENTS_REFS_RAW=$(
    {
        grep -oP '`docs/[^`]+`' "$AGENTS_MD" || true
        grep -oP '`scripts/[^`]+`' "$AGENTS_MD" || true
        grep -oP '`raw/[^`]+`' "$AGENTS_MD" || true
    } | tr -d '`'
)

AGENTS_COUNT=0
AGENTS_MISSING=0
while IFS= read -r ref; do
    [ -z "$ref" ] && continue
    # Skip placeholder paths (template-style refs like `wiki/agent-docs/resources/<snake>.md`)
    case "$ref" in
        *'<'*'>'*) continue ;;
    esac
    AGENTS_COUNT=$((AGENTS_COUNT + 1))
    full_path="$REPO_ROOT/$ref"
    if [[ "$ref" == *'*'* ]]; then
        # Glob pattern - check at least one match exists
        # shellcheck disable=SC2086
        match_count=$(compgen -G "$full_path" 2>/dev/null | wc -l)
        if [ "$match_count" -eq 0 ]; then
            error "AGENTS.md references glob '$ref' but no files match"
            AGENTS_MISSING=$((AGENTS_MISSING + 1))
        fi
    elif [ ! -e "$full_path" ]; then
        error "AGENTS.md references '$ref' but file does not exist"
        AGENTS_MISSING=$((AGENTS_MISSING + 1))
    fi
done <<< "$AGENTS_REFS_RAW"

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
# Check 5: reso-dd-kb generated artifacts fresher than source CSVs
# ---------------------------------------------------------------
echo "--- Check 5: reso-dd-kb generated artifacts vs source CSVs ---"

RESO_KB="$DOCS_DIR/data-models/reso-dd-kb"
RESO_INDEX="$RESO_KB/wiki/agent-docs/_index.md"
RESO_FIELDS="$RESO_KB/raw/fields.csv"
RESO_DBML="$RESO_KB/wiki/dbml/canonical.dbml"

if [ -f "$RESO_INDEX" ] && [ -f "$RESO_FIELDS" ]; then
    if [ "$RESO_FIELDS" -nt "$RESO_INDEX" ]; then
        warn "reso-dd-kb: raw/fields.csv newer than wiki/agent-docs/_index.md - re-run scripts/06_emit_agent_docs.py"
    fi
    if [ -f "$RESO_DBML" ] && [ "$RESO_FIELDS" -nt "$RESO_DBML" ]; then
        warn "reso-dd-kb: raw/fields.csv newer than wiki/dbml/canonical.dbml - re-run scripts/05_emit_dbml.py"
    fi
    if [ -z "${WARNINGS_RESO_KB+x}" ]; then
        ok "reso-dd-kb generated artifacts are at least as fresh as raw/fields.csv"
    fi
else
    warn "reso-dd-kb expected at $RESO_KB but key files missing (USAGE.md or raw/fields.csv)"
fi
echo ""

# ---------------------------------------------------------------
# Check 6: source-mappings generated artifacts fresher than inputs
# ---------------------------------------------------------------
echo "--- Check 6: source-mappings freshness ---"

SM="$DOCS_DIR/data-models/source-mappings"
SM_CURATED="$SM/raw/mapping_curated.csv"
SM_DASH_INV="$SM/raw/dash_inventory.csv"
SM_QOBRIX_INV="$SM/raw/qobrix_inventory.csv"
SM_CBP_INV="$SM/raw/cbp_inventory.csv"
SM_INDEX="$SM/wiki/agent-docs/_index.md"

if [ -d "$SM" ] && [ -f "$SM_CURATED" ]; then
    # Per-resource alignment freshness vs corresponding by_resource doc.
    for res in property member office contacts teams media; do
        align="$SM/raw/alignment_$res.csv"
        doc="$SM/wiki/agent-docs/by_resource/$res.md"
        if [ -f "$align" ] && [ -f "$doc" ] && [ "$align" -nt "$doc" ]; then
            warn "source-mappings: alignment_$res.csv newer than by_resource/$res.md - re-run scripts/05_emit_mapping_docs.py"
        fi
    done

    # Curated CSV vs inventories: if any inventory is newer than the
    # curated CSV, upstream sources changed and the curator should
    # review whether new rows are needed.
    for inv in "$SM_DASH_INV" "$SM_QOBRIX_INV" "$SM_CBP_INV"; do
        if [ -f "$inv" ] && [ "$inv" -nt "$SM_CURATED" ]; then
            warn "source-mappings: $(basename "$inv") newer than mapping_curated.csv - upstream changed; review curated rows for new/removed labels"
        fi
    done

    # Index freshness vs alignments.
    if [ -f "$SM_INDEX" ]; then
        for align in "$SM"/raw/alignment_*.csv; do
            [ -f "$align" ] || continue
            if [ "$align" -nt "$SM_INDEX" ]; then
                warn "source-mappings: $(basename "$align") newer than wiki/agent-docs/_index.md - re-run scripts/05_emit_mapping_docs.py"
            fi
        done
    fi

    ok "source-mappings present (curated + alignments + emitted markdown checked for freshness)"
else
    warn "source-mappings expected at $SM but key files missing (raw/mapping_curated.csv)"
fi
echo ""

# ---------------------------------------------------------------
# Check 7: canonical-processes generated artifacts fresher than inputs
# ---------------------------------------------------------------
echo "--- Check 7: canonical-processes freshness ---"

CP="$DOCS_DIR/business-processes/canonical-processes"
CP_CITATIONS="$CP/raw/citations.csv"
CP_COVERAGE="$CP/raw/coverage.csv"
CP_INDEX="$CP/wiki/agent-docs/_index.md"
CP_SM="$CP/wiki/agent-docs/state_machines.md"

if [ -d "$CP" ] && [ -d "$CP/processes" ]; then
    process_count=$(find "$CP/processes" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')

    if [ "$process_count" -lt 10 ]; then
        warn "canonical-processes: only $process_count process file(s) under processes/; canonical baseline expects 10"
    fi

    # Validate-citations output freshness vs hand-edited processes.
    if [ -f "$CP_CITATIONS" ]; then
        for proc in "$CP"/processes/*.md; do
            [ -f "$proc" ] || continue
            if [ "$proc" -nt "$CP_CITATIONS" ]; then
                warn "canonical-processes: $(basename "$proc") newer than raw/citations.csv - re-run scripts/01_validate_citations.py"
            fi
        done
    else
        warn "canonical-processes: raw/citations.csv missing - run scripts/01_validate_citations.py"
    fi

    # Emit output freshness vs citations (and processes).
    for out in "$CP_INDEX" "$CP_SM" "$CP_COVERAGE"; do
        if [ ! -f "$out" ]; then
            warn "canonical-processes: $(basename "$out") missing - run scripts/02_emit_index.py"
            continue
        fi
        if [ -f "$CP_CITATIONS" ] && [ "$CP_CITATIONS" -nt "$out" ]; then
            warn "canonical-processes: raw/citations.csv newer than $(basename "$out") - re-run scripts/02_emit_index.py"
        fi
        for proc in "$CP"/processes/*.md; do
            [ -f "$proc" ] || continue
            if [ "$proc" -nt "$out" ]; then
                warn "canonical-processes: $(basename "$proc") newer than $(basename "$out") - re-run scripts/02_emit_index.py"
                break
            fi
        done
    done

    ok "canonical-processes present ($process_count process file(s); citations + emit outputs checked for freshness)"
else
    warn "canonical-processes expected at $CP but key files missing (processes/ dir)"
fi
echo ""

# ---------------------------------------------------------------
# Check 8: integration (Layer 5) freshness vs Layer 1-3 indexes
# ---------------------------------------------------------------
echo "--- Check 8: integration freshness ---"

INT="$DOCS_DIR/integration"
INT_INDEX="$INT/wiki/agent-docs/_index.md"
INT_BY_RES="$INT/wiki/agent-docs/by_resource"
INT_CSV="$INT/raw/integration_index.csv"

# Source-of-record indexes Layer 5 joins on.
RDD_INDEX="$DOCS_DIR/data-models/reso-dd-kb/wiki/agent-docs/_index.md"
SM_ALIGN_DIR="$DOCS_DIR/data-models/source-mappings/raw"
CP_CITATIONS_LOCAL="$DOCS_DIR/business-processes/canonical-processes/raw/citations.csv"

if [ -d "$INT" ] && [ -f "$INT/scripts/01_emit_resource_views.py" ]; then
    page_count=$(find "$INT_BY_RES" -maxdepth 1 -name '*.md' 2>/dev/null | wc -l | tr -d ' ')

    if [ ! -f "$INT_INDEX" ] || [ ! -f "$INT_CSV" ] || [ "$page_count" -eq 0 ]; then
        warn "integration: outputs missing (run scripts/01_emit_resource_views.py)"
    else
        # Cross-chapter freshness: every upstream index newer than
        # any integration output is a stale-output warning.
        for upstream in "$RDD_INDEX" "$CP_CITATIONS_LOCAL" "$SM_ALIGN_DIR"/alignment_*.csv; do
            [ -f "$upstream" ] || continue
            for downstream in "$INT_INDEX" "$INT_CSV" "$INT_BY_RES"/*.md; do
                [ -f "$downstream" ] || continue
                if [ "$upstream" -nt "$downstream" ]; then
                    warn "integration: $(basename "$upstream") newer than $(basename "$downstream") - re-run docs/integration/scripts/01_emit_resource_views.py"
                    break 2
                fi
            done
        done
    fi

    ok "integration present ($page_count per-resource page(s); cross-chapter freshness checked vs reso-dd-kb, source-mappings, canonical-processes)"
else
    warn "integration expected at $INT but emit script missing"
fi
echo ""

# ---------------------------------------------------------------
# Check 9: CDL seed corpus freshness vs reso-dd-kb raw CSVs
# ---------------------------------------------------------------
echo "--- Check 9: CDL seed corpus freshness ---"

RDD_RAW="$DOCS_DIR/data-models/reso-dd-kb/raw"
CDL_SEED="$DOCS_DIR/data-models/reso-dd-kb/wiki/cdl/reso_full_corpus.sql"
CDL_EMIT="$DOCS_DIR/data-models/reso-dd-kb/scripts/07_emit_cdl_seed.py"

if [ -f "$CDL_EMIT" ]; then
    if [ ! -f "$CDL_SEED" ]; then
        warn "cdl seed missing: run docs/data-models/reso-dd-kb/scripts/07_emit_cdl_seed.py"
    else
        stale=0
        for upstream in "$RDD_RAW/resources.csv" "$RDD_RAW/fields.csv" \
                        "$RDD_RAW/field_definitions.csv" "$RDD_RAW/lookup_values.csv"; do
            [ -f "$upstream" ] || continue
            if [ "$upstream" -nt "$CDL_SEED" ]; then
                warn "cdl seed: $(basename "$upstream") newer than reso_full_corpus.sql - re-run scripts/07_emit_cdl_seed.py"
                stale=1
                break
            fi
        done
        if [ "$stale" -eq 0 ]; then
            row_count=$(grep -c '^  (' "$CDL_SEED" 2>/dev/null || echo 0)
            ok "cdl seed present ($row_count VALUES rows; fresh vs raw/{resources,fields,field_definitions,lookup_values}.csv)"
        fi
    fi
else
    warn "cdl seed emit script missing at $CDL_EMIT"
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
