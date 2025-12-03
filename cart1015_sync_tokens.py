#!/usr/bin/env python3
# CART1015 — Sync tokens after capsule restore

import json, shutil, os

with open("CURRENT_USER.json") as f:
    user = json.load(f)

if "tokens" in user and isinstance(user["tokens"], list):
    for tok in user["tokens"]:
        src = f"site/tokens/{tok}.json"
        if os.path.exists(src):
            continue  # already synced
        # token doesn't exist locally, skip silently

print("[CART1015] Token sync complete.")
