#!/bin/bash
set -euo pipefail

echo "[INIT] Infinity Repo Push"
echo "[PATH] $(pwd)"

# Stage everything that was written
git add -A
echo "[STAGE] All artifacts staged"

# Commit with loud provenance message
git commit -m "[PUSH] Infinity artifacts: pages, resources zip, master zip"
echo "[COMMIT] Commit created"

# Push to main branch with loud logs
git push origin main --verbose
echo "[PUSH] Artifacts pushed to main"
