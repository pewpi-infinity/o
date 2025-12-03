#!/usr/bin/env python3
import json, os, re

def load(path, default):
    try:
        with open(path,'r') as f:
            return json.load(f)
    except:
        return default

def detect_tone():
    """Reads recent history + repo + system messages and scores tone."""
    tone_score = 0

    # Termux history
    hist = os.popen("history | tail -n 200").read().lower()
    if "hydrogen" in hist: tone_score += 4
    if "ai" in hist: tone_score += 4
    if "fusion" in hist: tone_score += 3
    if "anger" in hist or "f***" in hist: tone_score += 6
    if "research" in hist: tone_score += 3

    # Git commit messages
    commits = os.popen("git log --pretty=%B -n 10").read().lower()
    if "fix" in commits: tone_score += 2
    if "research" in commits: tone_score += 4
    if "token" in commits: tone_score += 3

    return tone_score

def tone_to_color(score):
    """
    Converts tone score → AI color:
    Purple: symbiosis, alignment
    Red: new direction discovered
    Yellow: data-heavy mode
    Orange: engineer-building mode
    Pink: investigate anomalies
    Blue: calm analysis
    """
    if score >= 18:
        return "red"
    if score >= 14:
        return "pink"
    if score >= 10:
        return "purple"
    if score >= 7:
        return "orange"
    if score >= 4:
        return "yellow"
    return "blue"

def apply_color_map(base_map, tone_color):
    updated = {}
    for term, color in base_map.items():
        # keep original color but blend tone influence
        if tone_color == "purple":
            updated[term] = "purple"
        elif tone_color == "red":
            updated[term] = "red"
        elif tone_color == "pink":
            updated[term] = "pink"
        elif tone_color == "orange":
            updated[term] = "orange"
        elif tone_color == "yellow":
            updated[term] = "yellow"
        else:
            updated[term] = "blue"
    return updated

def main():
    print("[💜 CART F] Loading color map...")
    base_color_map = load("C13B0_COLOR_MAP.json", {})

    print("[💜 CART F] Detecting emotional tone...")
    score = detect_tone()
    tone_color = tone_to_color(score)
    print(f"[💜 CART F] Tone score: {score} → {tone_color}")

    print("[💜 CART F] Updating colors with tone modulation...")
    final_map = apply_color_map(base_color_map, tone_color)

    with open("C13B0_TONE_COLOR_MAP.json","w") as f:
        json.dump(final_map,f,indent=2)

    print("[💜 CART F] Saved → C13B0_TONE_COLOR_MAP.json")
    print("[💜 CART F] Done.")

if __name__ == "__main__":
    main()
