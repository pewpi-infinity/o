#!/usr/bin/env python3
# CART227 — Semantic Graph Builder
# Builds a weighted semantic graph of all RUOs based on
# crossover density, term similarity, domain overlap,
# entropy, and metadata.
#
# Output is used directly by CART229 (Infinity Seed Generator).

import json
import os
import hashlib

RUO_STORE = "CART217_RUO_STORE.json"
ENTROPY = "CART226_ENTROPY.json"
OUTPUT = "CART227_SEMANTIC_GRAPH.json"

def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def term_similarity(a, b):
    return len(set(a).intersection(set(b)))

def link_domain(url):
    if "://" not in url:
        return None
    parts = url.split("/")
    if len(parts) >= 3:
        return parts[2]
    return None

def domain_overlap(linksA, linksB):
    domA = {link_domain(l) for l in linksA if link_domain(l)}
    domB = {link_domain(l) for l in linksB if link_domain(l)}
    return len(domA.intersection(domB))

def weighted_edge(ruA, ruB, entropy_map):
    t_sim = term_similarity(ruA["terms"], ruB["terms"])
    d_sim = domain_overlap(ruA["links"], ruB["links"])
    crossA = len(ruA["crossover_links"])
    crossB = len(ruB["crossover_links"])

    entA = entropy_map.get(ruA["research_hash"], {}).get("entropy", 0)
    entB = entropy_map.get(ruB["research_hash"], {}).get("entropy", 0)

    # Weighted combination
    weight = (
        (t_sim * 0.4) +
        (d_sim * 0.2) +
        ((crossA + crossB) * 0.1) +
        ((entA + entB) * 0.3)
    )

    if weight <= 0:
        return None

    return weight

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART227] RUO store missing")

    if not os.path.exists(ENTROPY):
        raise FileNotFoundError("[CART227] Entropy file missing. Run CART226 first.")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    with open(ENTROPY, "r") as f:
        entropy_map = json.load(f)

    graph = {
        "nodes": [],
        "edges": []
    }

    # Build nodes
    for r in ruos:
        graph["nodes"].append({
            "id": r["research_hash"],
            "terms": r["terms"],
            "links": r["links"],
            "entropy": entropy_map.get(r["research_hash"], {}).get("entropy", 0)
        })

    # Build weighted edges
    for i in range(len(ruos)):
        for j in range(i + 1, len(ruos)):
            A = ruos[i]
            B = ruos[j]

            w = weighted_edge(A, B, entropy_map)
            if w:
                graph["edges"].append({
                    "from": A["research_hash"],
                    "to": B["research_hash"],
                    "weight": w
                })

    with open(OUTPUT, "w") as f:
        json.dump(graph, f, indent=4)

    print(f"[CART227] Semantic graph generated → {OUTPUT}")
    print(f"[CART227] Nodes:", len(graph["nodes"]))
    print(f"[CART227] Edges:", len(graph["edges"]))

if __name__ == "__main__":
    main()
