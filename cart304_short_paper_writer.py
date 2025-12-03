#!/usr/bin/env python3
# CART304 — Short-Form Research Paper Writer

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
ENTROPY = "CART226_ENTROPY.json"
OUTDIR = "CART304_SHORT_PAPERS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART304] RUO store missing")
    if not os.path.exists(ENTROPY):
        raise FileNotFoundError("[CART304] entropy missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(ENTROPY, "r") as f: entropy = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as f:
            f.write(f"# Short Research Paper — {rh}\n")
            f.write("## Abstract\n")
            f.write("This paper summarizes the key elements of this research unit object, its terms, its links, and its crossover logic.\n\n")

            f.write("## Key Terms\n")
            for t in r["terms"]:
                f.write(f"- {t}\n")

            f.write("\n## Core Insights\n")
            f.write(f"Entropy class: **{entropy.get(rh,{}).get('class','n/a')}**\n\n")

            f.write("## Crossover Interpretation\n")
            for c in r["crossover_links"]:
                f.write(f"- `{c['target_hash']}` → Reason: {c['reason']} (Weight {c['weight']})\n")

            f.write("\n## Conclusion\n")
            f.write("This RUO provides a concise anchor point for broader research pathways.\n")

    print(f"[CART304] Short papers written → {OUTDIR}")

if __name__ == "__main__":
    main()
