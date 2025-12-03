#!/usr/bin/env python3
# CART703 — Category Page Builder

import os, json

TERM_FEED = "CART352_TERM_FEED.json"

def main():
    if not os.path.exists(TERM_FEED):
        print("[CART703] Missing term feed.")
        return

    with open(TERM_FEED, "r") as f:
        terms = json.load(f)

    categories = sorted(set(t.lower().strip().replace(" ","_") for t in terms))

    for cat in categories:
        path = f"site/{cat}.html"
        with open(path, "w") as f:
            f.write(f"<html><body><h1>{cat.title()}</h1><div id='content'></div></body></html>")
        print("[CART703] Created", path)

if __name__ == "__main__":
    main()
