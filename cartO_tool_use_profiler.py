#!/usr/bin/env python3
import json, os

print("[💜 CART O] Loading C13B0 maps...")

def load(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

# Load what we have so far
user_vec     = load("C13B0_USER_VECTOR.json")
color_map    = load("C13B0_COLOR_MAP.json")
pattern_map  = load("C13B0_PATTERN_MAP.json")
bias_map     = load("C13B0_BIAS_COLOR_MAP.json")
density_map  = load("C13B0_DENSITY_MAP.json")
tone_map     = load("C13B0_TONE_COLOR_MAP.json")
sym_map      = load("C13B0_SYMBIOSIS_MAP.json")
div_map      = load("C13B0_DIVERGENCE_MAP.json")

# Unify all terms safely without type errors
def extract_terms(src):
    if isinstance(src, dict):
        return list(src.keys())
    if isinstance(src, list):
        return src
    return []

terms = set()
for src in [user_vec, color_map, pattern_map, bias_map, density_map, tone_map, sym_map, div_map]:
    terms.update(extract_terms(src))

terms = sorted(terms)
print(f"[💜 CART O] Total unified terms: {len(terms)}")

# Tool-Use keywords (GREEN)
tool_keywords = [
    "script", "module", "engine", "tool", "system", "ai", "os",
    "chmod", "python", "run", "generate", "repo", "commit",
    "termux", "scraper", "zip", "token", "build", "push",
    "hash", "parse", "logic", "analyzer", "harvester"
]

tool_use_map = {}

for t in terms:
    score = 0
    for kw in tool_keywords:
        if kw in t.lower():
            score += 1
    if score > 0:
        tool_use_map[t] = "green"
    else:
        tool_use_map[t] = "none"

with open("C13B0_TOOLUSE_MAP.json", "w") as f:
    json.dump(tool_use_map, f, indent=2)

print("[💜 CART O] Saved → C13B0_TOOLUSE_MAP.json")
print("[💜 CART O] Done.")
