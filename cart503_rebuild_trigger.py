#!/usr/bin/env python3
# CART503 — Automatic Rebuild Trigger

import json, os

EVENTS = "CART502_EVENTS.json"
TRIGGER = "CART503_TRIGGER.json"

def main():
    if not os.path.exists(EVENTS):
        print("[CART503] No events found")
        return

    with open(EVENTS, "r") as f:
        ev = json.load(f)

    signal = {"rebuild_needed": False}

    for e in ev:
        if e["type"] == "ruo_count" and e["value"] > 0:
            signal["rebuild_needed"] = True

    with open(TRIGGER, "w") as f:
        json.dump(signal, f, indent=4)

    print("[CART503] Rebuild trigger set:", signal["rebuild_needed"])

if __name__ == "__main__":
    main()
