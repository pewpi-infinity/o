#!/usr/bin/env python3
# CART314 — Material‑Science Lens Writer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
MATERIAL = "CART222_MATERIAL_SCIENCE.json"
OUTDIR = "CART314_MATERIAL"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART314] RUO store missing")
    if not os.path.exists(MATERIAL):
        raise FileNotFoundError("[CART314] material science vectors missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(MATERIAL, "r") as f: ms = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        profile = ms.get(rh, {})

        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Material‑Science Analysis — {rh}\n\n")

            md.write("## Material Matches\n")
            for k, v in profile.items():
                md.write(f"- **{k}** → {v}\n")

            md.write("\n## Interpretation\n")
            md.write("Material signals help map research to elemental or mineralogical domains.\n")

    print(f"[CART314] Material-science papers → {OUTDIR}")

if __name__ == "__main__":
    main()
