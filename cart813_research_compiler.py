#!/usr/bin/env python3
# CART813 — Research Compiler

import json, os, hashlib, time

DRAFT = "CART812_CONVERSATE_DRAFT.json"
OUT = "CART813_COMPILED.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def hash_text(t):
    return hashlib.sha256(t.encode()).hexdigest()

def main():
    draft = load(DRAFT, {})
    if not draft:
        print("[CART813] No draft.")
        return

    text = draft["paper"]
    h = hash_text(text)
    
    compiled = {
        "hash": h,
        "text": text,
        "outline": draft["outline"],
        "timestamp": int(time.time())
    }

    with open(OUT,"w") as f:
        json.dump(compiled,f,indent=4)

    print("[CART813] Compiled token built:", h)

if __name__ == "__main__":
    main()
