#!/usr/bin/env python3
# CART652 — Freeze Mode Switch

import json, sys

OUT = "CART652_FREEZE_MODE.json"

def main():
    if len(sys.argv) < 2:
        print("Usage: ./cart652_freeze_mode_switch.py active|frozen")
        return

    mode = sys.argv[1].lower()
    if mode not in ["active","frozen"]:
        print("Mode must be 'active' or 'frozen'")
        return

    with open(OUT, "w") as f:
        json.dump({"mode": mode}, f, indent=4)

    print(f"[CART652] Freeze mode set → {mode}")

if __name__ == "__main__":
    main()
