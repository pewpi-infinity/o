#!/usr/bin/env python3
# CART308 — Semantic Graph Analyzer

import json
import os

GRAPH = "CART227_SEMANTIC_GRAPH.json"
OUT = "CART308_GRAPH_ANALYSIS.md"

def main():
    if not os.path.exists(GRAPH):
        raise FileNotFoundError("[CART308] semantic graph missing")

    with open(GRAPH, "r") as f:
        graph = json.load(f)

    nodes = graph["nodes"]
    edges = graph["edges"]

    with open(OUT, "w") as md:
        md.write("# Semantic Graph Analysis\n")
        md.write(f"- Total Nodes: {len(nodes)}\n")
        md.write(f"- Total Edges: {len(edges)}\n\n")

        md.write("## Top Strongest Edges\n")
        top = sorted(edges, key=lambda x: x["weight"], reverse=True)[:25]
        for e in top:
            md.write(f"- `{e['from']}` → `{e['to']}` (W:{e['weight']})\n")

    print(f"[CART308] Graph analysis written → {OUT}")

if __name__ == "__main__":
    main()
