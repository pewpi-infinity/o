#!/usr/bin/env python3
# CART226 — Entropy Scorer
# Calculates entropy of each RUO based on crossover density,
# term diversity, link diversity, and structural variation.

import json
import os
import math

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "CART226_ENTROPY.json"

def diversity_score(items):
    if not items:
        return 0
    unique = len(set(items))
    return unique / len(items)

def crossover_score(crossovers):
    if not crossovers:
        return 0
    weights = [c["weight"] for c in crossovers]
    return sum(weights) / (len(weights) * 5)

def entropy_calc(ruo):
    terms = ruo["terms"]
    links = ruo["links"]
    cross = ruo["crossover_links"]

    term_div = diversity_score(terms)
    link_div = diversity_score(links)
    cross_div = crossover_score(cross)

    entropy = (term_div + link_div + cross_div) / 3.0
    return entropy

def classify(ent):
    if ent < 0.33:
        return "low"
    elif ent < 0.66:
        return "medium"
    return "high"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART226] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    entropy_map = {}

    for r in ruos:
        e = entropy_calc(r)
        entropy_map[r["research_hash"]] = {
            "entropy": e,
            "class": classify(e)
        }

    with open(OUTPUT, "w") as f:
        json.dump(entropy_map, f, indent=4)

    print(f"[CART226] Entropy scores written → {OUTPUT}")

if __name__ == "__main__":
    main()
