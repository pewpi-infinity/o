#!/usr/bin/env python3
# CART220 — Scientific Vectorizer
# Generates pseudo‑semantic vectors for RUOs (no scraping)

import json
import os
import hashlib
import random

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "CART220_VECTORS.json"

def vectorize(ruo):
    random.seed(int(ruo["research_hash"][:8], 16))
    return [random.random() for _ in range(2048)]

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART220] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    vectors = {}

    for r in ruos:
        vectors[r["research_hash"]] = vectorize(r)

    with open(OUTPUT, "w") as f:
        json.dump(vectors, f, indent=4)

    print(f"[CART220] Scientific vectors generated → {OUTPUT}")

if __name__ == "__main__":
    main()
