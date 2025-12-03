#!/usr/bin/env python3
# CART429 — Infinity Token Vault Builder

import os, shutil

FILES = [
    "INFINITY_TOKEN.json",
    "INFINITY_TOKEN_SIGNATURE.txt",
    "CART426_LINEAGE.json",
    "CART427_VERSION_HISTORY.json",
    "CART428_TOKEN_REGISTER.json"
]

VAULT = "CART429_VAULT"

def main():
    if os.path.exists(VAULT):
        shutil.rmtree(VAULT)
    os.makedirs(VAULT, exist_ok=True)

    for f in FILES:
        if os.path.exists(f):
            shutil.copy(f, VAULT)

    print("[CART429] Infinity Token Vault built → CART429_VAULT")

if __name__ == "__main__":
    main()
