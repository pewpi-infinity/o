#!/usr/bin/env python3
# CART801 — Terminal Engine (INF Generator + Commands)

import json, time, os, hashlib

STATE = "CART801_TERMINAL_STATE.json"
WALLET = "CART805_WALLET.json"
FEED = "CART804_FEED_BUFFER.json"

def load(path, default):
    if not os.path.exists(path):
        return default
    with open(path,"r") as f:
        return json.load(f)

def save(path, data):
    with open(path,"w") as f:
        json.dump(data, f, indent=4)

def hash_token(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    state = load(STATE, {
        "last_tick": int(time.time()),
        "inf_rate": 1,
        "inf_interval": 1800,  # 30 min
        "inf_accumulated": 0
    })

    wallet = load(WALLET, {"balance": 0, "history":[]})
    feed = load(FEED, {"tiles":[]})

    now = int(time.time())
    delta = now - state["last_tick"]

    # time-based earnings
    if delta >= state["inf_interval"]:
        cycles = delta // state["inf_interval"]
        earned = cycles * state["inf_rate"]
        wallet["balance"] += earned
        wallet["history"].append(
            {"time":now, "type":"time-earn","amount":earned}
        )
        state["last_tick"] = now

        # push a feed tile
        feed["tiles"].append({
            "type":"earn",
            "time": now,
            "inf": earned,
            "message": f"Earned {earned} INF from thinking cycle."
        })

    save(WALLET, wallet)
    save(FEED, feed)
    save(STATE, state)

    print("[CART801] Terminal engine updated.")

if __name__ == "__main__":
    main()
