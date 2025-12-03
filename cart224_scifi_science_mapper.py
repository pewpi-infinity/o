#!/usr/bin/env python3

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTPUT = "CART224_SCIFI_MAP.json"

SCIFI_MAP = {
    "tricorder": ["biosensors", "spectrometry", "telemetry"],
    "warp": ["relativity", "spacetime_metrics"],
    "transporter": ["quantum_teleportation", "entanglement"],
    "photon": ["quantum_electrodynamics"],
    "shield": ["magnetosphere", "field_containment"],
    "fusion": ["tokamak_reactors"],
    "ai": ["neural_nets", "computability"]
}

def map_scifi(terms):
    out = []
    for t in terms:
        if t in SCIFI_MAP:
            out.extend(SCIFI_MAP[t])
    return list(set(out))

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART224] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    out = {}

    for r in ruos:
        out[r["research_hash"]] = map_scifi(r["terms"])

    with open(OUTPUT, "w") as f:
        json.dump(out, f, indent=4)

    print(f"[CART224] Sci‑Fi → Science mappings saved → {OUTPUT}")

if __name__ == "__main__":
    main()
