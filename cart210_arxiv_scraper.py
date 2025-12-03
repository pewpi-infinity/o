#!/usr/bin/env python3
# CART210 — arXiv Multi-Term Scraper
# Scrapes arXiv using fusion queries from CART205–CART208

import requests
from bs4 import BeautifulSoup
import json
import os
import hashlib

FUSION_FILES = [
    "CART205_PAIR_FUSION.json",
    "CART206_TRIO_FUSION.json",
    "CART207_QUAD_FUSION.json",
    "CART208_OMNI_FUSION.json"
]

OUTPUT = "CART210_ARXIV_RAW.json"

def search_arxiv(query):
    url = f"https://arxiv.org/search/?query={query}&searchtype=all"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")
    entries = soup.select(".arxiv-result")

    results = []
    for e in entries[:5]:  # limit to first 5 per query to reduce load
        title = e.select_one(".title").get_text(strip=True)
        abstract = e.select_one(".abstract").get_text(strip=True)
        authors = e.select_one(".authors").get_text(strip=True)

        paper_hash = hashlib.sha256(
            f"{title}{abstract}{authors}".encode("utf-8")
        ).hexdigest()

        results.append({
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "hash": paper_hash
        })
    return results

def load_fusions():
    fusions = []
    for f in FUSION_FILES:
        if os.path.exists(f):
            with open(f, "r") as j:
                entries = json.load(j)
                for e in entries:
                    q = e.get("query") or " ".join(e.get("terms", []))
                    fusions.append(q)
    return fusions

def main():
    fusions = load_fusions()
    all_results = []

    for q in fusions:
        print(f"[CART210] Searching arXiv → {q}")
        try:
            res = search_arxiv(q)
            all_results.append({
                "query": q,
                "results": res
            })
        except Exception as err:
            print(f"[CART210] Error on query '{q}': {err}")

    with open(OUTPUT, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"[CART210] Saved arXiv dump → {OUTPUT}")

if __name__ == "__main__":
    main()
