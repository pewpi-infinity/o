#!/usr/bin/env python3
# CART425 — Infinity‑Token Signature Engine

import hashlib, json

TOKEN = "INFINITY_TOKEN.json"
SIGNATURE = "INFINITY_TOKEN_SIGNATURE.txt"

def main():
    with open(TOKEN, "r") as f:
        data = f.read()

    sig = hashlib.sha256(data.encode()).hexdigest()

    with open(SIGNATURE, "w") as f:
        f.write(sig + "\n")

    print("[CART425] Token signature created → INFINITY_TOKEN_SIGNATURE.txt")

if __name__ == "__main__":
    main()
