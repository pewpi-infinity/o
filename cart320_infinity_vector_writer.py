#!/usr/bin/env python3
# CART320 — Infinity Vector‑Driven Writer
# Creates research papers whose structure depends on the Infinity Seed vector.

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
SEED = "CART229_INFINITY_SEED.json"
OUTDIR = "CART320_VECTOR_WRITING"

def tone_from_value(v):
    if v > 0.66: return "Highly technical, formal reasoning."
    if v > 0.33: return "Balanced technical + intuitive reasoning."
    return "Simplified intuitive reasoning."

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART320] RUO store missing")
    if not os.path.exists(SEED):
        raise FileNotFoundError("[CART320] Infinity seed missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(SEED, "r") as f: seed = json.load(f)

    vec = seed["vector_seed"]
    style_index = sum(vec[:10]) / 10  # Leading vector average decides tone

    tone = tone_from_value(style_index)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]

        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Infinity-Vector Crafted Document — {rh}\n\n")

            md.write("## Tone Profile\n")
            md.write(f"{tone}\n\n")

            md.write("## Terms\n")
            for t in r["terms"]:
                md.write(f"- {t}\n")

            md.write("\n## Reasoning\n")
            md.write("Reasoning derived from Infinity-Vector tonal bias.\n")

    print(f"[CART320] Vector-driven papers → {OUTDIR}")

if __name__ == "__main__":
    main()
