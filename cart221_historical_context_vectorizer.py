#!/usr/bin/env python3

import json
import os
import hashlib
import random

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "CART221_HISTORICAL_CONTEXT.json"

HISTORICAL_MAP = {
    "egypt": "ancient_civilization",
    "sumer": "ancient_civilization",
    "rome": "classical_empire",
    "greece": "classical_philosophy",
    "mythology": "mythic_system",
    "scripture": "religious_text",
    "alchemy": "proto_science",
    "astronomy": "early_cosmology",
    "geometry": "greek_mathematics",
    "alchemy": "transmutation_system"
}

def classify(terms):
    tags = []
    for t in terms:
        if t in HISTORICAL_MAP:
            tags.append(HISTORICAL_MAP[t])
    return list(set(tags))

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART221] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    out = {}

    for r in ruos:
        classes = classify(r["terms"])
        out[r["research_hash"]] = {
            "historical_tags": classes,
            "weight": len(classes)
        }

    with open(OUTPUT, "w") as f:
        json.dump(out, f, indent=4)

    print(f"[CART221] Historical context vectors written → {OUTPUT}")

if __name__ == "__main__":
    main()
