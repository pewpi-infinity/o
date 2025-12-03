#!/usr/bin/env python3
# CART427 — Infinity‑Token Version History Builder

import json, os, time

TOKEN = "INFINITY_TOKEN.json"
HISTORY = "CART427_VERSION_HISTORY.json"

def main():
    if not os.path.exists(TOKEN):
        raise FileNotFoundError("[CART427] Infinity Token missing")

    with open(TOKEN, "r") as f:
        token = json.load(f)

    entry = {
        "version": len(token["color_distribution"]),
        "timestamp": int(time.time()),
        "token_sha": token["grand_master_sha256"]
    }

    if os.path.exists(HISTORY):
        with open(HISTORY, "r") as f:
            hist = json.load(f)
    else:
        hist = []

    hist.append(entry)

    with open(HISTORY, "w") as f:
        json.dump(hist, f, indent=4)

    print("[CART427] Version history updated → CART427_VERSION_HISTORY.json")

if __name__ == "__main__":
    main()
