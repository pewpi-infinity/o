#!/usr/bin/env python3
# CART324 — Experimental Path Planner

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART324_EXPERIMENTS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART324] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Experimental Path Plan — {rh}\n\n")
            md.write("## Step 1: Define Variables\n")
            for t in r["terms"]:
                md.write(f"- Variable: {t}\n")

            md.write("\n## Step 2: Input Conditions\n")
            for l in r["links"]:
                md.write(f"- Condition sourced from {l}\n")

            md.write("\n## Step 3: Crossover Measures\n")
            for c in r["crossover_links"]:
                md.write(f"- Measure effect of `{c['target_hash']}` via {c['reason']}\n")

            md.write("\n## Expected Outcomes\n")
            md.write("Defined based on RUO metadata + crossover structure.\n")

    print(f"[CART324] Experimental paths → {OUTDIR}")

if __name__ == "__main__":
    main()
