#!/usr/bin/env python3
# CART215 — Materials / Coins / Jewelry / Artifacts Scraper

import requests
from bs4 import BeautifulSoup
import json
import os
import hashlib

INPUT_SITES = "CART203_VALIDATED_SITES.json"
OUTPUT = "CART215_MATERIALS_SCRAPE.json"

MATERIAL_KEYWORDS = [
    "metal", "gold", "silver", "jewelry", "antique",
    "artifact", "coin", "copper", "steel", "bronze",
    "crystal", "gem", "sapphire", "emerald", "ruby",
    "minerals", "periodic"
]

def matches(url):
    u = url.lower()
    return any(k in u for k in MATERIAL_KEYWORDS)

def scrape(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        return soup.get_text(" ", strip=True)[:20000]
    except:
        return None

def h(t):
    return hashlib.sha256(t.encode()).hexdigest()

def main():
    if not os.path.exists(INPUT_SITES):
        raise FileNotFoundError("[CART215] Missing validated list")

    with open(INPUT_SITES, "r") as f:
        sites = json.load(f)["valid_sites"]

    rows = []

    for s in sites:
        if matches(s):
            print(f"[CART215] Scraping → {s}")
            txt = scrape(s)
            if txt:
                rows.append({
                    "site": s,
                    "category": "materials",
                    "text": txt,
                    "hash": h(txt)
                })

    with open(OUTPUT, "w") as f:
        json.dump(rows, f, indent=2)

    print(f"[CART215] Saved → {OUTPUT}")

if __name__ == "__main__":
    main()
