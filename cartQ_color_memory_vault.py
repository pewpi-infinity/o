#!/usr/bin/env python3
import json, os

print("[💜 CART Q] Loading C13B0 maps...")

# Load any valid JSON map in the folder
maps = {}
for file in os.listdir("."):
    if file.startswith("C13B0_") and file.endswith(".json"):
        try:
            with open(file, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    maps[file] = data
        except:
            pass

print(f"[💜 CART Q] Maps loaded: {len(maps)}")

# Merge all dicts safely
vault = {}
for name, data in maps.items():
    for k, v in data.items():
        # Last write wins — this is intentional
        vault[k] = v

# Save the unified vault
out = "C13B0_COLOR_MEMORY.json"
with open(out, "w") as f:
    json.dump(vault, f, indent=2)

print(f"[💜 CART Q] Saved → {out}")
print("[💜 CART Q] Done.")
