#!/usr/bin/env python3
import json, itertools, os

# Utility to load JSON safely
def load_json(path, default=None):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default if default is not None else {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

print("[💜 CART I] Loading maps…")

user_vec      = load_json("C13B0_USER_VECTOR.json", [])
color_map     = load_json("C13B0_COLOR_MAP.json", {})
density_map   = load_json("C13B0_DENSITY_MAP.json", {})
bias_map      = load_json("C13B0_BIAS_COLOR_MAP.json", {})

# Turn everything into a single weighted color lookup
print("[💜 CART I] Building unified color baseline…")
unified = {}

for term in user_vec:
    unified[term] = (
        bias_map.get(term)
        or density_map.get(term)
        or color_map.get(term)
        or "blue"
    )

terms = list(unified.keys())

if len(terms) < 3:
    print("[💜 CART I] Not enough terms for trio fusion. Exiting.")
    exit()

print(f"[💜 CART I] {len(terms)} terms loaded.")
print("[💜 CART I] Generating 3-term fusion clusters…")

fusion_map = {}

def fuse_colors(c1, c2, c3):
    palette = [c1, c2, c3]
    if "purple" in palette: return "purple"
    if "red" in palette:    return "red"
    if "orange" in palette: return "orange"
    if "yellow" in palette: return "yellow"
    if "pink" in palette:   return "pink"
    if "green" in palette:  return "green"
    return "blue"

count = 0
for t1, t2, t3 in itertools.combinations(terms, 3):
    c1 = unified.get(t1, "blue")
    c2 = unified.get(t2, "blue")
    c3 = unified.get(t3, "blue")

    fused = fuse_colors(c1, c2, c3)
    fusion_map[f"{t1}|{t2}|{t3}"] = fused
    count += 1

print(f"[💜 CART I] Built {count} trio-fusion entries.")

save_json("C13B0_TRIO_FUSION_MAP.json", fusion_map)

print("[💜 CART I] Saved → C13B0_TRIO_FUSION_MAP.json")
print("[💜 CART I] Done.")
