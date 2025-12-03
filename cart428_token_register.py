#!/usr/bin/env python3
# CART428 — Multi‑Token Register

import json, os, time

TOKEN = "INFINITY_TOKEN.json"
REGISTER = "CART428_TOKEN_REGISTER.json"

def main():
    if not os.path.exists(TOKEN):
        raise FileNotFoundError("[CART428] Infinity Token missing")

    with open(TOKEN, "r") as f:
        tok = json.load(f)

    entry = {
        "timestamp": int(time.time()),
        "sha256": tok["grand_master_sha256"],
        "research_count": tok["research_count"]
    }

    if os.path.exists(REGISTER):
        with open(REGISTER, "r") as f:
            reg = json.load(f)
    else:
        reg = []

    reg.append(entry)

    with open(REGISTER, "w") as f:
        json.dump(reg, f, indent=4)

    print("[CART428] Token added to global register")

if __name__ == "__main__":
    main()
