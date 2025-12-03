#!/usr/bin/env python3
# CART504 — Watchdog Manager

import os, time, json

STATE = "CART501_STATE.json"
LOG = "CART504_WATCHDOG_LOG.json"

def main():
    if not os.path.exists(STATE):
        print("[CART504] Kernel missing")
        return

    with open(STATE, "r") as f:
        st = json.load(f)

    entry = {
        "timestamp": int(time.time()),
        "kernel_status": st["status"]
    }

    if os.path.exists(LOG):
        with open(LOG, "r") as f:
            log = json.load(f)
    else:
        log = []

    log.append(entry)

    with open(LOG, "w") as f:
        json.dump(log, f, indent=4)

    print("[CART504] Watchdog updated")

if __name__ == "__main__":
    main()
