#!/usr/bin/env python3
# CART508 — Hazard Recovery System

import os, json, hashlib

LOG = "CART508_HAZARD_LOG.json"
FILES_TO_CHECK = [
    "grand_master.zip",
    "INFINITY_TOKEN.json",
    "CART404_MASTERHASH_MANIFEST.json"
]

def filehash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def main():
    hazards = []

    for f in FILES_TO_CHECK:
        if not os.path.exists(f):
            hazards.append({"file": f, "issue": "missing"})
        else:
            try:
                filehash(f)
            except:
                hazards.append({"file": f, "issue": "corrupt"})

    with open(LOG, "w") as f:
        json.dump(hazards, f, indent=4)

    print("[CART508] Hazard scan complete:", len(hazards), "issues detected.")

if __name__ == "__main__":
    main()
