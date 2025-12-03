#!/usr/bin/env python3
# CART603 — Crossover Evolution Engine
# Gradually evolves crossover weights over time.

import json, os, time

CROSS = "CART226_CROSSOVER_EXPANDED.json"
OUT = "CART603_CROSSOVER_EVOLVED.json"

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def main():
    base = load_json(CROSS, {})
    evolved = load_json(OUT, {"history": []})

    new_state = {}

    for ruo, links in base.items():
        new_links = []
        for link in links:
            w = link.get("weight", 1.0)
            # Simple evolution: strengthen slightly, decay slightly
            w = w * 1.02  # growth
            if w > 10:
                w = 10.0
            link["weight"] = round(w, 4)
            new_links.append(link)
        new_state[ruo] = new_links

    snapshot = {
        "timestamp": int(time.time()),
        "state": new_state
    }

    evolved["history"].append(snapshot)

    with open(OUT, "w") as f:
        json.dump(evolved, f, indent=4)

    print("[CART603] Crossover evolution snapshot →", OUT)

if __name__ == "__main__":
    main()
