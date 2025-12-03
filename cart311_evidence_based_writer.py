#!/usr/bin/env python3
# CART311 — Evidence-Based Writer
# Generates Markdown files using ONLY URL and metadata evidence.

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART311_EVIDENCE_PAPERS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART311] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Evidence-Based Research Report — {rh}\n\n")

            md.write("## Source Links (Evidence)\n")
            for l in r["links"]:
                md.write(f"- {l}\n")

            md.write("\n## Metadata\n")
            md.write(f"- Created: {r['metadata'].get('created')}\n")

            md.write("\n## Interpretation\n")
            md.write("Evidence-based reasoning is derived strictly from link presence and metadata.\n")

            md.write("\n## Crossover Evidence\n")
            for c in r["crossover_links"]:
                md.write(f"- `{c['target_hash']}` (Reason: {c['reason']}, W:{c['weight']})\n")

    print(f"[CART311] Evidence papers written → {OUTDIR}")

if __name__ == "__main__":
    main()
