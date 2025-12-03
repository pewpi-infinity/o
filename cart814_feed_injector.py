#!/usr/bin/env python3
# CART814 — Feed Injector

import json, os, time

FEED = "CART804_FEED_BUFFER.json"
COMP = "CART813_COMPILED.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def save(p,d):
    json.dump(d, open(p,"w"), indent=4)

def main():
    feed = load(FEED, {"tiles":[]})
    comp = load(COMP, {})

    if not comp:
        print("[CART814] No compiled token.")
        return

    tile = {
        "type":"token",
        "hash":comp["hash"],
        "preview": comp["text"][:200],
        "time": int(time.time())
    }

    feed["tiles"].append(tile)
    save(FEED, feed)

    print("[CART814] Token tile added to feed.")

if __name__ == "__main__":
    main()
