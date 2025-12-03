#!/usr/bin/env python3
# CART815 — Token Registration Engine

import json, os, time

TOKENS = "CART803_TOKENS.json"
COMP = "CART813_COMPILED.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def save(p,d):
    json.dump(d, open(p,"w"), indent=4)

def main():
    tokens = load(TOKENS, {"tokens":{}})
    comp = load(COMP, {})

    if not comp:
        print("[CART815] No compiled token found.")
        return

    tid = comp["hash"][:12]  # short id
    tokens["tokens"][tid] = comp

    save(TOKENS, tokens)

    print("[CART815] Token registered as", tid)

if __name__ == "__main__":
    main()
