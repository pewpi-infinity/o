#!/usr/bin/env python3
# CART412 — Copy Masterhash layers into the Grand Structure

import os, json, shutil

MASTERHASH_DIR = "CART402_GROWTH"
OUTDIR = "CART410_ZIPSTRUCT"

def main():
    if not os.path.exists(MASTERHASH_DIR):
        raise FileNotFoundError("[CART412] Missing masterhash dir")
    if not os.path.exists(OUTDIR):
        raise FileNotFoundError("[CART412] Missing ZIPSTRUCT")

    for fh in os.listdir(MASTERHASH_DIR):
        if not fh.endswith(".json"):
            continue

        fp = f"{MASTERHASH_DIR}/{fh}"

        with open(fp, "r") as f:
            mh = json.load(f)

        ruo = mh["ruo"]

        # research
        with open(f"{OUTDIR}/research/{ruo}.json", "w") as f:
            json.dump({"research_hash": mh["research_hash"]}, f, indent=4)

        # links
        with open(f"{OUTDIR}/links/{ruo}.json", "w") as f:
            json.dump({"links_hash": mh["links_hash"]}, f, indent=4)

        # combined
        with open(f"{OUTDIR}/research_plus_links/{ruo}.json", "w") as f:
            json.dump({"combined_hash": mh["combined_hash"]}, f, indent=4)

        # crossover
        with open(f"{OUTDIR}/crossover/{ruo}.json", "w") as f:
            json.dump({"crossover_growth": mh.get("crossover_growth", [])}, f, indent=4)

    print("[CART412] Copied all masterhash layers → CART410_ZIPSTRUCT")

if __name__ == "__main__":
    main()
