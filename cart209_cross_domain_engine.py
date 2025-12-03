#!/usr/bin/env python3
# CART209 — Cross-Domain Cartesian Engine
# Produces cross-domain fusion paths:
# (term × equation × site) → research vector

import json
import itertools
import os

INPUT = "CART204_MASTER_DICTIONARY.json"
OUTPUT = "CART209_CROSS_DOMAIN.json"

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError("[CART209] Missing master dictionary")

    with open(INPUT, "r") as f:
        master = json.load(f)

    terms = master["terms"]
    equations = list(master["equations"].keys())
    sites = master["websites"]

    cross_vectors = []

    for t in terms:
        for eq in equations:
            for site in sites:
                cross_vectors.append({
                    "term": t,
                    "equation": eq,
                    "site": site,
                    "query": f"{t} {eq}",
                    "domain_vector": [t, eq, site],
                    "hash_seed": f"{t}:{eq}:{site}"
                })

    with open(OUTPUT, "w") as f:
        json.dump(cross_vectors, f, indent=2)

    print(f"[CART209] Cross-domain vectors → {OUTPUT}")
    print(f"[CART209] Total: {len(cross_vectors)}")

if __name__ == "__main__":
    main()
