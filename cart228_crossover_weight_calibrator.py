#!/usr/bin/env python3
# CART228 — Crossover Weight Calibrator
# Recalculates crossover_link weights using semantic graph topology.
#
# Inputs:
#   CART217_RUO_STORE.json
#   CART227_SEMANTIC_GRAPH.json
#
# Output:
#   CART228_CALIBRATED_RUOS.json

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
GRAPH = "CART227_SEMANTIC_GRAPH.json"
OUTPUT = "CART228_CALIBRATED_RUOS.json"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART228] Missing RUO store")

    if not os.path.exists(GRAPH):
        raise FileNotFoundError("[CART228] Missing semantic graph")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    with open(GRAPH, "r") as f:
        graph = json.load(f)

    # Convert edges into a lookup table
    edge_map = {}
    for e in graph["edges"]:
        key = (e["from"], e["to"])
        edge_map[key] = e["weight"]
        # also add reverse
        key2 = (e["to"], e["from"])
        edge_map[key2] = e["weight"]

    # Update RUO crossover weights
    for r in ruos:
        new_links = []
        for c in r["crossover_links"]:
            target = c["target_hash"]
            key = (r["research_hash"], target)
            weight = edge_map.get(key, c["weight"])
            new_links.append({
                "target_hash": target,
                "reason": c["reason"],
                "weight": weight
            })
        r["crossover_links"] = new_links

    with open(OUTPUT, "w") as f:
        json.dump(ruos, f, indent=4)

    print(f"[CART228] Calibrated crossover weights saved → {OUTPUT}")

if __name__ == "__main__":
    main()
