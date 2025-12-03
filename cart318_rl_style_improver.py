#!/usr/bin/env python3
# CART318 — RL-Style Improvement Engine
# Takes Markdown output from any CART3xx module and improves clarity/style.

import os

INPUT_DIR = "CART301_SUMMARIES"
OUTDIR = "CART318_IMPROVED"

def improve(line):
    # Simple rule-based enhancement placeholder
    if "##" in line and "Conclusion" in line:
        return line + "\nThis section synthesizes above information.\n"
    return line

def main():
    if not os.path.exists(INPUT_DIR):
        raise FileNotFoundError("[CART318] Input summaries missing")

    os.makedirs(OUTDIR, exist_ok=True)

    for fname in os.listdir(INPUT_DIR):
        if not fname.endswith(".md"):
            continue

        with open(f"{INPUT_DIR}/{fname}", "r") as f:
            lines = f.readlines()

        improved = [improve(l) for l in lines]

        with open(f"{OUTDIR}/{fname}", "w") as f:
            f.writelines(improved)

    print(f"[CART318] Improved papers written → {OUTDIR}")

if __name__ == "__main__":
    main()
