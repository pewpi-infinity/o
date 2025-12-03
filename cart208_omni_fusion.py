#!/usr/bin/env python3
# CART208 — Omni Fusion Engine
# Generates multi-term fusion queries (5-term up to ALL)
# WARNING: Produces MASSIVE output sets.

import json
import itertools
import os

INPUT = "CART204_MASTER_DICTIONARY.json"
OUTPUT = "CART208_OMNI_FUSION.json"

def generate_fusions(terms):
    all_fusion_sets = []
    # Build from 5-term up to ALL terms
    for r in range(5, min(len(terms) + 1, 12)):  # limit at 12-term for sanity
        combos = itertools.combinations(terms, r)
        for c in combos:
            all_fusion_sets.append({
                "terms": list(c),
                "query": " ".join(c),
                "depth": r,
                "signature": sum(len(x) for x in c)
            })
    return all_fusion_sets

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError("[CART208] Missing master dictionary")

    with open(INPUT, "r") as f:
        master = json.load(f)

    terms = master["terms"]
    fusion = generate_fusions(terms)

    with open(OUTPUT, "w") as f:
        json.dump(fusion, f, indent=2)

    print(f"[CART208] Omni fusion sets generated → {OUTPUT}")
    print(f"[CART208] Total sets: {len(fusion)}")

if __name__ == "__main__":
    main()
