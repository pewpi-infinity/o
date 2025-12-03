#!/usr/bin/env python3
# CART211 — Science Websites Scraper
# Scrapes validated science-related URLs from CART203

import requests
from bs4 import BeautifulSoup
import json
import os
import hashlib

INPUT_SITES = "CART203_VALIDATED_SITES.json"
OUTPUT = "CART211_SCIENCE_SCRAPE.json"

SCIENCE_KEYWORDS = [
    "physics", "chemistry", "biology", "astronomy", "geology",
    "energy", "hydrogen", "fusion", "quantum", "neutrino",
    "materials", "periodic", "laboratory"
]

def is_science_site(url):
    url_low = url.lower()
    return any(k in url_low for k in SCIENCE_KEYWORDS)

def hash_page(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def scrape(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        text = soup.get_text(" ", strip=True)
        return text[:10000]  # limit raw text
    except:
        return None

def main():
    if not os.path.exists(INPUT_SITES):
        raise FileNotFoundError("[CART211] Missing CART203_VALIDATED_SITES.json")

    with open(INPUT_SITES, "r") as f:
        sites = json.load(f)["valid_sites"]

    results = []

    for s in sites:
        if is_science_site(s):
            print(f"[CART211] Scraping science site → {s}")
            text = scrape(s)
            if text:
                results.append({
                    "site": s,
                    "category": "science",
                    "text": text,
                    "hash": hash_page(text)
                })

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2)

    print(f"[CART211] Saved → {OUTPUT}")

if __name__ == "__main__":
    main()
