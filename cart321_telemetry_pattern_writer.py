#!/usr/bin/env python3
# CART321 — Telemetry Pattern Writer
# Writes telemetry diagnostics for each RUO to track system behavior.

import json, os, hashlib, time

RUO_STORE = "CART217_RUO_STORE.json"
OUTDIR = "CART321_TELEMETRY"

def hash_str(s):
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def main():
    if not os.path.exists(RUO_STORE):
        raise FileNotFoundError("[CART321] RUO store missing")

    with open(RUO_STORE, "r") as f:
        ruos = json.load(f)

    os.makedirs(OUTDIR, exist_ok=True)

    timestamp = int(time.time())

    for r in ruos:
        rh = r["research_hash"]
        fname = f"{OUTDIR}/{rh}.md"

        telemetry = {
            "timestamp": timestamp,
            "ruo_hash": rh,
            "term_signature": hash_str(",".join(r["terms"])),
            "link_count": len(r["links"]),
            "crossover_count": len(r["crossover_links"])
        }

        with open(fname, "w") as md:
            md.write(f"# Telemetry Report — {rh}\n\n")
            for k, v in telemetry.items():
                md.write(f"- **{k}:** {v}\n")

            md.write("\n## Interpretation\nTelemetry values allow system-level monitoring for the RUO.\n")

    print(f"[CART321] Telemetry patterns → {OUTDIR}")

if __name__ == "__main__":
    main()
