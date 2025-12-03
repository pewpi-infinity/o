#!/usr/bin/env python3
# CART430 — Final Infinity Token Exporter

import os, zipfile

EXPORT = "infinity_token_export.zip"
VAULT = "CART429_VAULT"
GRAND = "grand_master.zip"

def main():
    with zipfile.ZipFile(EXPORT, "w", zipfile.ZIP_DEFLATED) as zipf:
        if os.path.exists(GRAND):
            zipf.write(GRAND, "grand_master.zip")

        for root, dirs, files in os.walk(VAULT):
            for f in files:
                fp = os.path.join(root, f)
                arc = fp.replace(f"{VAULT}/", "vault/")
                zipf.write(fp, arc)

    print("[CART430] Final Infinity Token export created → infinity_token_export.zip")

if __name__ == "__main__":
    main()
