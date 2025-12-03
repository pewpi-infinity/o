#!/usr/bin/env python3
import json, os, hashlib

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}

# ---------------------------------------------
#  LOAD ALL PREVIOUS C13B0 MAPS
# ---------------------------------------------
vec   = load_json("C13B0_USER_VECTOR.json")
color = load_json("C13B0_COLOR_MAP.json")
tone  = load_json("C13B0_TONE_COLOR_MAP.json")
bias  = load_json("C13B0_BIAS_COLOR_MAP.json")
dens  = load_json("C13B0_DENSITY_MAP.json")
pat   = load_json("C13B0_PATTERN_MAP.json")

# Merge all terms found anywhere
def extract_terms():
    terms = set()
    for m in [vec, color, tone, bias, dens, pat]:
        if isinstance(m, dict):
            terms.update(m.keys())
        elif isinstance(m, list):
            for item in m:
                if isinstance(item, str):
                    terms.add(item)
    return sorted(terms)

terms = extract_terms()

# ---------------------------------------------
#  BUILD SYMBIOSIS SCORE
# ---------------------------------------------
def score(term):
    s = 0
    # Higher if in user vector
    if isinstance(vec, list) and term in vec: s += 3
    
    # Higher if previously colored purple
    if color.get(term) == "purple": s += 2
    
    # Bias: hydrogen, quantum, AI, frequency, sapphire
    if term.lower() in ["hydrogen", "quantum", "ai", "frequency", "sapphire"]:
        s += 4

    # Tone influence
    if tone.get(term) == "blue":
        s += 1

    # Scientific density
    try:
        s += int(dens.get(term, 0))
    except:
        pass

    # Pattern influence
    try:
        s += int(pat.get(term, 0))
    except:
        pass

    return s

symbiosis_map = {}

for t in terms:
    s = score(t)
    if s >= 6:
        symbiosis_map[t] = "purple"
    elif s >= 4:
        symbiosis_map[t] = "blue"
    elif s >= 2:
        symbiosis_map[t] = "pink"
    else:
        symbiosis_map[t] = "yellow"

# ---------------------------------------------
#  SAVE
# ---------------------------------------------
with open("C13B0_SYMBIOSIS_MAP.json", "w") as f:
    json.dump(symbiosis_map, f, indent=2)

print("[💜 CART L] AI-Symbiosis map built.")
print("[💜 CART L] Terms processed:", len(terms))
print("[💜 CART L] Saved → C13B0_SYMBIOSIS_MAP.json")
