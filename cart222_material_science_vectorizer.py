#!/usr/bin/env python3

import json
import os
import hashlib

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "CART222_MATERIAL_SCIENCE.json"

MATERIAL_DOMAINS = {
    "gold": {"atomic": 79, "type": "metal"},
    "silver": {"atomic": 47, "type": "metal"},
    "copper": {"atomic": 29, "type": "metal"},
    "iron": {"atomic": 26, "type": "metal"},
    "platinum": {"atomic": 78, "type": "metal"},
    "sapphire": {"class": "corundum", "hardness": 9},
    "diamond": {"class": "carbon", "hardness": 10},
    "emerald": {"class": "beryl", "hardness": 7.5},
}

def generate_material_profile(terms):
    profile = {}
    for t in terms:
        if t in MATERIAL_DOMAINS:
            profile[t] = MATERIAL_DOMAINS[t]
    return profile

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART222] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    out = {}

    for r in ruos:
        m = generate_material_profile(r["terms"])
        out[r["research_hash"]] = m

    with open(OUTPUT, "w") as f:
        json.dump(out, f, indent=4)

    print(f"[CART222] Material science vectors → {OUTPUT}")

if __name__ == "__main__":
    main()
