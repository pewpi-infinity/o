#!/usr/bin/env python3
# 💜 CART M — C13B0 anomaly detector

import json, os, itertools

def load(f):
    return json.load(open(f)) if os.path.exists(f) else {}

# Load previous maps
color_map   = load("C13B0_COLOR_MAP.json")
bias_map    = load("C13B0_BIAS_COLOR_MAP.json")
pattern_map = load("C13B0_PATTERN_MAP.json")
tone_map    = load("C13B0_TONE_COLOR_MAP.json")
symb_map    = load("C13B0_SYMBIOSIS_MAP.json")
density_map = load("C13B0_DENSITY_MAP.json")

# Build the master term list
terms = sorted(set(
    list(color_map.keys()) +
    list(bias_map.keys()) +
    list(pattern_map.keys()) +
    list(tone_map.keys()) +
    list(symb_map.keys()) +
    list(density_map.keys())
))

anomalies = {}

def detect_anomaly(term):
    """Term gets pink if something in its maps is unusual."""
    reasons = []

    # 1. Bias score unusually high
    if term in bias_map and isinstance(bias_map[term], (int, float)) and bias_map[term] > 3:
        reasons.append("high bias weighting")

    # 2. Pattern divergence
    if term in pattern_map and isinstance(pattern_map[term], (int, float)) and pattern_map[term] < 0.1:
        reasons.append("pattern divergence")

    # 3. Density spikes
    if term in density_map and isinstance(density_map[term], (int, float)) and density_map[term] > 2:
        reasons.append("density anomaly")

    # 4. Symbiosis mismatch
    if term in symb_map and symb_map[term] == "low":
        reasons.append("low AI-symbiosis")

    return reasons

for t in terms:
    r = detect_anomaly(t)
    if r:
        anomalies[t] = {
            "color": "pink",
            "reason": r
        }

# Save anomaly map
with open("C13B0_ANOMALY_MAP.json", "w") as f:
    json.dump(anomalies, f, indent=2)

print("[💜 CART M] Anomaly detector complete.")
print(f"[💜 CART M] Total anomalies: {len(anomalies)}")
print("[💜 CART M] Saved → C13B0_ANOMALY_MAP.json")
