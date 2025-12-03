#!/usr/bin/env python3
# CART1010 — Export encrypted capsule for IPFS or transfer

import json, time, shutil

SRC = "PEWPI_USER_CAPSULE.json"
DST = f"CART1010_EXPORT_{int(time.time())}.capsule"

shutil.copy(SRC, DST)

print("[CART1010] Capsule exported as:", DST)
