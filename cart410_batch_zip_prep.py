#!/usr/bin/env python3
# CART410 — Batch ZIP Directory Prep

import os, shutil

OUTDIR = "CART410_ZIPSTRUCT"

SUBS = [
    "research", 
    "links",
    "research_plus_links",
    "crossover",
    "index",
    "color"
]

def main():
    if os.path.exists(OUTDIR):
        shutil.rmtree(OUTDIR)

    for s in SUBS:
        os.makedirs(f"{OUTDIR}/{s}", exist_ok=True)

    print("[CART410] Grand Master ZIP structure prepared → CART410_ZIPSTRUCT")

if __name__ == "__main__":
    main()
