#!/usr/bin/env python3
# CART328 — Graph Narrative Writer

import json, os

GRAPH = "CART227_SEMANTIC_GRAPH.json"
OUT = "CART328_GRAPH_NARRATIVE.md"

def main():
    if not os.path.exists(GRAPH):
        raise FileNotFoundError("[CART328] graph file missing")

    with open(GRAPH, "r") as f:
        graph = json.load(f)

    nodes = graph["nodes"]
    edges = sorted(graph["edges"], key=lambda x: x["weight"], reverse=True)

    with open(OUT, "w") as md:
        md.write("# Graph Narrative Analysis\n\n")

        md.write("## Overview\n")
        md.write(f"- Total Nodes: {len(nodes)}\n")
        md.write(f"- Total Edges: {len(edges)}\n\n")

        md.write("## Strongest Connections (Narrative)\n")
        for e in edges[:40]:
            md.write(f"- `{e['from']}` is strongly linked to `{e['to']}`.\n")
            md.write(f"  This relationship is weighted at **{e['weight']}**, suggesting high conceptual density.\n\n")

    print("[CART328] Graph narrative written → CART328_GRAPH_NARRATIVE.md")

if __name__ == "__main__":
    main()
