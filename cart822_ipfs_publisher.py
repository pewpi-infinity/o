#!/usr/bin/env python3
# CART822 — Token to IPFS Publisher

import json, os

COMP = "CART813_COMPILED.json"
OUT = "CART822_PUBLISH_RESULT.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def main():
    comp = load(COMP, {})
    if not comp:
        print("[CART822] No compiled token.")
        return

    # Browser will upload; this just preps the data
    with open(OUT,"w") as f:
        json.dump({
            "ready": True,
            "token": comp
        }, f, indent=4)

    print("[CART822] Token prepared for IPFS publish.")

if __name__ == "__main__":
    main()
