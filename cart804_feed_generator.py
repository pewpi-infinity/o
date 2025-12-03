#!/usr/bin/env python3
# CART804 — Feed Generator (Infinite Scroll Logic)

import json, os, time, random

RUO = "CART217_RUO_STORE.json"
EVOLVE = "CART601_EVOLVED_TERMS.json"
CROSS = "CART603_CROSSOVER_EVOLVED.json"
FEED = "CART804_FEED_BUFFER.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def save(p,d):
    json.dump(d, open(p,"w"), indent=4)

def main():
    ruos = load(RUO, [])
    evo = load(EVOLVE, {"history":[]})
    cross = load(CROSS, {"history":[]})
    feed = load(FEED, {"tiles":[]})

    # grab last snapshots
    evo_terms = evo["history"][-1]["evolved_terms"] if evo["history"] else []
    cross_map = cross["history"][-1]["state"] if cross["history"] else {}

    # tile logic
    tile = {
        "time": int(time.time()),
        "terms": random.sample(evo_terms, min(3,len(evo_terms))) if evo_terms else [],
        "message": "Logic-placed tile via Infinity-OS feed engine.",
        "crossover_links": len(cross_map),
        "ruo_count": len(ruos)
    }

    feed["tiles"].append(tile)
    save(FEED, feed)

    print("[CART804] Tile added to feed.")

if __name__ == "__main__":
    main()
