#!/usr/bin/env python3
# CART823 — Global Token Ledger

import json, os, time

LEDGER = "WORLD_TOKEN_LEDGER.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def save(p,d):
    json.dump(d, open(p,"w"), indent=4)

def main():
    ledger = load(LEDGER, {"count":0,"history":[]})

    ledger["count"] += 1
    ledger["history"].append({
        "time": int(time.time()),
        "event": "token_generated",
        "total": ledger["count"]
    })

    save(LEDGER, ledger)
    print("[CART823] Global ledger incremented:", ledger["count"])

if __name__ == "__main__":
    main()
