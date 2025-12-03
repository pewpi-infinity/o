#!/usr/bin/env python3
# CART422 — GitHub Credential Loader (Local Only)

import os
import json

OUT = "CART422_CREDENTIALS.json"

def main():
    user = os.getenv("GITHUB_USER", "")
    token = os.getenv("GITHUB_TOKEN", "")

    creds = {
        "github_user": user,
        "github_token_present": bool(token),
        "warning": "Token stored ONLY in env variable, not saved here."
    }

    with open(OUT, "w") as f:
        json.dump(creds, f, indent=4)

    print("[CART422] Loaded GitHub credentials (safe mode)")

if __name__ == "__main__":
    main()
