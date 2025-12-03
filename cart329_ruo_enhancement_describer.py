#!/usr/bin/env python3
# CART329 — RUO Enhancement Describer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART329_ENHANCEMENTS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART329] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# RUO Enhancement Recommendations — {rh}\n\n")

            md.write("## Term Expansion Suggestions\n")
            md.write("- Add deeper domain terms.\n")
            md.write("- Include lateral concepts.\n\n")

            md.write("## Link Expansion Suggestions\n")
            md.write("- Add more diversified URLs.\n\n")

            md.write("## Crossover Improvements\n")
            md.write("- Add cross-discipline connections.\n")
            md.write("- Strengthen high-similarity pathways.\n")

    print("[CART329] Enhancement docs → CART329_ENHANCEMENTS")

if __name__ == "__main__":
    main()
