#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)/infinity_research_writer"
CONFIG="$ROOT/config/color_anchors.json"
TERMS="$ROOT/topics/search_terms.txt"
LINKS="$ROOT/links/web_links.txt"
EQS="$ROOT/equations/equations.txt"
BUILD="$ROOT/build"
PAGES="$BUILD/pages"
RESOURCES="$BUILD/resources"
RES_ZIP="$BUILD/resources_links.zip"
MASTER_ZIP="$BUILD/master_research.zip"
MANIFEST="$BUILD/manifest.json"
RUNLOG="$BUILD/run.log"

# Ensure build folders exist
mkdir -p "$BUILD" "$PAGES" "$RESOURCES"

echo "[INIT] Infinity Research Writer" | tee "$RUNLOG"
echo "[PATH] ROOT=$ROOT" | tee -a "$RUNLOG"

# Verify required files exist
for f in "$CONFIG" "$TERMS" "$LINKS" "$EQS"; do
  if [ ! -f "$f" ]; then
    echo "[ERROR] Missing required file: $f" | tee -a "$RUNLOG"
    exit 1
  fi
done

# Check python
if ! command -v python3 >/dev/null 2>&1; then
  echo "[ERROR] python3 not found." | tee -a "$RUNLOG"
  exit 1
fi

# Save links catalog
cp "$LINKS" "$RESOURCES/research_links.txt"

echo "[RUN] Generating pages, resources zip, and master zip..." | tee -a "$RUNLOG"

python3 - << 'PYEND' | tee -a "$RUNLOG"
import os, json, hashlib, zipfile, random, time
from pathlib import Path

# Paths
ROOT = os.path.abspath("infinity_research_writer")
CONFIG = os.path.join(ROOT, "config", "color_anchors.json")
TERMS = os.path.join(ROOT, "topics", "search_terms.txt")
LINKS = os.path.join(ROOT, "links", "web_links.txt")
EQS = os.path.join(ROOT, "equations", "equations.txt")
BUILD = os.path.join(ROOT, "build")
PAGES = os.path.join(BUILD, "pages")
RESOURCES = os.path.join(BUILD, "resources")
RES_ZIP = os.path.join(BUILD, "resources_links.zip")
MASTER_ZIP = os.path.join(BUILD, "master_research.zip")
MANIFEST = os.path.join(BUILD, "manifest.json")

# Hash helpers
def sha256_file(fp):
    h = hashlib.sha256()
    with open(fp, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_text(txt):
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()

# Load config + data
with open(CONFIG) as f: config = json.load(f)
with open(TERMS) as f: terms = [t.strip() for t in f if t.strip()]
with open(LINKS) as f: links = [l.strip() for l in f if l.strip()]
with open(EQS) as f: eqs = [e.strip() for e in f if e.strip()]

palette = config["palette"]
default_anchors = config["rules"]["defaultAnchors"]
link_fmt = config["rules"]["linkFormat"]
max_anchors = config["rules"]["tagging"]["maxAnchorsPerPage"]

# Create term groups
def random_groups(items, min_k=2, max_k=5):
    items = items[:]
    random.shuffle(items)
    groups = []
    i = 0
    while i < len(items):
        k = random.randint(min_k, max_k)
        groups.append(items[i:i+k])
        i += k
    return groups

term_groups = random_groups(terms)

# Select anchors for term
def pick_anchors(term):
    anchors = set(default_anchors)
    lower = term.lower()
    if any(k in lower for k in ["hydrogen","fusion","battery","graphene","capacity"]):
        anchors.update(["capacity","risk","alignment"])
    if any(k in lower for k in ["governance","ethics","justice"]):
        anchors.update(["ethics","scope"])
    if any(k in lower for k in ["provenance","learning","clarity"]):
        anchors.update(["provenance","learning","clarity"])
    return list(anchors)[:max_anchors]

# Equation rigor scoring
def equation_score(eq_list):
    s = 0.0
    for e in eq_list:
        e_low = e.lower()
        if "kkt" in e_low or "lagrang" in e_low or "convex" in e_low or "robust" in e_low:
            s += 0.35
        elif "markov" in e_low or "bayes" in e_low or "confidence" in e_low:
            s += 0.25
        elif "pca" in e_low or "eigen" in e_low or "ridge" in e_low or "lasso" in e_low:
            s += 0.20
        elif "control" in e_low or "stability" in e_low:
            s += 0.25
        else:
            s += 0.10
    return min(1.0, s)

# Valuation (score and tier)
def valuation(metrics):
    weights = {
        "coverage": 0.20,
        "diversity": 0.15,
        "coherence": 0.20,
        "rigor": 0.20,
        "clarity": 0.15,
        "provenance": 0.10
    }
    score = sum(weights[k] * metrics[k] for k in weights)
    if score >= 0.8: tier = "gold"
    elif score >= 0.6: tier = "silver"
    else: tier = "bronze"
    return score, tier

# Generate pages
pages_manifest = []
target_pages = 10000
random.seed(42)
count = 0

while count < target_pages:
    group = term_groups[count % len(term_groups)]
    term = "- ".join(group).replace(" ", "") + f"-p{count+1}"
    anchors = pick_anchors(term)

    # Select links + equations
    Lk = random.sample(links, k=random.randint(1,3))
    Eq = random.sample(eqs, k=random.randint(1,3))

    # Compute metrics
    coverage = min(1.0, len(group)/5)
    diversity = min(1.0, len(set("".join(group))) / 100)
    coherence = 0.6 + 0.1*len(anchors)
    rigor = equation_score(Eq)
    clarity = 0.7
    provenance = min(1.0, len(Lk)/3)

    score, tier = valuation({
        "coverage": coverage,
        "diversity": diversity,
        "coherence": coherence,
        "rigor": rigor,
        "clarity": clarity,
        "provenance": provenance
    })

    header = "\n".join(
        f"[ANCHOR] {a} {palette.get(a,'#999999')} {link_fmt.format(anchor=a, term=term)}"
        for a in anchors
    )

    body = f"""
TITLE: {term}
SUMMARY: Research scaffold for {', '.join(group)}.

LINKS:
- {Lk[0]}
{('- ' + Lk[1]) if len(Lk)>1 else ''}
{('- ' + Lk[2]) if len(Lk)>2 else ''}

EQUATIONS:
- {Eq[0]}
{('- ' + Eq[1]) if len(Eq)>1 else ''}
{('- ' + Eq[2]) if len(Eq)>2 else ''}

VALUATION:
- Score: {score:.3f}
- Tier: {tier}
""".strip()

    content = header + "\n\n" + body + "\n"
    fname = f"{term}.txt"
    path = os.path.join(PAGES, fname)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    pages_manifest.append({
        "file": fname,
        "term": term,
        "anchors": anchors,
        "linksUsed": Lk,
        "equationsUsed": Eq,
        "score": round(score,3),
        "tier": tier,
        "hash": sha256_text(content)
    })

    count += 1
    if count % 500 == 0:
        print(f"[PROGRESS] {count} / {target_pages}")

print("[DONE] Pages written.")

# Build resources zip
with zipfile.ZipFile(RES_ZIP, "w", zipfile.ZIP_DEFLATED) as rz:
    rz.write(os.path.join(RESOURCES, "research_links.txt"), "research_links.txt")

# Build master zip
with zipfile.ZipFile(MASTER_ZIP, "w", zipfile.ZIP_DEFLATED) as mz:
    for p in pages_manifest:
        mz.write(os.path.join(PAGES, p["file"]), p["file"])
    mz.write(RES_ZIP, "resources_links.zip")

# Manifest
manifest = {
    "version": "1.0.1",
    "generatedAt": int(time.time()),
    "pageCount": len(pages_manifest),
    "masterZip": sha256_file(MASTER_ZIP),
    "resourcesZip": sha256_file(RES_ZIP)
}

with open(MANIFEST, "w") as f:
    json.dump(manifest, f, indent=2)

print("[COMPLETE] Manifest saved.")
PYEND

echo "[COMPLETE] Writer done." | tee -a "$RUNLOG"
