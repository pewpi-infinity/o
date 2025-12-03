#!/usr/bin/env python3
# CART230 — RUO Finalizer + Freeze Engine
#
# Freezes RUOs and marks the research_block as finalized.

import json
import os
from datetime import datetime

MASTER = "research_block.json"
CALIBRATED = "CART228_CALIBRATED_RUOS.json"
SEED = "CART229_INFINITY_SEED.json"
OUTPUT = "CART230_FINAL_BLOCK.json"

def main():
    if not os.path.exists(MASTER):
        raise FileNotFoundError("[CART230] research_block.json missing")

    if not os.path.exists(CALIBRATED):
        raise FileNotFoundError("[CART230] Need calibrated RUOs from CART228")

    if not os.path.exists(SEED):
        raise FileNotFoundError("[CART230] Need Infinity Seed from CART229")

    with open(MASTER, "r") as f:
        block = json.load(f)

    with open(CALIBRATED, "r") as f:
        calibrated_ruos = json.load(f)

    with open(SEED, "r") as f:
        seed = json.load(f)

    final = {
        "finalized_at": str(datetime.now()),
        "master_hash": block["master_hash"],
        "infinity_seed": seed,
        "ruos": calibrated_ruos,
        "immutable": True
    }

    with open(OUTPUT, "w") as f:
        json.dump(final, f, indent=4)

    print(f"[CART230] Finalized Infinity Block saved → {OUTPUT}")
    print("[CART230] Block is now immutable.")

if __name__ == "__main__":
    main()
