#!/usr/bin/env python3
# CART207 — Quad Fusion Query Builder
# Generates all 4-term fusion chains (heavy).

import json
import itertools
import os

INPUT = "CART204_MASTER_DICTIONARY.json"
OUTPUT = "CART207_QUAD_FUSION.json"

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError("[CART207] Missing master dictionary")

    with open(INPUT, "r") as f:
        master = json.load(f)

    terms = master["terms"]

    quads = list(itertools.combinations(terms, 4))
    fusion = []

    for q in quads:
        fusion.append({
            "quad": list(q),
            "query": " ".join(q),
            "complexity_score": sum(len(x) for x in q)
        })

    with open(OUTPUT, "w") as f:
        json.dump(fusion, f, indent=2)

    print(f"[CART207] Generated {len(fusion)} quad fusions → {OUTPUT}")

if __name__ == "__main__":
    main()
