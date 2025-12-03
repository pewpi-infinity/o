#!/usr/bin/env python3
# CART315 — Geometry Lens Writer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
GEOMETRY = "CART223_GEOMETRY_EXPANSION.json"
OUTDIR = "CART315_GEOMETRY"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART315] RUO store missing")
    if not os.path.exists(GEOMETRY):
        raise FileNotFoundError("[CART315] geometry expansions missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(GEOMETRY, "r") as f: geo = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        eqs = geo.get(rh, [])

        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Geometry Lens Analysis — {rh}\n\n")

            md.write("## Geometry Equations\n")
            for e in eqs:
                md.write(f"- {e}\n")

            md.write("\n## Interpretation\n")
            md.write("Geometry equations indicate spatial, structural, or volumetric logic inside this RUO.\n")

    print(f"[CART315] Geometry-lens papers → {OUTDIR}")

if __name__ == "__main__":
    main()
