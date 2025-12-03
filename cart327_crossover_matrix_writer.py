#!/usr/bin/env python3
# CART327 — Crossover Matrix Writer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART327_MATRIX"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART327] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    hashes = [r["research_hash"] for r in ruos]
    index = {h: i for i, h in enumerate(hashes)}

    # Initialize empty matrix
    size = len(hashes)
    matrix = [[0]*size for _ in range(size)]

    for r in ruos:
        row = index[r["research_hash"]]
        for c in r["crossover_links"]:
            col = index.get(c["target_hash"])
            if col is not None:
                matrix[row][col] = round(c["weight"], 3)

    # Write markdown matrix
    fname = f"{OUTDIR}/crossover_matrix.md"
    with open(fname, "w") as md:
        md.write("# Crossover Weight Matrix\n\n")
        md.write("| RUO | " + " | ".join(hashes) + " |\n")
        md.write("|" + "---|" * (len(hashes)+1) + "\n")

        for i, h in enumerate(hashes):
            row = " | ".join(str(matrix[i][j]) for j in range(size))
            md.write(f"| {h} | {row} |\n")

    print("[CART327] Crossover matrix → CART327_MATRIX")

if __name__ == "__main__":
    main()
