#!/usr/bin/env python3
# CART204 — Master Dictionary Builder
# Combines CART201 + CART202 + CART203 into one research dictionary

import json
import os

IN1 = "CART201_SEARCH_TERMS.json"
IN2 = "CART202_EQUATIONS.json"
IN3 = "CART203_VALIDATED_SITES.json"
OUTPUT = "CART204_MASTER_DICTIONARY.json"

def load(path):
    with open(path, "r") as f:
        return json.load(f)

def main():
    if not all(os.path.exists(p) for p in [IN1, IN2, IN3]):
        raise FileNotFoundError("[CART204] Missing one or more inputs.")

    t = load(IN1)
    e = load(IN2)
    w = load(IN3)

    master = {
        "terms": t["terms"],
        "equations": e,
        "websites": w["valid_sites"],
        "metadata": {
            "total_terms": len(t["terms"]),
            "total_equations": len(e),
            "total_sites": len(w["valid_sites"])
        }
    }

    with open(OUTPUT, "w") as f:
        json.dump(master, f, indent=4)

    print(f"[CART204] Master dictionary created → {OUTPUT}")

if __name__ == "__main__":
    main()
