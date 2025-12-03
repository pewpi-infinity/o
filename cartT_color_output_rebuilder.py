#!/usr/bin/env python3
import json, os

print("[💜 CART T] Loading C13B0 maps...")

def load(path):
    with open(path, "r") as f:
        return json.load(f)

# Load only maps that exist
maps = {}
for fname in [
    "C13B0_USER_VECTOR.json",
    "C13B0_COLOR_MAP.json",
    "C13B0_PATTERN_MAP.json",
    "C13B0_DENSITY_MAP.json",
    "C13B0_TONE_COLOR_MAP.json",
    "C13B0_BIAS_COLOR_MAP.json",
    "C13B0_SYMBIOSIS_MAP.json",
    "C13B0_DIVERGENCE_MAP.json"
]:
    if os.path.exists(fname):
        print(f"[💜 CART T] ✓ Loaded {fname}")
        maps[fname] = load(fname)

# Flatten all terms safely
all_terms = set()

def collect(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            all_terms.add(str(k))
            collect(v)
    elif isinstance(obj, list):
        for item in obj:
            collect(item)
    elif isinstance(obj, str):
        all_terms.add(obj)

print("[💜 CART T] Flattening terms…")
for m in maps.values():
    collect(m)

all_terms = sorted(all_terms)

print("[💜 CART T] Total flattened terms:", len(all_terms))

# Rebuild unified color output structure
unified = {}
for term in all_terms:
    unified[term] = {
        "base_color": maps.get("C13B0_COLOR_MAP.json", {}).get(term, "none"),
        "tone_color": maps.get("C13B0_TONE_COLOR_MAP.json", {}).get(term, "none"),
        "bias_color": maps.get("C13B0_BIAS_COLOR_MAP.json", {}).get(term, "none"),
        "symbiosis": maps.get("C13B0_SYMBIOSIS_MAP.json", {}).get(term, 0),
        "density": maps.get("C13B0_DENSITY_MAP.json", {}).get(term, 0),
        "pattern": maps.get("C13B0_PATTERN_MAP.json", {}).get(term, 0),
        "divergence": maps.get("C13B0_DIVERGENCE_MAP.json", {}).get(term, 0)
    }

with open("C13B0_COLOR_OUTPUT.json", "w") as f:
    json.dump(unified, f, indent=2)

print("[💜 CART T] Saved → C13B0_COLOR_OUTPUT.json")
