#!/usr/bin/env python3

import json, os

def audit():
    print("[AUDIT] Starting Integrity Check...")

    # Load capsule
    if not os.path.exists("PEWPI_USER_CAPSULE.json"):
        print("[AUDIT] Capsule missing!")
        return

    with open("PEWPI_USER_CAPSULE.json") as f:
        cap = json.load(f)

    # Check token files
    missing = []
    for t in cap.get("tokens", []):
        if not os.path.exists(f"site/tokens/{t}.json"):
            missing.append(t)

    if missing:
        print("[AUDIT] Missing token files:", missing)

    # Ledger drift check
    if os.path.exists("CART805_WALLET.json"):
        with open("CART805_WALLET.json") as f:
            ledger = json.load(f)
        if ledger != cap.get("ledger", {}):
            print("[AUDIT] Ledger drift detected.")
            cap["ledger"] = ledger

    # Save repaired capsule
    with open("PEWPI_USER_CAPSULE.json","w") as f:
        json.dump(cap,f,indent=2)

    print("[AUDIT] Complete.")

if __name__ == "__main__":
    audit()
