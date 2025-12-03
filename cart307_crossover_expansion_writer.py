#!/usr/bin/env python3
# CART307 — Crossover Expansion Writer

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART307_CROSSOVER_EXPANSIONS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART307] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    ru_map = {r["research_hash"]: r for r in ruos}

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Crossover Expansion — {rh}\n\n")

            for c in r["crossover_links"]:
                target = ru_map.get(c["target_hash"])
                md.write(f"## Link → `{c['target_hash']}`\n")
                md.write(f"- Reason: {c['reason']}\n")
                md.write(f"- Weight: {c['weight']}\n")
                if target:
                    md.write("\n### Target Terms\n")
                    for t in target["terms"]:
                        md.write(f"- {t}\n")
                    md.write("\n### Target Links\n")
                    for l in target["links"]:
                        md.write(f"- {l}\n")
                md.write("\n---\n")

    print(f"[CART307] Crossover expansions written → {OUTDIR}")

if __name__ == "__main__":
    main()
