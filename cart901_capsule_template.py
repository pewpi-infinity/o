#!/usr/bin/env python3
# CART901 — Pewpi Capsule Template

import json

TEMPLATE = {
    "encrypted": True,
    "capsule": "",
    "meta": {
        "created": 0,
        "last_login": 0,
        "version": 1
    }
}

with open("PEWPI_USER_CAPSULE.json","w") as f:
    json.dump(TEMPLATE, f, indent=4)

print("[CART901] Capsule template created.")
