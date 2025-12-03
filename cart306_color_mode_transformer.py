#!/usr/bin/env python3
# CART306 — Color Mode Transformer
# Generates RUO research papers in specific OS color modes.

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART306_COLOR_MODE"

MODES = {
    "green": "Engineering Focus — step-by-step, mechanisms, constraints.",
    "red": "Routing & Expansion — new directions, pathways.",
    "blue": "Input Expansion — where to add new data and why.",
    "pink": "Investigation — questions, anomalies, weaknesses.",
    "orange": "CEO Summary — strategy, impact, business vision.",
    "purple": "Assimilation — integrate into the broader knowledge system.",
    "yellow": "Data Acquisition — where to get more data + why it matters."
}

def write_mode(md, ruo, mode_name):
    md.write(f"## Mode: {mode_name.upper()}\n")
    md.write(f"{MODES[mode_name]}\n\n")
    md.write("### Terms\n")
    for t in ruo["terms"]:
        md.write(f"- {t}\n")
    md.write("\n### Crossover Highlights\n")
    for c in ruo["crossover_links"]:
        md.write(f"- `{c['target_hash']}` → {c['reason']} (W:{c['weight']})\n")
    md.write("\n---\n\n")

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART306] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Color-Mode Research Paper — {rh}\n\n")
            for mode in MODES:
                write_mode(md, r, mode)

    print(f"[CART306] Color mode papers written → {OUTDIR}")

if __name__ == "__main__":
    main()
