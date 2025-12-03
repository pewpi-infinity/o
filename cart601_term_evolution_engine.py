#!/usr/bin/env python3
# CART601 — Term Evolution Engine
# Evolves term sets over time based on RUO usage and seed term feed.

import json, os, time
from collections import Counter

RUO_STORE = "CART217_RUO_STORE.json"
TERM_FEED = "CART352_TERM_FEED.json"
OUT = "CART601_EVOLVED_TERMS.json"

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def main():
    ruos = load_json(RUO_STORE, [])
    seed_terms = load_json(TERM_FEED, [])
    prev = load_json(OUT, {"history": []})

    # 1. Collect all terms from RUOs
    all_terms = []
    for r in ruos:
        all_terms.extend(r.get("terms", []))

    freq = Counter(all_terms)
    top_terms = [t for t, _ in freq.most_common(100)]

    # 2. Generate evolved terms (simple combinatorics / mutations)
    evolved = []
    for t in top_terms:
        t_norm = t.replace(" ", "_")
        evolved.append(f"{t_norm}_v2")
        evolved.append(f"{t_norm}_deep")
        evolved.append(f"{t_norm}_x")

    # 3. Mix in some seed terms not currently dominant
    extra = [t for t in seed_terms if t not in top_terms][:50]

    snapshot = {
        "timestamp": int(time.time()),
        "top_terms": top_terms,
        "evolved_terms": evolved,
        "extra_seed_terms": extra
    }

    prev["history"].append(snapshot)

    with open(OUT, "w") as f:
        json.dump(prev, f, indent=4)

    print("[CART601] Term evolution snapshot written →", OUT)

if __name__ == "__main__":
    main()
