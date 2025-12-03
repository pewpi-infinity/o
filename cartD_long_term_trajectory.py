#!/usr/bin/env python3

import json, os, time

VEC_FILE = "C13B0_USER_VECTOR.json"
PAT_FILE = "C13B0_PATTERN_MAP.json"
OUT_FILE = "C13B0_TRAJECTORY_MAP.json"

print("[💜 CART D] Loading vectors...")

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}

user_vec = load_json(VEC_FILE)
pattern_map = load_json(PAT_FILE)

print("[💜 CART D] Building 30-day trend scores...")

trajectory = {}
timestamp = time.time()

for term in user_vec:
    freq = user_vec.get(term, 0)
    pat  = pattern_map.get(term, 0)

    score = (freq * 0.6) + (pat * 0.4)
    trajectory[term] = {
        "trend_score": score,
        "timestamp": timestamp
    }

with open(OUT_FILE, "w") as f:
    json.dump(trajectory, f, indent=2)

print("[💜 CART D] Saved →", OUT_FILE)
print("[💜 CART D] Done.")
