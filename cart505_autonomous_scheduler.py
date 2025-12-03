#!/usr/bin/env python3
# CART505 — Autonomous Scheduler Loop

import time, os

INTERVAL = 300  # 5 minutes

def main():
    print("[CART505] Scheduler running. Ctrl+C to stop.")
    while True:
        os.system("./cart501_autonomous_kernel.py")
        os.system("./cart502_research_event_watcher.py")
        os.system("./cart503_rebuild_trigger.py")
        os.system("./cart504_watchdog.py")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
