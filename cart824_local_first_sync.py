#!/usr/bin/env python3
# CART824 — Local-first Sync Engine for IPFS

import json, os

IN = "CART822_PUBLISH_RESULT.json"
LEDGER = "WORLD_TOKEN_LEDGER.json"
OUT = "CART824_SYNC_PACKAGE.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def main():
    token = load(IN, {})
    ledger = load(LEDGER, {})

    with open(OUT,"w") as f:
        json.dump({
            "token": token,
            "ledger": ledger
        }, f, indent=4)

    print("[CART824] Sync package prepared.")

if __name__ == "__main__":
    main()
