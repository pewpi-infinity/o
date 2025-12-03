#!/usr/bin/env python3
# CART604 — Evolution History Recorder
# Aggregates snapshots from 601/602/603 into a single history file.

import json, os, time

TERMS = "CART601_EVOLVED_TERMS.json"
COLORS = "CART602_COLOR_BIAS_EVOLVED.json"
CROSS = "CART603_CROSSOVER_EVOLVED.json"
OUT = "CART604_EVOLUTION_LOG.json"

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def main():
    terms = load_json(TERMS, {})
    colors = load_json(COLORS, {})
    cross = load_json(CROSS, {})
    log = load_json(OUT, {"entries": []})

    entry = {
        "timestamp": int(time.time()),
        "terms_snapshot_index": len(terms.get("history", [])) - 1,
        "colors_snapshot_index": len(colors.get("history", [])) - 1,
        "crossover_snapshot_index": len(cross.get("history", [])) - 1
    }

    log["entries"].append(entry)

    with open(OUT, "w") as f:
        json.dump(log, f, indent=4)

    print("[CART604] Evolution history updated →", OUT)

if __name__ == "__main__":
    main()
