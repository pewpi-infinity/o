#!/usr/bin/env python3
# CART704 — Research Preview Builder

import os, json

RUO = "CART217_RUO_STORE.json"
OUT_DIR = "site/data"

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    if not os.path.exists(RUO):
        print("[CART704] RUO store missing.")
        return

    with open(RUO, "r") as f:
        ruos = json.load(f)

    for i, r in enumerate(ruos[:10000]):  # limit to first batch
        preview = {
            "title": f"Research Entry #{i+1}",
            "abstract": f"Preview automatically generated for RUO: {r.get('terms', [])[:3]}"
        }
        with open(f"{OUT_DIR}/preview_{i}.json", "w") as f:
            json.dump(preview, f, indent=4)

    print("[CART704] Research previews generated.")

if __name__ == "__main__":
    main()
