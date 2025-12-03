#!/usr/bin/env python3
# CART229 — Infinity Seed Generator
#
# Produces:
#   1. seed_hash (SHA-256)
#   2. seed_bundle (JSON)
#   3. seed_vector (512-D deterministic vector)

import json
import hashlib
import os
import random

MASTER = "research_block.json"
VECTORS = "CART220_VECTORS.json"
OUTPUT = "CART229_INFINITY_SEED.json"

def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def deterministic_vector(seed, dims=512):
    random.seed(int(seed[:16], 16))
    return [round(random.random(), 9) for _ in range(dims)]

def main():
    if not os.path.exists(MASTER):
        raise FileNotFoundError("[CART229] research_block.json missing")

    with open(MASTER, "r") as f:
        block = json.load(f)

    # Primary material for hashing
    base_string = (
        block["master_hash"] +
        str(len(block["research"])) +
        str(len(block["data_links"])) +
        str(len(block["research_plus"])) +
        str(len(block["crossover"]))
    )

    seed_hash = sha256(base_string)

    # Load RUO vectors if available
    vectors = {}
    if os.path.exists(VECTORS):
        with open(VECTORS, "r") as f:
            vectors = json.load(f)

    # Infinity Seed Vector (primary)
    seed_vector = deterministic_vector(seed_hash, 512)

    seed_bundle = {
        "seed_hash": seed_hash,
        "master_hash": block["master_hash"],
        "ruo_count": len(block["research"]),
        "vector_dimensions": 512,
        "vector_seed": seed_vector
    }

    with open(OUTPUT, "w") as f:
        json.dump(seed_bundle, f, indent=4)

    print(f"[CART229] Infinity Seed generated → {OUTPUT}")
    print(f"[CART229] Seed hash:", seed_hash)

if __name__ == "__main__":
    main()
