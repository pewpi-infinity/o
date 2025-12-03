#!/usr/bin/env python3
# CART206 — Trio Fusion Query Builder
# Creates all 3-term intelligent fusion combinations

import json
import itertools
import os

INPUT = "CART204_MASTER_DICTIONARY.json"
OUTPUT = "CART206_TRIO_FUSION.json"

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError("[CART206] Missing CART204_MASTER_DICTIONARY.json")

    with open(INPUT, "r") as f:
        master = json.load(f)

    terms = master["terms"]

    trios = list(itertools.combinations(terms, 3))
    fusion = []

    for a, b, c in trios:
        fusion.append({
            "trio": [a, b, c],
            "query": f"{a} {b} {c}",
            "complexity_score": len(a) + len(b) + len(c)
        })

    with open(OUTPUT, "w") as f:
        json.dump(fusion, f, indent=4)

    print(f"[CART206] Generated {len(fusion)} fused trios → {OUTPUT}")

if __name__ == "__main__":
    main()
