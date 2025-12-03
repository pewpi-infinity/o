#!/usr/bin/env python3
# CART316 — Sci-Fi → Reality Translator Writer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
SCIFI = "CART224_SCIFI_MAP.json"
OUTDIR = "CART316_SCIFI_REALITY"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART316] RUO store missing")
    if not os.path.exists(SCIFI):
        raise FileNotFoundError("[CART316] sci-fi mapping missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(SCIFI, "r") as f: sci = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        mappings = sci.get(rh, [])

        fname = f"{OUTDIR}/{rh}.md"
        with open(fname, "w") as md:
            md.write(f"# Sci‑Fi → Reality Analysis — {rh}\n\n")

            md.write("## Sci‑Fi Concepts Detected\n")
            for m in mappings:
                md.write(f"- {m}\n")

            md.write("\n## Scientific Interpretation\n")
            md.write("The sci‑fi signals map into these scientific domains:\n")
            for m in mappings:
                md.write(f"- `{m}` → realistic interpretation pathway.\n")

            md.write("\n## Conclusion\n")
            md.write("Sci‑fi concepts serve as conceptual frameworks for deeper research.\n")

    print(f"[CART316] Sci‑Fi Reality papers → {OUTDIR}")

if __name__ == "__main__":
    main()
