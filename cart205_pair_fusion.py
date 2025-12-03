#!/usr/bin/env python3
# CART205 — Pair Fusion Query Builder
# Creates all 2-term fusion combinations from master dictionary

import json
import itertools
import os

INPUT = "CART204_MASTER_DICTIONARY.json"
OUTPUT = "CART205_PAIR_FUSION.json"

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError("[CART205] Missing CART204_MASTER_DICTIONARY.json")

    with open(INPUT, "r") as f:
        master = json.load(f)

    terms = master["terms"]
    pairs = list(itertools.combinations(terms, 2))

    fusion = []
    for a, b in pairs:
        fusion.append({
            "pair": [a, b],
            "query": f"{a} {b}",
            "score": len(a) + len(b)   # crude relevance; extended later
        })

    with open(OUTPUT, "w") as f:
        json.dump(fusion, f, indent=4)

    print(f"[CART205] Generated {len(fusion)} fused pairs → {OUTPUT}")

if __name__ == "__main__":
    main()
