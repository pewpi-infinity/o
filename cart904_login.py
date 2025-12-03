#!/usr/bin/env python3
# CART904 — Login + Capsule Loader

import json, time, getpass
from cart902_pewpi_crypto import decrypt_pw

CAP = "PEWPI_USER_CAPSULE.json"

def main():
    with open(CAP,"r") as f:
        data = json.load(f)

    if not data["encrypted"]:
        print("[CART904] Capsule not encrypted — error.")
        return

    password = getpass.getpass("Password: ")

    try:
        capsule = decrypt_pw(password, data["capsule"])
    except:
        print("[CART904] Incorrect password.")
        return

    data["meta"]["last_login"] = int(time.time())
    with open(CAP,"w") as f:
        json.dump(data,f,indent=4)

    with open("CURRENT_USER.json","w") as f:
        json.dump(capsule,f,indent=4)

    print(f"[CART904] Welcome, {capsule['user']}.")

if __name__ == "__main__":
    main()
