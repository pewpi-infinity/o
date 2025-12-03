#!/usr/bin/env python3
# CART214 — Ancient Text / Manuscript Scraper
# Extracts textual data from ancient-related domains.

import requests
from bs4 import BeautifulSoup
import json
import os
import hashlib

INPUT_SITES = "CART203_VALIDATED_SITES.json"
OUTPUT = "CART214_ANCIENT_SCRAPE.json"

ANCIENT_KEYWORDS = [
    "ancient", "manuscript", "myth", "mythology",
    "scripture", "temple", "scroll", "tablet",
    "archaeology", "sumer", "egypt", "greece",
    "lost", "creation", "epic"
]

def classify(url):
    u = url.lower()
    return any(k in u for k in ANCIENT_KEYWORDS)

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
        raise FileNotFoundError("[CART214] Missing list")

    with open(INPUT_SITES, "r") as f:
        sites = json.load(f)["valid_sites"]

    rows = []

    for s in sites:
        if classify(s):
            print(f"[CART214] Scraping → {s}")
            txt = scrape(s)
            if txt:
                rows.append({
                    "site": s,
                    "category": "ancient",
                    "text": txt,
                    "hash": h(txt)
                })

    with open(OUTPUT, "w") as f:
        json.dump(rows, f, indent=2)

    print(f"[CART214] Saved → {OUTPUT}")

if __name__ == "__main__":
    main()
