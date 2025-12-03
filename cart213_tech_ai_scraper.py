#!/usr/bin/env python3
# CART213 — Tech / AI Scraper

import requests
from bs4 import BeautifulSoup
import json
import os
import hashlib

INPUT_SITES = "CART203_VALIDATED_SITES.json"
OUTPUT = "CART213_TECH_AI_SCRAPE.json"

TECH_KEYWORDS = [
    "ai", "machine", "neural", "algorithm", "robot",
    "technology", "software", "hardware", "quantum",
    "data", "compute", "chips", "innovation"
]

def is_tech(url):
    u = url.lower()
    return any(k in u for k in TECH_KEYWORDS)

def scrape(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        return soup.get_text(" ", strip=True)[:15000]
    except:
        return None

def h(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    if not os.path.exists(INPUT_SITES):
        raise FileNotFoundError("[CART213] Missing site list")

    with open(INPUT_SITES, "r") as f:
        sites = json.load(f)["valid_sites"]

    output = []

    for s in sites:
        if is_tech(s):
            print(f"[CART213] Scraping tech/AI site → {s}")
            txt = scrape(s)
            if txt:
                output.append({
                    "site": s,
                    "category": "tech_ai",
                    "text": txt,
                    "hash": h(txt)
                })

    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)

    print(f"[CART213] Saved → {OUTPUT}")

if __name__ == "__main__":
    main()
