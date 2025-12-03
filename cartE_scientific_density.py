#!/usr/bin/env python3
# 💜 CART E — Scientific Density Indexer (C13B0)

import json
import os

# Load vectors safely
def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}

user_vector = load_json("C13B0_USER_VECTOR.json")
color_map   = load_json("C13B0_COLOR_MAP.json")


# Density rulebook
PHYSICS_TERMS = {
    "quantum", "photon", "wave", "spin", "quark", "hydrogen",
    "resonance", "lattice", "frequency", "oscillation"
}

CHEMISTRY_TERMS = {
    "oxidation", "bond", "enthalpy", "entropy", "isotope",
    "plasma", "ion", "catalyst"
}

ENGINEERING_TERMS = {
    "semiconductor", "graphene", "conductivity", "bandgap",
    "superconductor", "device", "circuit"
}

DISCOVERY_TERMS = {
    "tachyon", "wormhole", "singularity", "maser",
    "rydberg", "casimir"
}

# Density → Color logic
def density_to_color(term):
    t = term.lower()

    if t in PHYSICS_TERMS:
        return "blue"

    if t in CHEMISTRY_TERMS:
        return "yellow"

    if t in ENGINEERING_TERMS:
        return "orange"

    if t in DISCOVERY_TERMS:
        return "red"

    return "green"


density_map = {}

for term in user_vector:
    density_map[term] = density_to_color(term)


# Save it
outpath = "C13B0_DENSITY_MAP.json"
with open(outpath, "w") as f:
    json.dump(density_map, f, indent=2)

print("[💜 CART E] Scientific density map built.")
print(f"[💜 CART E] Saved → {outpath}")
