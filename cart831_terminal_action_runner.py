#!/usr/bin/env python3
# CART831 — Terminal Action Runner
# Executes the full pipeline after terminal input.

import os

def run(cmd):
    print(f"[CART831] Running pipeline for '{cmd}'")

    # Write input
    with open("CART806_INPUT.txt","w") as f:
        f.write(cmd)

    # Parse command
    os.system("python3 cart806_terminal_command_parser.py")

    # Dispatch logic
    os.system("python3 cart811_command_dispatcher.py")

    # Conversate writer (if applicable)
    if cmd.strip().lower().startswith("write ") or cmd.strip().lower().startswith("conversate "):
        os.system("python3 cart812_conversate_writer_engine.py")
        os.system("python3 cart813_research_compiler.py")
        os.system("python3 cart822_ipfs_publisher.py")
        os.system("python3 cart823_world_ledger.py")
        os.system("python3 cart824_local_first_sync.py")
        os.system("python3 cart814_feed_injector.py")

    print("[CART831] Pipeline complete.")

if __name__ == "__main__":
    run("test")
