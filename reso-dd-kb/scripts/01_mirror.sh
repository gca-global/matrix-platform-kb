#!/usr/bin/env bash
#
# Mirror dd.reso.org/DD2.0/ into reso-dd-kb/mirror/DD2.0/.
#
# Politeness:
#   - 1 req/s with random jitter
#   - real User-Agent with a contact email
#   - --execute robots=on (dd.reso.org returns 404 for robots.txt;
#     wget treats that as "no restrictions" but we keep the flag on
#     so a future robots.txt is automatically respected)
#   - full crawl log to _meta/crawl.log
#
# After wget exits, scripts/_emit_manifest.py walks the mirror tree
# and emits _meta/manifest.json (URL, local path, status, size, sha256).
#
# Re-runnable: wget --mirror uses --timestamping under the hood, so a
# second run only refetches changed pages.
set -euo pipefail

KB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MIRROR_DIR="$KB_ROOT/mirror"
META_DIR="$KB_ROOT/_meta"
SCRIPT_DIR="$KB_ROOT/scripts"

UA='matrix-platform-kb-mirror/1.0 (+https://github.com/sharpsir/matrix-platform-kb; sergey@sharpsir.com)'

mkdir -p "$MIRROR_DIR" "$META_DIR"

echo "[01_mirror] target:  $MIRROR_DIR"
echo "[01_mirror] log:     $META_DIR/crawl.log"
echo "[01_mirror] start:   $(date -Iseconds)"

# Snapshot robots.txt for the record (even if it's a 404).
curl -sS -A "$UA" -o "$META_DIR/robots.txt" \
  -w '[01_mirror] robots.txt status: %{http_code}, %{size_download} bytes\n' \
  https://dd.reso.org/robots.txt || true

cd "$MIRROR_DIR"

# wget exits non-zero if any page returns >= 400. We keep going so
# the manifest can record the failures, then re-raise via the
# manifest gate below.
set +e
wget \
  --mirror \
  --no-parent \
  --convert-links \
  --adjust-extension \
  --page-requisites \
  --no-host-directories \
  --domains=dd.reso.org \
  --wait=1 --random-wait \
  --user-agent="$UA" \
  --execute robots=on \
  --retry-connrefused \
  --tries=3 \
  --waitretry=5 \
  --output-file="$META_DIR/crawl.log" \
  https://dd.reso.org/DD2.0/
WGET_RC=$?
set -e

echo "[01_mirror] wget rc:  $WGET_RC"
echo "[01_mirror] end:     $(date -Iseconds)"

# Build manifest.json from the crawl log + the on-disk tree.
python3 "$SCRIPT_DIR/_emit_manifest.py"

# Hard gate: refuse to declare success if any URL did not return 200.
MANIFEST="$META_DIR/manifest.json" python3 - <<'PY'
import json, os, sys
data = json.loads(open(os.environ["MANIFEST"]).read())
bad = [e for e in data["entries"] if e["status"] != 200]
if bad:
    print(f"[01_mirror] FAIL: {len(bad)} URLs did not return 200; first 10:")
    for e in bad[:10]:
        print(f"  {e['status']}  {e['url']}")
    sys.exit(2)
print(f"[01_mirror] OK: {len(data['entries'])} URLs, all status 200")
PY
