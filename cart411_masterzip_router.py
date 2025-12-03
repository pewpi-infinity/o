#!/usr/bin/env python3
# CART411 — Master ZIP Router → Grand Structure

import json, os, shutil

ROUTER = "CART405_ROUTER.json"
MASTERZIPS = "CART408_MASTERZIPS"
OUTDIR = "CART410_ZIPSTRUCT"

def main():
    if not os.path.exists(ROUTER):
        raise FileNotFoundError("[CART411] Missing router file")
    if not os.path.exists(MASTERZIPS):
        raise FileNotFoundError("[CART411] Missing master zip directory")
    if not os.path.exists(OUTDIR):
        raise FileNotFoundError("[CART411] Missing prepared ZIPSTRUCT")

    with open(ROUTER, "r") as f:
        router = json.load(f)

    for r in router:
        ruo = r["ruo"]
        color = r["color_category"]
        zipname = f"{MASTERZIPS}/{ruo}.zip"

        if os.path.exists(zipname):
            target = f"{OUTDIR}/color/{color}"
            os.makedirs(target, exist_ok=True)
            shutil.copy(zipname, target)

    print("[CART411] Routed master zips into color categories")

if __name__ == "__main__":
    main()
