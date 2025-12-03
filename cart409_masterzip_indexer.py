#!/usr/bin/env python3
# CART409 — Master ZIP Index Builder

import os, json

MANIFEST = "CART404_MASTERHASH_MANIFEST.json"
ROUTER = "CART405_ROUTER.json"
OUT = "CART409_MASTERZIP_INDEX.md"

def main():
    if not os.path.exists(MANIFEST):
        raise FileNotFoundError("[CART409] Manifest missing")
    if not os.path.exists(ROUTER):
        raise FileNotFoundError("[CART409] Router missing")

    with open(MANIFEST, "r") as f:
        mani = json.load(f)
    with open(ROUTER, "r") as f:
        router = json.load(f)

    color_map = {}
    for r in router:
        color_map[r["ruo"]] = r["color_category"]

    with open(OUT, "w") as md:
        md.write("# Master ZIP Index\n\n")
        for entry in mani:
            ruo = entry["ruo"]
            color = color_map.get(ruo, "unknown")
            md.write(f"- `{ruo}.zip` — **{color}**\n")

    print("[CART409] Master ZIP index → CART409_MASTERZIP_INDEX.md")

if __name__ == "__main__":
    main()
