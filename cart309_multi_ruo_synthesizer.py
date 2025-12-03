#!/usr/bin/env python3
# CART309 — Multi-RUO Synthesizer

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART309_SYNTHESIS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART309] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    # Use groups of 3 RUOs to generate synthesis docs
    for i in range(0, len(ruos), 3):
        group = ruos[i:i+3]
        if len(group) < 3:
            continue

        fname = f"{OUTDIR}/synthesis_{i}.md"
        with open(fname, "w") as md:
            md.write("# Multi‑RUO Synthesis\n")
            for r in group:
                md.write(f"\n## RUO `{r['research_hash']}`\n")
                for t in r["terms"]:
                    md.write(f"- {t}\n")

            md.write("\n## Combined Insight\n")
            md.write("These three RUOs collectively show:\n")
            md.write("- domain overlap\n")
            md.write("- crossovers\n")
            md.write("- shared metadata\n")

    print(f"[CART309] Multi-RUO syntheses → {OUTDIR}")

if __name__ == "__main__":
    main()
