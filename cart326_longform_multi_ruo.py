#!/usr/bin/env python3
# CART326 — Long‑Form Multi‑RUO Paper Generator

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART326_LONGFORM"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART326] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    batch_size = 5
    for i in range(0, len(ruos), batch_size):
        group = ruos[i:i+batch_size]
        if len(group) < 5:
            break

        fname = f"{OUTDIR}/multi_ruo_{i}.md"
        with open(fname, "w") as md:
            md.write("# Long‑Form Multi‑RUO Research Document\n\n")

            md.write("## 1. Introduction\n")
            md.write("This document synthesizes five RUOs into a unified research framework.\n\n")

            section = 2
            for r in group:
                rh = r["research_hash"]
                md.write(f"## {section}. RUO {rh}\n")
                md.write("### Terms\n")
                for t in r["terms"]:
                    md.write(f"- {t}\n")
                md.write("\n### Links\n")
                for l in r["links"]:
                    md.write(f"- {l}\n")
                md.write("\n### Crossover Structure\n")
                for c in r["crossover_links"]:
                    md.write(f"- {c['target_hash']} ⟶ {c['reason']} (W:{c['weight']})\n")
                md.write("\n---\n")
                section += 1

            md.write("\n## Combined Interpretation\n")
            md.write("This section explores all five RUOs as a single conceptual research engine.\n")

    print("[CART326] Long-form multi-RUO papers → CART326_LONGFORM")

if __name__ == "__main__":
    main()
