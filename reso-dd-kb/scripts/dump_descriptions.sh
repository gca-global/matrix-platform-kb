#!/usr/bin/env bash
# Dump public.reso_field_descriptions from the Atlas Supabase project to
# raw/field_descriptions.csv.
#
# Requires PSQL_URL (the project pooler URL with read access). Idempotent.
#
# Usage:
#   PSQL_URL=postgres://...@db.<project>.supabase.co:6543/postgres \
#     reso-dd-kb/scripts/dump_descriptions.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/raw/field_descriptions.csv"

if [[ -z "${PSQL_URL:-}" ]]; then
  echo "PSQL_URL env var is required" >&2
  exit 2
fi

psql "$PSQL_URL" -At -c "\\copy (
  SELECT field, locale, description, wiki_url, lookups_url, dd_version, source, updated_at
  FROM public.reso_field_descriptions
  ORDER BY field
) TO STDOUT WITH CSV HEADER" > "$OUT"

echo "wrote $(wc -l < "$OUT") lines to $OUT"
