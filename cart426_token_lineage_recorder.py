#!/usr/bin/env python3
# CART426 — Infinity‑Token Lineage Recorder

import json, os, time

TOKEN = "INFINITY_TOKEN.json"
LINEAGE = "CART426_LINEAGE.json"

def main():
    if not os.path.exists(TOKEN):
        raise FileNotFoundError("[CART426] Infinity Token missing")

    with open(TOKEN, "r") as f:
        token = json.load(f)

    entry = {
        "timestamp": int(time.time()),
        "sha256": token["grand_master_sha256"],
        "research_count": token["research_count"],
        "color_distribution": token["color_distribution"]
    }

    if os.path.exists(LINEAGE):
        with open(LINEAGE, "r") as f:
            lineage = json.load(f)
    else:
        lineage = []

    lineage.append(entry)

    with open(LINEAGE, "w") as f:
        json.dump(lineage, f, indent=4)

    print("[CART426] Token lineage updated → CART426_LINEAGE.json")

if __name__ == "__main__":
    main()
