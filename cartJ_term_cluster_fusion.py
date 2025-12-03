#!/usr/bin/env python3
import json, itertools, os

print("[💜 CART J] Loading C13B0 maps...")

def load_json(path):
    if os.path.exists(path):
        with open(path,'r') as f:
            return json.load(f)
    return {}

# Load previous outputs
color_map = load_json("C13B0_BIAS_COLOR_MAP.json")
tone_map  = load_json("C13B0_TONE_COLOR_MAP.json")
density   = load_json("C13B0_DENSITY_MAP.json")
user_vec  = load_json("C13B0_USER_VECTOR.json")

# Combine all known terms
all_terms = list(set(
    list(color_map.keys()) +
    list(tone_map.keys()) +
    list(user_vec)
))

print(f"[💜 CART J] Total terms detected: {len(all_terms)}")

if len(all_terms) < 5:
    print("[💜 CART J] Not enough terms for 4–5 term fusion. Exiting.")
    exit(0)

# Color blending logic
def blend_colors(colors):
    # simple blend: count frequencies
    score = {}
    for c in colors:
        score[c] = score.get(c,0) + 1
    # return dominant
    return max(score, key=score.get)

clusters = {}

print("[💜 CART J] Generating 4-term clusters...")
for combo in itertools.combinations(all_terms,4):
    colors = []
    for t in combo:
        c = color_map.get(t) or tone_map.get(t)
        if c: colors.append(c)
    if colors:
        clusters["+".join(combo)] = blend_colors(colors)

print("[💜 CART J] Generating 5-term clusters...")
for combo in itertools.combinations(all_terms,5):
    colors = []
    for t in combo:
        c = color_map.get(t) or tone_map.get(t)
        if c: colors.append(c)
    if colors:
        clusters["+".join(combo)] = blend_colors(colors)

outfile = "C13B0_CLUSTER_FUSION.json"
with open(outfile,"w") as f:
    json.dump(clusters,f,indent=2)

print(f"[💜 CART J] Saved → {outfile}")
print("[💜 CART J] Done.")
