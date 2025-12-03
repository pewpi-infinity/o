#!/usr/bin/env python3

import json
import os

print("[💜 CART P] Loading C13B0 maps...")

def load(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

# Load all maps created so far
vec        = load("C13B0_USER_VECTOR.json")
color      = load("C13B0_COLOR_MAP.json")
pattern    = load("C13B0_PATTERN_MAP.json")
density    = load("C13B0_DENSITY_MAP.json")
tone       = load("C13B0_TONE_COLOR_MAP.json")
bias       = load("C13B0_BIAS_COLOR_MAP.json")
symbi      = load("C13B0_SYMBIOSIS_MAP.json")
divergence = load("C13B0_DIVERGENCE_MAP.json")

# Combine everything into a unified "blueprint intelligence" surface
blueprint = {}

print("[💜 CART P] Integrating maps...")

def ensure_iterable(x):
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        return [x]
    if isinstance(x, dict):
        return list(x.keys())
    return []

all_terms = set()

for source in [vec, color, pattern, density, tone, bias, symbi, divergence]:
    all_terms.update(ensure_iterable(source))

for term in all_terms:
    blueprint[term] = {
        "color": color.get(term),
        "pattern": pattern.get(term) if isinstance(pattern, dict) else None,
        "density": density.get(term),
        "tone": tone.get(term),
        "bias": bias.get(term),
        "symbiosis": symbi.get(term),
        "divergence": divergence.get(term),
    }

with open("C13B0_BLUEPRINT.json", "w") as f:
    json.dump(blueprint, f, indent=2)

print("[💜 CART P] Saved → C13B0_BLUEPRINT.json")
print("[💜 CART P] Done.")
