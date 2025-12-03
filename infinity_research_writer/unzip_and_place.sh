#!/usr/bin/env bash
set -euo pipefail

ART_DIR="artifacts"
ZIP="$ART_DIR/master_research.zip"
MANIFEST="$ART_DIR/manifest.json"
OUT_DIR="infinity_tokens"

echo "[INIT] Unzipper" | tee unzip.log
mkdir -p "$OUT_DIR"

if [ ! -f "$ZIP" ] || [ ! -f "$MANIFEST" ]; then
  echo "[ERROR] Missing master zip or manifest in artifacts/" | tee -a unzip.log
  exit 1
fi

echo "[UNZIP] Extracting pages..." | tee -a unzip.log
unzip -o "$ZIP" -d "$OUT_DIR" >/dev/null

echo "[INDEX] Building UI index..." | tee -a unzip.log

python3 - << 'PYEND' | tee -a unzip.log
import json, os

MANIFEST = "artifacts/manifest.json"
OUT_DIR = "infinity_tokens"

with open(MANIFEST) as f:
    m = json.load(f)

entries = []
for p in m.get("pages", []):
    entries.append({
        "file": p["file"],
        "term": p["term"],
        "anchors": p["anchors"],
        "links": [f"link://{a}/{p['term']}" for a in p["anchors"]],
        "valuation": p.get("valuation", {})
    })

index = {
    "version": m.get("version"),
    "count": len(entries),
    "masterHash": m.get("masterZip", {}).get("sha256"),
    "entries": entries
}

with open(os.path.join(OUT_DIR, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2)

print(f"[DONE] index.json created with {len(entries)} entries.")
PYEND

echo "[LIST] Sample files:" | tee -a unzip.log
ls -1 "$OUT_DIR" | head -n 10 | tee -a unzip.log

echo "[COMPLETE] Unzip and index ready." | tee -a unzip.log
