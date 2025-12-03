#!/usr/bin/env python3
# CART507 — Autonomous Rebuilder

import os, json

TRIGGER = "CART503_TRIGGER.json"
CALC = "CART506_CALCULATOR_MATRIX.json"
LOG = "CART507_REBUILD_LOG.json"

MODULES = {
    "RUO_STORE": "./cart217_ruo_builder.py",
    "CROSSOVER": "./cart226_crossover_expander.py",
    "MASTERHASH": "./cart401_masterhash_builder.py",
    "MASTERZIP": "./cart408_masterzip_builder.py",
    "GRANDMASTER": "./cart415_grand_master_zip.py",
    "TOKEN": "./cart424_token_metadata_builder.py"
}

def main():
    if not os.path.exists(TRIGGER):
        print("[CART507] No trigger found.")
        return
    if not os.path.exists(CALC):
        print("[CART507] No calculator matrix found.")
        return

    with open(TRIGGER, "r") as f:
        trigger = json.load(f)
    with open(CALC, "r") as f:
        calc = json.load(f)["calculators"]

    log = []

    if trigger.get("rebuild_needed"):
        for module, script in MODULES.items():
            c = calc.get(module, {})
            if c.get("rebuild_need"):
                os.system(script)
                log.append({"module": module, "status": "rebuilt", "priority": c.get("priority")})

    with open(LOG, "w") as f:
        json.dump(log, f, indent=4)

    print("[CART507] Autonomous rebuild cycle complete.")

if __name__ == "__main__":
    main()
