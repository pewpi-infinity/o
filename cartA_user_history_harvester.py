#!/usr/bin/env python3
import os, json, re
from collections import Counter

# ---------------------------------------------------------
#  CART A — USER HISTORY HARVESTER
#  Builds the C13B0 User Intent Vector
# ---------------------------------------------------------

OUTPUT_FILE = "C13B0_USER_VECTOR.json"

def read_termux_history():
    """Reads ~/.bash_history and extracts terms."""
    hist_path = os.path.expanduser("~/.bash_history")
    if not os.path.exists(hist_path):
        return []

    with open(hist_path, "r", errors="ignore") as f:
        lines = f.readlines()

    words = []
    for line in lines:
        tokens = re.findall(r"[a-zA-Z0-9_\-]+", line.lower())
        words.extend(tokens)
    return words


def read_local_intent_file():
    """Optional expansion — user intent file."""
    intent_file = os.path.expanduser("~/intent_keywords.txt")
    if not os.path.exists(intent_file):
        return []
    with open(intent_file, "r", errors="ignore") as f:
        return re.findall(r"[a-zA-Z0-9_\-]+", f.read().lower())


def reduce_noise(words):
    """Simple stopword filter."""
    blacklist = {
        "ls","cd","mv","rm","python","pip","git","chmod","bash",
        "pkg","termux","clear","run","./","home","data","files"
    }
    return [w for w in words if w not in blacklist and len(w) > 2]


def extract_top_terms(words, top_n=50):
    """Find high-frequency interest signals."""
    counter = Counter(words)
    most_common = counter.most_common(top_n)
    return [w for w, c in most_common]


def save_vector(vector):
    with open(OUTPUT_FILE, "w") as f:
        json.dump({"C13B0_vector": vector}, f, indent=4)


def main():
    print("[💜 CART A] Harvesting user signals…")

    words = []
    words.extend(read_termux_history())
    words.extend(read_local_intent_file())

    words = reduce_noise(words)

    if not words:
        print("[💜 CART A] No meaningful history found.")
        save_vector([])
        return

    vector = extract_top_terms(words, 50)

    print("[💜 CART A] C13B0 vector generated.")
    print(vector)

    save_vector(vector)
    print(f"[💜 CART A] Saved → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
