#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
LOCK="version_locks/STEM-NATION-COUNCIL-ARRIVAL-V1/files"
STAMP="$(date +%Y%m%d_%H%M%S)"
BACKUP="version_locks/pre_restore_backups/council_arrival_v1_$STAMP.tar.gz"
test -d "$LOCK" || { echo "ERROR: snapshot missing"; exit 1; }
echo "Verifying locked snapshot..."
(cd "$LOCK" && sha256sum -c ../SHA256SUMS.txt)
echo "Creating safety backup..."
tar -czf "$BACKUP" templates static web_app.py 2>/dev/null || true
echo "Restoring locked files..."
cp -a "$LOCK/." .
python -m py_compile web_app.py
echo "RESTORE COMPLETE"
echo "Safety backup: $BACKUP"
