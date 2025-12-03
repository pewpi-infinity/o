#!/usr/bin/env python3
# CART319 — Multi-Perspective Research Composer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART319_MULTIPERSPECTIVE"

PERSPECTIVES = [
    "Scientific",
    "Engineering",
    "Historical",
    "Geometry",
    "Material Science",
    "Sci‑Fi Conceptual",
    "CEO Strategic"
]

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART319] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]

        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Multi-Perspective Research Report — {rh}\n\n")

            for p in PERSPECTIVES:
                md.write(f"## {p} View\n")
                md.write("Interpretation of this RUO from this perspective.\n\n")

    print(f"[CART319] Multi-perspective papers → {OUTDIR}")

if __name__ == "__main__":
    main()
