#!/usr/bin/env python3
# CART212 — Medical / Health Scraper

import requests
from bs4 import BeautifulSoup
import json
import os
import hashlib

INPUT_SITES = "CART203_VALIDATED_SITES.json"
OUTPUT = "CART212_MEDICAL_SCRAPE.json"

MEDICAL_KEYWORDS = [
    "health", "medicine", "medical", "wellness",
    "disease", "treatment", "genetics", "immune",
    "nutrition", "pharma", "biotech"
]

def is_medical(url):
    u = url.lower()
    return any(k in u for k in MEDICAL_KEYWORDS)

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
        raise FileNotFoundError("[CART212] Missing website list")

    with open(INPUT_SITES, "r") as f:
        sites = json.load(f)["valid_sites"]

    data = []

    for s in sites:
        if is_medical(s):
            print(f"[CART212] Scraping → {s}")
            text = scrape(s)
            if text:
                data.append({
                    "site": s,
                    "category": "medical",
                    "text": text,
                    "hash": h(text)
                })

    with open(OUTPUT, "w") as f:
        json.dump(data, f, indent=2)

    print(f"[CART212] Saved → {OUTPUT}")

if __name__ == "__main__":
    main()
