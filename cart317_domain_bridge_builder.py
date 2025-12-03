#!/usr/bin/env python3
# CART317 — Domain Bridge Builder

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
GRAPH = "CART227_SEMANTIC_GRAPH.json"
OUTDIR = "CART317_DOMAIN_BRIDGES"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART317] RUO store missing")
    if not os.path.exists(GRAPH):
        raise FileNotFoundError("[CART317] semantic graph missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(GRAPH, "r") as f: graph = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    # Quick lookup
    weights = {}
    for e in graph["edges"]:
        weights.setdefault(e["from"], []).append((e["to"], e["weight"]))

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        bridges = sorted(weights.get(rh, []), key=lambda x: x[1], reverse=True)

        with open(fname, "w") as md:
            md.write(f"# Domain Bridge Report — {rh}\n\n")

            md.write("## Strongest Bridges\n")
            for t, w in bridges[:10]:
                md.write(f"- `{rh}` ↔ `{t}` (W:{w})\n")

            md.write("\n## Interpretation\n")
            md.write("These edges represent conceptual bridges across domains.\n")

    print(f"[CART317] Domain bridge files → {OUTDIR}")

if __name__ == "__main__":
    main()
