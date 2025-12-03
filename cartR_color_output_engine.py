#!/usr/bin/env python3
# [💜 CART R] C13B0 Color Output Engine — Fixed Version

import json
import os

FILES = [
    "C13B0_USER_VECTOR.json",
    "C13B0_COLOR_MAP.json",
    "C13B0_PATTERN_MAP.json",
    "C13B0_DENSITY_MAP.json",
    "C13B0_TONE_COLOR_MAP.json",
    "C13B0_BIAS_COLOR_MAP.json",
    "C13B0_SYMBIOSIS_MAP.json",
    "C13B0_DIVERGENCE_MAP.json"
]

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}

def normalize_structure(data):
    """Ensures everything becomes a dict of {term: score/color/etc}."""
    if isinstance(data, dict):
        return data
    if isinstance(data, list):
        # convert list to {"term":1} style just to keep terms
        return {str(x): 1 for x in data}
    return {}

def merge_dicts(dicts):
    final = {}
    for d in dicts:
        for k, v in d.items():
            if k not in final:
                final[k] = v
    return final

def main():
    print("[💜 CART R] Loading C13B0 maps...")

    loaded = []
    for f in FILES:
        print(f"[💜 CART R] ✓ Loaded {f}")
        loaded.append(normalize_structure(load_json(f)))

    print("[💜 CART R] Merging maps…")
    merged = merge_dicts(loaded)

    print(f"[💜 CART R] Total merged terms: {len(merged)}")

    out_path = "C13B0_COLOR_OUTPUT.json"
    with open(out_path, "w") as f:
        json.dump(merged, f, indent=2)

    print(f"[💜 CART R] Saved → {out_path}")
    print("[💜 CART R] Done.")

if __name__ == "__main__":
    main()
