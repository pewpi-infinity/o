#!/usr/bin/env python3
# CART322 — Scientific Calendar Planner
# Builds project plans from RUO data.

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART322_CALENDAR"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART322] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for index, r in enumerate(ruos):
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Scientific Calendar Plan — {rh}\n\n")
            md.write("## Day 1: Term Review\n")
            for t in r["terms"]:
                md.write(f"- {t}\n")
            md.write("\n## Day 2: Link Analysis\n")
            for l in r["links"]:
                md.write(f"- {l}\n")
            md.write("\n## Day 3: Crossover Work\n")
            for c in r["crossover_links"]:
                md.write(f"- {c['target_hash']} (reason: {c['reason']})\n")
            md.write("\n## Day 4–7: Deep Research Window\n")
            md.write("Interpret and expand this RUO.\n")

    print(f"[CART322] Calendar plans → {OUTDIR}")

if __name__ == "__main__":
    main()
