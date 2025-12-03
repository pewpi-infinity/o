#!/usr/bin/env python3
import json, os

print("[💜 CART S] Normalizing C13B0 maps...")

def load(name):
    if not os.path.exists(name): return {}
    try:
        with open(name) as f:
            data = json.load(f)
            return data
    except:
        return {}

def normalize(obj):
    # Convert lists → indexed dicts
    if isinstance(obj, list):
        return {str(i): v for i, v in enumerate(obj)}
    # Convert nested lists → flatten into dict
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            if isinstance(v, list):
                for idx, item in enumerate(v):
                    cleaned[f"{k}_{idx}"] = item
            else:
                cleaned[k] = v
        return cleaned
    return {}

maps = [
    "C13B0_USER_VECTOR.json",
    "C13B0_COLOR_MAP.json",
    "C13B0_PATTERN_MAP.json",
    "C13B0_DENSITY_MAP.json",
    "C13B0_TONE_COLOR_MAP.json",
    "C13B0_BIAS_COLOR_MAP.json",
    "C13B0_SYMBIOSIS_MAP.json",
    "C13B0_DIVERGENCE_MAP.json",
    "C13B0_CLUSTER_FUSION.json"
]

for m in maps:
    if os.path.exists(m):
        data = load(m)
        data = normalize(data)
        with open(m, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[💜 CART S] Normalized → {m}")

print("[💜 CART S] Done. All maps now dict-safe.")
