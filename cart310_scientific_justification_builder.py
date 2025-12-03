#!/usr/bin/env python3
# CART310 — Scientific Justification Builder

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
GEOMETRY = "CART223_GEOMETRY_EXPANSION.json"
OUTDIR = "CART310_JUSTIFICATIONS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART310] RUO store missing")
    if not os.path.exists(GEOMETRY):
        raise FileNotFoundError("[CART310] geometry missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(GEOMETRY, "r") as f: geometry = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Scientific Justification — {rh}\n\n")
            md.write("## Relevant Equations\n")
            for eq in geometry.get(rh, []):
                md.write(f"- {eq}\n")
            md.write("\n## Interpretation\n")
            md.write("Equations support domain relationships...\n")

    print(f"[CART310] Scientific justifications → {OUTDIR}")

if __name__ == "__main__":
    main()
