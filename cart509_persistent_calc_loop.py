#!/usr/bin/env python3
# CART509 — Persistent Calculation Loop

import os, time

HISTORY = "CART509_CALC_HISTORY.json"

def main():
    print("[CART509] Starting persistent calculation loop. Ctrl+C to exit.")

    while True:
        os.system("./cart506_universal_calculator_engine.py")

        if os.path.exists("CART506_CALCULATOR_MATRIX.json"):
            os.system("jq '.' CART506_CALCULATOR_MATRIX.json >> CART509_CALC_HISTORY.json 2>/dev/null")

        time.sleep(60)

if __name__ == "__main__":
    main()
