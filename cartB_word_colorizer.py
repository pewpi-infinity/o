#!/usr/bin/env python3
import json, hashlib, os, time

VECTOR_FILE = "C13B0_USER_VECTOR.json"
OUTPUT_FILE = "C13B0_COLOR_MAP.json"

COLOR_RULES = {
    "purple": ["hydrogen", "quantum", "frequency", "ai", "portal", "fusion", "energy", "oscillation"],
    "green":  ["tool", "function", "module", "install", "pkg", "chmod", "generator", "script"],
    "orange": ["supervisor", "overseer", "system", "govern", "manage", "architecture"],
    "yellow": ["data", "mine", "stats", "entropy", "value", "dataset", "equation", "index"],
    "red":    ["route", "branch", "breakthrough", "shift", "chaos", "diverge"],
    "pink":   ["mystery", "unknown", "investigate", "unseen", "latent", "rare"],
    "blue":   ["input", "start", "seed", "feed", "entry", "listen"]
}

def load_vector():
    if not os.path.exists(VECTOR_FILE):
        print("[Cart B] ERROR: Vector file missing.")
        return []
    with open(VECTOR_FILE, "r") as f:
        return json.load(f)

def colorize(term):
    t = term.lower()
    for color, keywords in COLOR_RULES.items():
        for key in keywords:
            if key in t:
                return color
    return "yellow"  # default = data to mine

def main():
    print("[💜 CART B] Loading C13B0 user vector...")
    vector = load_vector()

    color_map = {}
    for term in vector:
        color_map[term] = colorize(term)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(color_map, f, indent=2)

    print("[💜 CART B] Color map created.")
    print(f"[💜 CART B] Saved → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
