#!/usr/bin/env python3
# CART325 — Resource / URL Planner

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART325_RESOURCES"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART325] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Resource Plan — {rh}\n\n")

            md.write("## URLs\n")
            for l in r["links"]:
                md.write(f"- {l}\n")

            md.write("\n## Resource Categories\n")
            md.write("- Data sources\n")
            md.write("- Background material\n")
            md.write("- Cross-domain references\n\n")

            md.write("## Acquisition Strategy\n")
            md.write("Structured step-by-step resource acquisition.\n")

    print(f"[CART325] Resource plans → {OUTDIR}")

if __name__ == "__main__":
    main()
