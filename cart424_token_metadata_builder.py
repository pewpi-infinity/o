#!/usr/bin/env python3
# CART424 — Infinity‑Token Metadata Builder

import os, json, hashlib, time

GRAND = "grand_master.zip"
ROUTER = "CART405_ROUTER.json"
OUT = "INFINITY_TOKEN.json"

def filehash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not os.path.exists(GRAND):
        raise FileNotFoundError("[CART424] grand_master.zip missing")
    if not os.path.exists(ROUTER):
        raise FileNotFoundError("[CART424] router missing")

    with open(ROUTER, "r") as f:
        router = json.load(f)

    color_count = {}
    for r in router:
        c = r["color_category"]
        color_count[c] = color_count.get(c, 0) + 1

    token = {
        "infinity_token_version": 1,
        "timestamp": int(time.time()),
        "grand_master_sha256": filehash(GRAND),
        "research_count": len(router),
        "color_distribution": color_count,
        "lineage": "InfinityOS Stage‑4 Master"
    }

    with open(OUT, "w") as f:
        json.dump(token, f, indent=4)

    print("[CART424] Infinity Token metadata created → INFINITY_TOKEN.json")

if __name__ == "__main__":
    main()
