#!/usr/bin/env python3
# CART905 — Capsule Backup -> IPFS

import json

def main():
    with open("PEWPI_USER_CAPSULE.json","r") as f:
        cap = f.read()

    pkg = {
        "type":"capsule_backup",
        "encrypted_capsule": cap
    }

    with open("CART905_CAPSULE_PACKAGE.json","w") as f:
        json.dump(pkg,f,indent=4)

    print("[CART905] Capsule backup prepared. Browser will publish to IPFS.")

if __name__ == "__main__":
    main()
