#!/usr/bin/env python3
# CART301 — RUO Summarizer
# Produces readable Markdown summaries for each RUO.

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART301_SUMMARIES"

def md_escape(s):
    return s.replace("_", "\\_")

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART301] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        fname = f"{OUTDIR}/{r['research_hash']}.md"
        with open(fname, "w") as f:
            f.write(f"# RUO Summary — {r['research_hash']}\n\n")
            f.write("## Terms\n")
            for t in r["terms"]:
                f.write(f"- {md_escape(t)}\n")
            f.write("\n## Links\n")
            for l in r["links"]:
                f.write(f"- {l}\n")
            f.write("\n## Crossover Links\n")
            for c in r["crossover_links"]:
                f.write(f"- **Target:** `{c['target_hash']}` — Reason: {c['reason']} (Weight: {c['weight']})\n")

    print(f"[CART301] RUO summaries written → {OUTDIR}")

if __name__ == "__main__":
    main()
