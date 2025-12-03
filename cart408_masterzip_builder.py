#!/usr/bin/env python3
# CART408 — Master ZIP Builder

import os, json, zipfile

STAGING = "CART406_STAGING"
OUTDIR = "CART408_MASTERZIPS"

def main():
    if not os.path.exists(STAGING):
        raise FileNotFoundError("[CART408] Staging folder missing")

    os.makedirs(OUTDIR, exist_ok=True)

    for ruo in os.listdir(STAGING):
        path = f"{STAGING}/{ruo}"
        if not os.path.isdir(path):
            continue

        zipname = f"{OUTDIR}/{ruo}.zip"
        with zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(path):
                for file in files:
                    fp = os.path.join(root, file)
                    arc = fp.replace(f"{STAGING}/", "")
                    zipf.write(fp, arc)

    print("[CART408] Master ZIPs → CART408_MASTERZIPS")

if __name__ == "__main__":
    main()
