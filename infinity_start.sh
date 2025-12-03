#!/bin/bash

echo "[∞] Starting Infinity‑OS…"

# move into project directory
cd "$(dirname "$0")"

echo "[∞] Ensuring permissions…"
find . -type f -name "*.py" -exec chmod +x {} \;
chmod -R +x site/js/*.js

echo "[∞] Launching local web server on port 8080…"
python3 -m http.server 8080 >/dev/null 2>&1 &

echo "[∞] Starting heartbeat engine…"
node site/js/heartbeat.js >/dev/null 2>&1 &

echo "[∞] Starting auto-writer…"
./cart11001_auto_writer.py >/dev/null 2>&1 &

echo "[∞] Starting integrity auditor…"
./cart11002_integrity_audit.py >/dev/null 2>&1 &

echo "[∞] Infinity‑OS is online."
echo "Open in your browser:  http://localhost:8080/site/interface/mode.html"
