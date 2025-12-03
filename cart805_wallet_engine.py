#!/usr/bin/env python3
# CART805 — Wallet Engine

import json, os, time

WALLET = "CART805_WALLET.json"

def load(path,d):
    return json.load(open(path)) if os.path.exists(path) else d

def save(path,d):
    json.dump(d, open(path,"w"), indent=4)

def main():
    wallet = load(WALLET, {"balance":0,"history":[]})
    save(WALLET, wallet)
    print("[CART805] Wallet engine initialized.")

if __name__ == "__main__":
    main()
