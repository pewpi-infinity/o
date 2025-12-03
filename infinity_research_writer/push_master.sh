#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)/infinity_research_writer"
BUILD="$ROOT/build"
MASTER_ZIP="$BUILD/master_research.zip"
MANIFEST="$BUILD/manifest.json"
ART_DIR="$(pwd)/artifacts"

echo "[INIT] Push master zip" | tee "$BUILD/push.log"

if [ ! -f "$MASTER_ZIP" ] || [ ! -f "$MANIFEST" ]; then
  echo "[ERROR] Missing artifacts. Run writer first." | tee -a "$BUILD/push.log"
  exit 1
fi

mkdir -p "$ART_DIR"
cp "$MASTER_ZIP" "$ART_DIR/"
cp "$MANIFEST" "$ART_DIR/"

if [ ! -d ".git" ]; then
  echo "[ERROR] No git repo here. Run: git init && git remote add origin <URL>" | tee -a "$BUILD/push.log"
  exit 1
fi

git add artifacts/master_research.zip artifacts/manifest.json

HASH=$(grep -m1 '"sha256"' "$MANIFEST" | sed 's/.*"sha256": "\(.*\)".*/\1/')
COUNT=$(grep -m1 '"pageCount"' "$MANIFEST" | sed 's/[^0-9]*\([0-9]*\).*/\1/')
DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

git commit -m "Infinity master research zip: pages=$COUNT sha256=$HASH date=$DATE"
git push

echo "[VERIFY] artifacts/" | tee -a "$BUILD/push.log"
ls -lh artifacts/ | tee -a "$BUILD/push.log"

echo "[COMPLETE] Push done: sha256=$HASH pages=$COUNT" | tee -a "$BUILD/push.log"
