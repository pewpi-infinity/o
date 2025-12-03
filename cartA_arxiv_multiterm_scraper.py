#!/usr/bin/env python3
import os, itertools, requests, hashlib, json, time
from datetime import datetime
from urllib.parse import quote

# -------------------------------------------------------
#   CART A — arXiv Research Scraper + Color Logic Seed
#   Batch-safe, no flooding, 2 → 5 term combos
# -------------------------------------------------------

TERMS = [
    "hydrogen","quantum","frequency","lattice","entropy","fusion","electron",
    "vapor","crystal","ionization","superconductivity","spin","wavefunction",
    "graphene","resonance","tachyon","muon","boson","neutrino","plasma",
    "bandgap","oxidation","probability","singularity","vacuum"
]  # We'll expand to 1000 later.

# Starting color logic seeds
def color_seed(term):
    term = term.lower()
    if "hydro" in term: return "purple"
    if "quant" in term: return "blue"
    if "spin" in term or "wave" in term: return "yellow"
    if "entropy" in term: return "red"
    if "crystal" in term or "lattice" in term: return "orange"
    return "green"  # default tool-state

def fetch_arxiv(query):
    url = f"https://export.arxiv.org/api/query?search_query=all:{quote(query)}&start=0&max_results=3"
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return "ERROR"

def write_temp_article(combo, content):
    path = "temp_articles"
    os.makedirs(path, exist_ok=True)
    h = hashlib.sha256((" ".join(combo) + content).encode()).hexdigest()[:16]
    filename = f"{path}/{h}.txt"
    with open(filename, "w") as f:
        f.write("TERMS: " + ", ".join(combo) + "\n")
        f.write("COLORS: " + ", ".join([color_seed(t) for t in combo]) + "\n")
        f.write("CONTENT:\n")
        f.write(content)

def batch_or_zip():
    # only zip every 10,000 articles
    path = "temp_articles"
    if not os.path.exists(path): return
    
    files = os.listdir(path)
    if len(files) < 10000:
        return  # too early
    
    # Create master directory
    master = "master_batches"
    os.makedirs(master, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zipname = f"{master}/master_batch_{stamp}.zip"
    
    os.system(f"zip -r {zipname} temp_articles > /dev/null 2>&1")
    os.system("rm -rf temp_articles")
    os.makedirs("temp_articles", exist_ok=True)

def generate_combos(terms, n):
    return list(itertools.combinations(terms, n))

def main():
    print("∞ CART A — arXiv Research Scraper Running ∞")
    print("Generating 2→5 term combinations...")
    
    for size in [2,3,4,5]:
        combos = generate_combos(TERMS, size)
        print(f"[+] {len(combos)} combos of size {size}")

        for combo in combos:
            query = " AND ".join(combo)
            print("   →", query)
            r = fetch_arxiv(query)
            write_temp_article(combo, r)
            batch_or_zip()
            time.sleep(0.3)  # Keep arXiv happy

    print("\nCompleted CART A.")
    print("Articles stored in temp_articles/")
    print("Master zips stored in master_batches/")

if __name__ == "__main__":
    main()

