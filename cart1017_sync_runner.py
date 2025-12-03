#!/usr/bin/env python3

import subprocess

print("[SYNC] Starting multi‑device sync...")

subprocess.call(["python3","cart1015_sync_tokens.py"])
subprocess.call(["python3","cart1016_sync_ledger.py"])

print("[SYNC] Multi‑device sync complete. Login now.")
