#!/usr/bin/env python3
# CART323 — Hypothesis Generator
# Produces a set of testable hypotheses for each RUO.

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART323_HYPOTHESES"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART323] RUO store missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Hypothesis Set — {rh}\n\n")

            md.write("## Primary Hypothesis\n")
            md.write(f"- The presence of terms {', '.join(r['terms'])} suggests a structural research pattern.\n\n")

            md.write("## Secondary Hypotheses\n")
            for c in r["crossover_links"]:
                md.write(f"- `{rh}` → `{c['target_hash']}` due to *{c['reason']}*.\n")

            md.write("\n## Null Hypothesis\n")
            md.write("Crossover weights do not correlate with conceptual proximity.\n")

    print(f"[CART323] Hypotheses written → {OUTDIR}")

if __name__ == "__main__":
    main()
