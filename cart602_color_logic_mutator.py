#!/usr/bin/env python3
# CART602 — Color Logic Mutator
# Evolves color biases over time based on Infinity Seed.

import json, os, time, random

SEED = "CART229_INFINITY_SEED.json"
BASE_COLOR_MAP = "C13B0_COLOR_MAP.json"  # optional
OUT = "CART602_COLOR_BIAS_EVOLVED.json"

DEFAULT_COLORS = ["purple","blue","red","green","yellow","orange","pink"]

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def main():
    seed = load_json(SEED, {"vector_seed": [0.5]*128})["vector_seed"]
    base_map = load_json(BASE_COLOR_MAP, {})
    evolved = load_json(OUT, {"history": []})

    # derive a "mutation factor" from seed
    factor = sum(seed[:16]) / max(len(seed[:16]), 1)
    rnd = random.Random(int(factor * 1e6))

    # if no base_map, start with an empty one
    working = dict(base_map)

    # mutate: randomly swap some colors for some terms
    terms = list(working.keys())
    if not terms:
        # bootstrap few fake entries if none exist
        terms = ["hydrogen","entropy","ai","fusion","portal","infinity"]
        for t in terms:
            working[t] = rnd.choice(DEFAULT_COLORS)

    mutated = {}
    for t in terms:
        old_color = working.get(t, rnd.choice(DEFAULT_COLORS))
        if rnd.random() < 0.15:  # 15% chance to mutate
            new_color = rnd.choice(DEFAULT_COLORS)
        else:
            new_color = old_color

        mutated[t] = {
            "previous": old_color,
            "current": new_color
        }

    snapshot = {
        "timestamp": int(time.time()),
        "mutation_factor": factor,
        "mapping": mutated
    }

    evolved["history"].append(snapshot)

    with open(OUT, "w") as f:
        json.dump(evolved, f, indent=4)

    print("[CART602] Color logic mutation snapshot →", OUT)

if __name__ == "__main__":
    main()
