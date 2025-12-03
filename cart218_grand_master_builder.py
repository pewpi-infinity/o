#!/usr/bin/env python3
# CART218 — Grand Master Builder
# Builds grandmaster structure with 4 buckets + nested masters.

import json
import os
import hashlib
from datetime import datetime

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "research_block.json"

def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART218] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    bucket_research = []
    bucket_links = []
    bucket_combined = []
    bucket_crossover = []

    for r in ruos:
        bucket_research.append({
            "research_hash": r["research_hash"],
            "terms": r["terms"],
            "metadata": r["metadata"]
        })

        bucket_links.append({
            "data_links_hash": r["data_links_hash"],
            "links": r["links"]
        })

        bucket_combined.append({
            "research_plus_data_links_hash": r["research_plus_data_links_hash"],
            "combined": r["research_hash"] + r["data_links_hash"]
        })

        bucket_crossover.append({
            "research_hash": r["research_hash"],
            "crossover_links": r["crossover_links"]
        })

    master = {
        "created": str(datetime.now()),
        "research": bucket_research,
        "data_links": bucket_links,
        "research_plus": bucket_combined,
        "crossover": bucket_crossover,
        "nested_masters": []
    }

    master_hash = sha256(json.dumps(master, sort_keys=True))
    master["master_hash"] = master_hash

    with open(OUTPUT, "w") as f:
        json.dump(master, f, indent=4)

    print(f"[CART218] Grand master built → {OUTPUT}")
    print(f"[CART218] Hash: {master_hash}")

if __name__ == "__main__":
    main()
