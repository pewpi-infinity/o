#!/usr/bin/env python3

import json
import os

EQ_INPUT = "CART202_EQUATIONS.json"
OUTPUT = "CART225_EQ_DOMAIN_MAP.json"

DOMAIN_MAP = {
    "E=mc^2": "relativity",
    "F=ma": "mechanics",
    "V=IR": "electricity",
    "pV=nRT": "thermodynamics",
    "A=πr^2": "geometry",
    "V=4/3πr^3": "geometry",
    "∇·E=ρ/ε0": "electromagnetism",
    "ψ": "quantum_mechanics"
}

def domain_of(eq):
    for k, v in DOMAIN_MAP.items():
        if k.replace(" ", "") in eq.replace(" ", ""):
            return v
    return "unknown"

def main():
    if not os.path.exists(EQ_INPUT):
        raise FileNotFoundError("[CART225] Equation file missing")

    with open(EQ_INPUT, "r") as f:
        eqs = json.load(f)

    out = {}
    for original, details in eqs.items():
        domain = domain_of(original)
        out[original] = {
            "domain": domain,
            "tokens": details["tokens"]
        }

    with open(OUTPUT, "w") as f:
        json.dump(out, f, indent=4)

    print(f"[CART225] Equation domains saved → {OUTPUT}")

if __name__ == "__main__":
    main()
