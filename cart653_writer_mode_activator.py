#!/usr/bin/env python3
# CART653 — Writer Mode Activator

import os, json, time

FREEZE = "CART652_FREEZE_MODE.json"
OUT = "CART653_WRITER_MODE.json"

def main():
    mode = {
        "writer_enabled": True,
        "timestamp": int(time.time())
    }

    if os.path.exists(FREEZE):
        with open(FREEZE, "r") as f:
            fr = json.load(f)
        if fr.get("mode") == "frozen":
            print("[CART653] Cannot enable writer: freeze mode active.")
            return

    with open(OUT, "w") as f:
        json.dump(mode, f, indent=4)

    print("[CART653] Writer mode ENABLED. System will generate new 10k zips daily.")

if __name__ == "__main__":
    main()
