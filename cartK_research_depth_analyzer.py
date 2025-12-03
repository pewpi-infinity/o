#!/usr/bin/env python3
# 💜 CART K — C13B0 Research Depth Analyzer

import json, os, math

def load(path):
    if os.path.exists(path):
        with open(path, 'r') as f: return json.load(f)
    return {}

# Load all prior maps
vec   = load("C13B0_USER_VECTOR.json")
color = load("C13B0_COLOR_MAP.json")
pat   = load("C13B0_PATTERN_MAP.json")
tone  = load("C13B0_TONE_COLOR_MAP.json")
bias  = load("C13B0_BIAS_COLOR_MAP.json")
dens  = load("C13B0_DENSITY_MAP.json")

terms = sorted(set(vec + list(color.keys()) + list(bias.keys())))

depth_map = {}

def score(term):
    s = 0
    if term in color: s += 1
    if term in bias:  s += 2
    if term in tone:  s += 1
    if term in dens:  s += dens.get(term, 0)
    if term in pat:   s += pat.get(term, 0)
    return s

for term in terms:
    depth_map[term] = score(term)

with open("C13B0_DEPTH_MAP.json", "w") as f:
    json.dump(depth_map, f, indent=2)

print("[💜 CART K] Depth map built.")
print("[💜 CART K] Saved → C13B0_DEPTH_MAP.json")
