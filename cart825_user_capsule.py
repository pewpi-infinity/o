#!/usr/bin/env python3
# CART825 — User Account Capsule (local encrypted storage)

import json, os

CAPSULE = "PEWPI_USER_CAPSULE.json"

template = {
    "encrypted": True,
    "user": None,
    "capsule": None
}

with open(CAPSULE, "w") as f:
    json.dump(template, f, indent=4)

print("[CART825] Pewpi account capsule created.")
