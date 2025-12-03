#!/usr/bin/env python3
# CART203 — Website Validator
# Validates 250 sites → ensures https + 200 OK → removes 404s

import requests
import json
import os

INPUT_FILE = "websites_250.txt"
OUTPUT_FILE = "CART203_VALIDATED_SITES.json"

def validate(url):
    if not url.startswith("http"):
        url = "https://" + url

    try:
        r = requests.get(url, timeout=10)
        return (r.status_code, url)
    except:
        return ("error", url)

def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"[CART203] Missing {INPUT_FILE}")

    with open(INPUT_FILE, "r") as f:
        sites = [l.strip() for l in f.readlines() if l.strip()]

    validated = []
    for s in sites:
        status, fixed = validate(s)
        if status == 200:
            validated.append(fixed)
            print(f"[CART203] OK → {fixed}")
        else:
            print(f"[CART203] BAD ({status}) → {fixed}")

    output = {
        "total_valid": len(validated),
        "valid_sites": validated
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=4)

    print(f"[CART203] Saved → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
