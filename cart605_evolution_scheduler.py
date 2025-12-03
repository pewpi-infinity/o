#!/usr/bin/env python3
# CART605 — Evolution Scheduler (Stage‑6)
# Runs term evolution, color mutation, crossover evolution, and logging in a loop.

import os, time

INTERVAL = 600  # 10 minutes

def main():
    print("[CART605] Evolution scheduler running. Ctrl+C to stop.")
    while True:
        os.system("./cart601_term_evolution_engine.py")
        os.system("./cart602_color_logic_mutator.py")
        os.system("./cart603_crossover_evolution_engine.py")
        os.system("./cart604_evolution_history_recorder.py")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
