#!/usr/bin/env python3
# CART809 — INF Reward Engine for Writing

import json, os, time, hashlib

WALLET = "CART805_WALLET.json"
REWARD = "CART809_WRITER_REWARD.json"

def load(p,d): 
    return json.load(open(p)) if os.path.exists(p) else d

def save(p,d): 
    json.dump(d, open(p,"w"), indent=4)

def complexity(text):
    return len(set(text.split()))  # unique word count

def main():
    reward = load(REWARD, {"last_write":0})
    wallet = load(WALLET, {"balance":0,"history":[]})

    now = time.time()
    delta = now - reward["last_write"]

    if delta > 900:  # reward every 15 minutes of writing focus
        amount = 1  # 1 INF per writing cycle
        wallet["balance"] += amount
        wallet["history"].append({
            "time":now,
            "type":"writer-earn",
            "amount":amount
        })
        reward["last_write"] = now

    save(WALLET, wallet)
    save(REWARD, reward)

    print("[CART809] Writer reward checked.")

if __name__ == "__main__":
    main()
