#!/usr/bin/env python3
# CART502 — Research Event Watcher

import os, json, time

RUO = "CART217_RUO_STORE.json"
STATE = "CART501_STATE.json"
OUT = "CART502_EVENTS.json"

def main():
    if not os.path.exists(STATE):
        print("[CART502] Kernel state missing, run CART501 first")
        return

    events = []

    # watch RUO count
    if os.path.exists(RUO):
        with open(RUO, "r") as f:
            ruos = json.load(f)
        events.append({"type": "ruo_count", "value": len(ruos)})

    with open(OUT, "w") as f:
        json.dump(events, f, indent=4)

    print("[CART502] Research events recorded")

if __name__ == "__main__":
    main()
