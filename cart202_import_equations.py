#!/usr/bin/env python3
# CART202 — Import 250 Equations
# Parses equations → LaTeX-standard tokens → JSON output

import json
import os
import re

INPUT_FILE = "equations_250.txt"
OUTPUT_FILE = "CART202_EQUATIONS.json"

def normalize_equation(eq):
    # Remove spaces, ensure LaTeX compatibility
    eq = eq.strip()
    eq = eq.replace(" ", "")
    eq = eq.replace("^", "^{") + "}" if "^" in eq else eq
    return eq

def tokenize(eq):
    # Basic mathematical tokenization
    tokens = re.findall(r"[A-Za-z]+|[0-9]+|[\+\-\*\/\=\^\(\)]", eq)
    return tokens

def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"[CART202] Missing {INPUT_FILE}")

    with open(INPUT_FILE, "r") as f:
        equations = [l.strip() for l in f.readlines() if l.strip()]

    output = {}
    for eq in equations:
        clean = normalize_equation(eq)
        output[eq] = {
            "normalized": clean,
            "tokens": tokenize(clean)
        }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=4)

    print(f"[CART202] Processed {len(output)} equations → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
