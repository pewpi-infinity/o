#!/usr/bin/env python3
# CART302 — Research Threader
# Builds 3-hop reasoning threads across RUOs using crossover graphs.

import json
import os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART302_THREADS"

def top_links(ruo, count=3):
    return sorted(
        ruo["crossover_links"],
        key=lambda x: x["weight"],
        reverse=True
    )[:count]

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART302] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    ru_map = {r["research_hash"]: r for r in ruos}
    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        fname = f"{OUTDIR}/{r['research_hash']}_thread.md"

        with open(fname, "w") as f:
            f.write(f"# Research Thread — {r['research_hash']}\n\n")

            f.write("## Step 1 — Base RUO\n")
            f.write(f"`{r['research_hash']}` with terms:\n")
            for t in r["terms"]:
                f.write(f"- {t}\n")

            first_hops = top_links(r)

            f.write("\n## Step 2 — First Hop Connections\n")
            for hop in first_hops:
                h = hop["target_hash"]
                f.write(f"- → `{h}` (Weight {hop['weight']})\n")

            f.write("\n## Step 3 — Second Hop Connections\n")
            for hop in first_hops:
                h = hop["target_hash"]
                if h in ru_map:
                    second_hops = top_links(ru_map[h], 2)
                    for h2 in second_hops:
                        f.write(f"  - → `{h}` → `{h2['target_hash']}` (Weight {h2['weight']})\n")

    print(f"[CART302] Research threads written → {OUTDIR}")

if __name__ == "__main__":
    main()
