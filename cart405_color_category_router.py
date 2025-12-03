#!/usr/bin/env python3
# CART405 — 7-Color Category Router

import json, os, hashlib

INFINITY_SEED = "CART229_INFINITY_SEED.json"
MANIFEST = "CART404_MASTERHASH_MANIFEST.json"
OUT = "CART405_ROUTER.json"

COLORS = ["green","red","blue","pink","orange","purple","yellow"]

def main():
    if not os.path.exists(INFINITY_SEED):
        raise FileNotFoundError("[CART405] Missing Infinity seed")
    if not os.path.exists(MANIFEST):
        raise FileNotFoundError("[CART405] Missing masterhash manifest")

    with open(INFINITY_SEED, "r") as f:
        seed = json.load(f)["vector_seed"]

    with open(MANIFEST, "r") as f:
        mani = json.load(f)

    vec_index = int(sum(seed[:50]) * 1000)  # steer categories via vector

    router = []
    for entry in mani:
        idx = int(hashlib.sha256(entry["ruo"].encode()).hexdigest(), 16)
        color = COLORS[(idx + vec_index) % len(COLORS)]
        entry["color_category"] = color
        router.append(entry)

    with open(OUT, "w") as f:
        json.dump(router, f, indent=4)

    print("[CART405] Color routing table →", OUT)

if __name__ == "__main__":
    main()
