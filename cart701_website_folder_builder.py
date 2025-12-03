#!/usr/bin/env python3
# CART701 — Website Folder Builder

import os

DIRS = [
    "site",
    "site/assets",
    "site/js",
    "site/css",
    "site/data"
]

def main():
    for d in DIRS:
        os.makedirs(d, exist_ok=True)
        print(f"[CART701] Created: {d}")

if __name__ == "__main__":
    main()
