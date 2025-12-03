#!/usr/bin/env python3
# CART312 — Narrative Science Writer
# Writes story-style scientific narratives around each RUO.

import json, os

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART312_NARRATIVE"

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART312] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        with open(fname, "w") as md:
            md.write(f"# Narrative Science Document — {rh}\n\n")

            md.write("## Story\n")
            md.write("In this RUO, a thread begins with a set of core concepts:\n\n")

            md.write("### Terms as Characters\n")
            for t in r["terms"]:
                md.write(f"- **{t}** plays a role in this narrative.\n")

            md.write("\n### How They Interact\n")
            md.write("The links form the world these terms explore:\n")
            for l in r["links"]:
                md.write(f"- Pathway: {l}\n")

            md.write("\n### Crossover Encounters\n")
            for c in r["crossover_links"]:
                md.write(f"- Meets `{c['target_hash']}` through {c['reason']} (W:{c['weight']}).\n")

            md.write("\n### Closing\n")
            md.write("This narrative contextualizes how this RUO contributes to the broader research universe.\n")

    print(f"[CART312] Narrative papers → {OUTDIR}")

if __name__ == "__main__":
    main()
