#!/usr/bin/env python3
# 💜 CART H — C13B0 Term-Pair Intelligence Builder

import json
import itertools
import os

# --- Helpers ---------------------------------------------------------
def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# --- Load required maps ----------------------------------------------
print("[💜 CART H] Loading maps…")
color_map      = load_json("C13B0_BIAS_COLOR_MAP.json")      # hydrogen + periodic bias applied
density_map    = load_json("C13B0_DENSITY_MAP.json")         # scientific density
pattern_vector = load_json("C13B0_USER_VECTOR.json")         # original harvested vector

print("[💜 CART H] Maps loaded.")

# --- Extract base terms -----------------------------------------------
terms = list(pattern_vector)

if len(terms) < 2:
    print("[💜 CART H] Not enough terms for fusion.")
    exit(0)

# --- Build term pairs -------------------------------------------------
print("[💜 CART H] Building 2-term combinations…")
pairs = list(itertools.combinations(terms, 2))

fusion_results = {}

for a, b in pairs:
    cA = color_map.get(a, "yellow")
    cB = color_map.get(b, "yellow")

    # Fusion color logic:
    # purple dominates → assimilation
    # blue mixes with purple → deep research
    # red overrides on divergence
    # green remains a tool modifier
    fusion_color = None

    if "purple" in (cA, cB):
        fusion_color = "purple"
    elif "red" in (cA, cB):
        fusion_color = "red"
    elif "blue" in (cA, cB):
        fusion_color = "blue"
    elif "yellow" in (cA, cB):
        fusion_color = "yellow"
    else:
        fusion_color = cA  # fallback

    densityA = density_map.get(a, 1)
    densityB = density_map.get(b, 1)
    density_score = (densityA + densityB) / 2

    fusion_results[f"{a}+{b}"] = {
        "colorA": cA,
        "colorB": cB,
        "fusion_color": fusion_color,
        "density_score": density_score,
    }

# --- Save output ------------------------------------------------------
save_json("C13B0_PAIR_FUSION.json", fusion_results)
print("[💜 CART H] Saved → C13B0_PAIR_FUSION.json")
print("[💜 CART H] Done.")
