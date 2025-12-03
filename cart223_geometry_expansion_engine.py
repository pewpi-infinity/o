#!/usr/bin/env python3

import json
import os
import math

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "CART223_GEOMETRY_EXPANSION.json"

GEOMETRY_EQ = {
    "circle": ["A=πr^2", "C=2πr"],
    "triangle": ["A=1/2bh"],
    "sphere": ["V=4/3πr^3", "SA=4πr^2"],
    "cube": ["V=a^3"],
    "square": ["A=a^2"],
    "torus": ["V=2π^2 R r^2"]
}

def get_geo(terms):
    out = []
    for t in terms:
        if t in GEOMETRY_EQ:
            out.extend(GEOMETRY_EQ[t])
    return list(set(out))

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART223] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    out = {}

    for r in ruos:
        eqs = get_geo(r["terms"])
        out[r["research_hash"]] = eqs

    with open(OUTPUT, "w") as f:
        json.dump(out, f, indent=4)

    print(f"[CART223] Geometry expansions saved → {OUTPUT}")

if __name__ == "__main__":
    main()
