#!/usr/bin/env python3
# CART1016 — Sync ledger after capsule restore

import json

with open("CURRENT_USER.json") as f:
    user = json.load(f)

with open("CART805_WALLET.json","w") as f:
    json.dump(user.get("ledger",{}),f,indent=4)

print("[CART1016] Ledger synced.")
