#!/usr/bin/env python3
# CART219 — Grand Master ZIP Engine
# Creates zip with 4 buckets

import json
import os
import zipfile

SRC = "research_block.json"
OUTZIP = "research_block.zip"

def main():
    if not os.path.exists(SRC):
        raise FileNotFoundError("[CART219] research_block.json missing")

    with open(SRC, "r") as f:
        block = json.load(f)

    with zipfile.ZipFile(OUTZIP, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr("research.json", json.dumps(block["research"], indent=4))
        z.writestr("data_links.json", json.dumps(block["data_links"], indent=4))
        z.writestr("research_plus.json", json.dumps(block["research_plus"], indent=4))
        z.writestr("crossover.json", json.dumps(block["crossover"], indent=4))
        z.writestr("metadata.json", json.dumps({
            "master_hash": block["master_hash"],
            "created": block["created"]
        }, indent=4))

    print(f"[CART219] ZIP created → {OUTZIP}")

if __name__ == "__main__":
    main()
