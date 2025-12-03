#!/usr/bin/env python3
# CART414 — 7‑Color OS Interface Builder

import os, json

ROUTER = "CART405_ROUTER.json"
OUTDIR = "CART410_ZIPSTRUCT/color"

COLORS = ["green","red","blue","pink","orange","purple","yellow"]

def main():
    if not os.path.exists(ROUTER):
        raise FileNotFoundError("[CART414] Router missing")

    with open(ROUTER, "r") as f:
        router = json.load(f)

    for c in COLORS:
        with open(f"{OUTDIR}/{c}/{c}.md", "w") as md:
            md.write(f"# {c.upper()} MODE\n\n")
            md.write("This mode displays research aligned with this cognitive role.\n\n")

    for r in router:
        color = r["color_category"]
        ruo = r["ruo"]
        with open(f"{OUTDIR}/{color}/{color}.md", "a") as md:
            md.write(f"- {ruo}.zip\n")

    print("[CART414] 7-color interface built")

if __name__ == "__main__":
    main()
