#!/usr/bin/env python3
# CART812 — Conversate Token Writer Engine
# Turns user input into a token-structured research document.

import json, os, time, random

INPUT = "CART806_INPUT.txt"
OUT = "CART812_CONVERSATE_DRAFT.json"
RUO = "CART217_RUO_STORE.json"
EVO = "CART601_EVOLVED_TERMS.json"

def load(p,d):
    return json.load(open(p)) if os.path.exists(p) else d

def main():
    if not os.path.exists(INPUT):
        print("[CART812] No input.")
        return

    with open(INPUT,"r") as f:
        prompt = f.read().strip()

    ruos = load(RUO, [])
    evo = load(EVO, {"history":[]})

    terms = evo["history"][-1]["evolved_terms"] if evo["history"] else []

    # basic outline generation
    outline = [
        f"Research Topic: {prompt}",
        "1. Context",
        "2. Related Concepts",
        "3. Data Points",
        "4. Interpretation",
        "5. Conclusion"
    ]

    bullets = [
        f"- Key idea: {prompt}",
        f"- Related evolved term: {random.choice(terms) if terms else 'none'}",
        f"- Supporting RUO: {random.choice(ruos)['terms'][:2] if ruos else []}"
    ]

    paper = f"""
Title: {prompt}

Abstract:
This document explores the topic '{prompt}' using Infinity-OS logic,
crossovers, evolved term sets, and RUO relationships.

Body:
- {bullets[0]}
- {bullets[1]}
- {bullets[2]}

Conclusion:
This token represents an indexed research artifact derived from the user's
query and system logic.
"""

    draft = {
        "prompt": prompt,
        "outline": outline,
        "bullets": bullets,
        "paper": paper,
        "timestamp": int(time.time())
    }

    with open(OUT,"w") as f:
        json.dump(draft,f,indent=4)

    print("[CART812] Conversate draft built.")

if __name__ == "__main__":
    main()
