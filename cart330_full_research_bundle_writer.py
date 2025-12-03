#!/usr/bin/env python3
# CART330 — Full Research Bundle Writer
# Creates a complete bundle folder per RUO.

import json, os, shutil

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART330_BUNDLES"

def safe_copy(src_folder, rh, out):
    if not os.path.exists(src_folder):
        return
    for f in os.listdir(src_folder):
        if f.startswith(rh) and f.endswith(".md"):
            shutil.copy(f"{src_folder}/{f}", out)

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART330] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    STAGES = [
        "CART301_SUMMARIES",
        "CART302_THREADS",
        "CART303_WEAVES",
        "CART304_SHORT_PAPERS",
        "CART305_LONG_PAPERS",
        "CART306_COLOR_MODE",
        "CART307_CROSSOVER_EXPANSIONS",
        "CART308_GRAPH_ANALYSIS.md",
        "CART309_SYNTHESIS",
        "CART310_JUSTIFICATIONS",
        "CART311_EVIDENCE_PAPERS",
        "CART312_NARRATIVE",
        "CART313_HISTORICAL",
        "CART314_MATERIAL",
        "CART315_GEOMETRY",
        "CART316_SCIFI_REALITY",
        "CART317_DOMAIN_BRIDGES",
        "CART318_IMPROVED",
        "CART319_MULTIPERSPECTIVE",
        "CART320_VECTOR_WRITING"
    ]

    for r in ruos:
        rh = r["research_hash"]
        bundle_path = f"{OUTDIR}/{rh}"
        os.makedirs(bundle_path, exist_ok=True)

        for st in STAGES:
            if os.path.isdir(st):
                safe_copy(st, rh, bundle_path)
            elif os.path.isfile(st):  
                # The single-file outputs like graph analysis
                shutil.copy(st, bundle_path)

    print("[CART330] Full RUO bundles → CART330_BUNDLES")

if __name__ == "__main__":
    main()
