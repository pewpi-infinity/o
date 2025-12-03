#!/usr/bin/env python3
import os, json, subprocess

C13 = "C13B0"

def load_json(path, default):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default

def save_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=4)

def read_termux_history():
    hist_file = os.path.expanduser("~/.bash_history")
    if not os.path.exists(hist_file):
        return []
    try:
        with open(hist_file, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
        return []

def git_recent_commits():
    try:
        out = subprocess.check_output(["git", "log", "-n", "20", "--pretty=format:%s"], stderr=subprocess.DEVNULL)
        return out.decode().split("\n")
    except:
        return []

def analyze_context(user_vec, hist, commits):
    score = {}
    for word in user_vec:
        base = word.lower()
        score[base] = score.get(base, 0)

        for line in hist:
            if base in line.lower():
                score[base] += 3

        for c in commits:
            if base in c.lower():
                score[base] += 5

    ranked = sorted(score.items(), key=lambda x: x[1], reverse=True)
    return ranked

def main():
    print("[💜 CART C] Loading C13B0 user vector…")
    uv = load_json(f"{C13}_USER_VECTOR.json", [])

    print("[💜 CART C] Reading Termux history…")
    hist = read_termux_history()

    print("[💜 CART C] Reading recent commits…")
    commits = git_recent_commits()

    print("[💜 CART C] Building cross-context pattern scores…")
    results = analyze_context(uv, hist, commits)

    print("[💜 CART C] Saving pattern map → C13B0_PATTERN_MAP.json")
    save_json(f"{C13}_PATTERN_MAP.json", results)

    print("[💜 CART C] Done.")

if __name__ == "__main__":
    main()
