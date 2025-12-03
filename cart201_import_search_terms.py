#!/usr/bin/env python3
# CART201 — Import 250 Search Terms
# Loads and validates raw search terms → outputs JSON

import json
import os

INPUT_FILE = "search_terms_250.txt"
OUTPUT_FILE = "CART201_SEARCH_TERMS.json"

def load_terms(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"[CART201] Missing {path}")

    with open(path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    # Remove duplicates, normalize, sort
    terms = sorted(list(set([t.lower() for t in lines])))

    if len(terms) < 200:
        print("[CART201] WARNING: Less than expected terms.")

    return terms

def main():
    terms = load_terms(INPUT_FILE)

    out = {
        "total_terms": len(terms),
        "terms": terms
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(out, f, indent=4)

    print(f"[CART201] Loaded {len(terms)} terms → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
