#!/usr/bin/env python3
# CART303 — Research Weaver
# Combines signals from history, geometry, sci-fi mappings, materials, entropy,
# and crossover structure into one integrated Markdown analysis per RUO.

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
ENTROPY = "CART226_ENTROPY.json"
HISTORY = "CART221_HISTORICAL_CONTEXT.json"
MATERIAL = "CART222_MATERIAL_SCIENCE.json"
GEOMETRY = "CART223_GEOMETRY_EXPANSION.json"
SCIFI = "CART224_SCIFI_MAP.json"
OUTDIR = "CART303_WEAVES"

def main():
    required = [RUO_STORE, ENTROPY, HISTORY, MATERIAL, GEOMETRY, SCIFI]
    for r in required:
        if not os.path.exists(r):
            raise FileNotFoundError(f"[CART303] Missing {r}")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(ENTROPY, "r") as f: entropy = json.load(f)
    with open(HISTORY, "r") as f: history = json.load(f)
    with open(MATERIAL, "r") as f: material = json.load(f)
    with open(GEOMETRY, "r") as f: geometry = json.load(f)
    with open(SCIFI, "r") as f: scifi = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as f:
            f.write(f"# Research Weave — {rh}\n\n")
            f.write("## Core Terms\n")
            for t in r["terms"]:
                f.write(f"- {t}\n")

            f.write("\n## Historical Context\n")
            f.write(str(history.get(rh, {})) + "\n")

            f.write("\n## Material Science Notes\n")
            f.write(str(material.get(rh, {})) + "\n")

            f.write("\n## Geometry Expansion\n")
            for eq in geometry.get(rh, []):
                f.write(f"- {eq}\n")

            f.write("\n## Sci‑Fi → Science Mapping\n")
            for s in scifi.get(rh, []):
                f.write(f"- {s}\n")

            f.write("\n## Entropy\n")
            f.write(str(entropy.get(rh, {})) + "\n")

            f.write("\n## Crossover Links\n")
            for c in r["crossover_links"]:
                f.write(f"- `{c['target_hash']}` — {c['reason']} (W:{c['weight']})\n")

    print(f"[CART303] Research weaves written → {OUTDIR}")

if __name__ == "__main__":
    main()
