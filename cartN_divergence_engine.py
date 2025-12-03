#!/usr/bin/env python3
import json, os, hashlib

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

print("[💜 CART N] Loading C13B0 maps...")

vec   = load_json("C13B0_USER_VECTOR.json")          # list
color = load_json("C13B0_COLOR_MAP.json")            # dict
bias  = load_json("C13B0_BIAS_COLOR_MAP.json")       # dict
dens  = load_json("C13B0_DENSITY_MAP.json")          # dict
symb  = load_json("C13B0_SYMBIOSIS_MAP.json")        # dict

# ---- Build safe unified term set ----
terms = set()

if isinstance(vec, list):
    terms.update(vec)

if isinstance(color, dict):
    terms.update(color.keys())

if isinstance(bias, dict):
    terms.update(bias.keys())

if isinstance(dens, dict):
    terms.update(dens.keys())

if isinstance(symb, dict):
    terms.update(symb.keys())

terms = sorted(terms)

print(f"[💜 CART N] Total unified terms: {len(terms)}")

# ---- Divergence Logic ----
divergence = {}

for t in terms:
    h = hashlib.md5(t.encode()).hexdigest()
    score = int(h[:2], 16) / 255  # 0.0 - 1.0 random-but-deterministic
    # Higher score = more divergence (new direction)
    if score > 0.66:
        divergence[t] = "red"
    else:
        divergence[t] = "blue"

# ---- Save ----
with open("C13B0_DIVERGENCE_MAP.json", "w") as f:
    json.dump(divergence, f, indent=2)

print("[💜 CART N] Saved → C13B0_DIVERGENCE_MAP.json")
print("[💜 CART N] Done.")
