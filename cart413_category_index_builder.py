#!/usr/bin/env python3
# CART413 — Category Index Builder

import os, json

ROUTER = "CART405_ROUTER.json"
OUTDIR = "CART410_ZIPSTRUCT/index"

CATEGORIES = [
    "AI", "quantum", "astronomy", "materials", "geology", "gemstones",
    "jewelry", "chemistry", "biology", "engineering", "electronics",
    "mythology", "ancient", "history", "soil", "nature", "carpentry",
    "plumbing", "space", "signals", "future", "math", "geometry"
]

def main():
    if not os.path.exists(ROUTER):
        raise FileNotFoundError("[CART413] Router missing")

    with open(ROUTER, "r") as f:
        router = json.load(f)

    # Create category index files
    for cat in CATEGORIES:
        with open(f"{OUTDIR}/{cat}.md", "w") as md:
            md.write(f"# {cat} Research Index\n\n")

    # Populate categories
    for r in router:
        ruo = r["ruo"]
        for cat in CATEGORIES:
            if cat in ruo.lower():
                with open(f"{OUTDIR}/{cat}.md", "a") as md:
                    md.write(f"- {ruo}\n")

    print("[CART413] Category indexes created → /index")

if __name__ == "__main__":
    main()
