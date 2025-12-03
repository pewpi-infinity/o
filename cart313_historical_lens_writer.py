#!/usr/bin/env python3
# CART313 — Historical Lens Writer

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
HISTORY = "CART221_HISTORICAL_CONTEXT.json"
OUTDIR = "CART313_HISTORICAL"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART313] RUO store missing")
    if not os.path.exists(HISTORY):
        raise FileNotFoundError("[CART313] historical context missing")

    with open(RUO_STORE, "r") as f: ruos = json.load(f)
    with open(HISTORY, "r") as f: hist = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        tags = hist.get(rh, {}).get("historical_tags", [])

        with open(fname, "w") as md:
            md.write(f"# Historical Lens Analysis — {rh}\n\n")

            md.write("## Historical Tags\n")
            for t in tags:
                md.write(f"- {t}\n")

            md.write("\n## Interpretation\n")
            md.write("This RUO shows connections to historical systems such as:\n")
            for t in tags:
                md.write(f"- {t}: contextually linked via term/domain structure.\n")

            md.write("\n## Relevance\n")
            md.write("Historical signals allow deeper cross‑temporal research.\n")

    print(f"[CART313] Historical lens papers → {OUTDIR}")

if __name__ == "__main__":
    main()
