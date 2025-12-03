#!/usr/bin/env python3
# CART903 — Account Creation

import json, time, getpass
from cart902_pewpi_crypto import encrypt_pw

def main():
    username = input("Choose username: ")
    password = getpass.getpass("Choose password: ")

    capsule = {
        "user": username,
        "prefs": {},
        "local_id": int(time.time()),
        "ledger": {"balance":0,"tokens":[]}
    }

    encrypted_capsule = encrypt_pw(password, capsule)

    data = {
        "encrypted": True,
        "capsule": encrypted_capsule,
        "meta": {
            "created": int(time.time()),
            "last_login": 0
        }
    }

    with open("PEWPI_USER_CAPSULE.json","w") as f:
        json.dump(data, f, indent=4)

    print("[CART903] Account created for", username)

if __name__ == "__main__":
    main()
