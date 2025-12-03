#!/usr/bin/env python3
# CART403 — RUO Batch Distributor (10,000 per batch)

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART403_BATCHES"
BATCH_SIZE = 10000

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART403] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    batches = [
        ruos[i:i+BATCH_SIZE]
        for i in range(0, len(ruos), BATCH_SIZE)
    ]

    for idx, b in enumerate(batches):
        with open(f"{OUTDIR}/batch_{idx}.json", "w") as f:
            json.dump(b, f, indent=4)

    print(f"[CART403] Created {len(batches)} batches → CART403_BATCHES")

if __name__ == "__main__":
    main()
