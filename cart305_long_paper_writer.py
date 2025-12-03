#!/usr/bin/env python3
# CART305 — Long-Form Research Paper Writer
# Generates detailed multi-section papers.

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART305_LONG_PAPERS"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART305] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as f:
            f.write(f"# Long-Form Research Paper — {rh}\n\n")
            f.write("## 1. Introduction\n")
            f.write("This document provides an expanded research analysis...\n\n")

            f.write("## 2. Terms\n")
            for t in r["terms"]:
                f.write(f"- {t}\n")

            f.write("\n## 3. Link Overview\n")
            for l in r["links"]:
                f.write(f"- {l}\n")

            f.write("\n## 4. Metadata\n")
            f.write(str(r["metadata"]) + "\n")

            f.write("\n## 5. Crossover Analysis\n")
            for c in r["crossover_links"]:
                f.write(f"- `{c['target_hash']}` — {c['reason']} (W:{c['weight']})\n")

            f.write("\n## 6. Structural Interpretation\n")
            f.write("This section analyzes how this RUO connects across the entire research network.\n")

            f.write("\n## 7. Domain Impact\n")
            f.write("Potential applications are explored here.\n")

            f.write("\n## 8. Expansion Potential\n")
            f.write("Future crossover expansions described.\n")

            f.write("\n## 9. System Integration\n")
            f.write("How this RUO contributes to the Infinity OS.\n")

            f.write("\n## 10. Conclusion\n")
            f.write("Final remarks.\n")

    print(f"[CART305] Long papers written → {OUTDIR}")

if __name__ == "__main__":
    main()
