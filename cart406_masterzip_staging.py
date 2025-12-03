#!/usr/bin/env python3
# CART406 — Master ZIP Staging Directory Builder
import os, json, shutil

MANIFEST = "CART404_MASTERHASH_MANIFEST.json"
STAGING = "CART406_STAGING"

def main():
    if not os.path.exists(MANIFEST):
        raise FileNotFoundError("[CART406] Manifest missing")

    with open(MANIFEST, "r") as f:
        mani = json.load(f)

    if os.path.exists(STAGING):
        shutil.rmtree(STAGING)

    os.makedirs(STAGING, exist_ok=True)

    for entry in mani:
        path = f"{STAGING}/{entry['ruo']}"
        os.makedirs(path, exist_ok=True)

    print("[CART406] Staging directory created → CART406_STAGING")

if __name__ == "__main__":
    main()
