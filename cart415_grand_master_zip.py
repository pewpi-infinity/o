#!/usr/bin/env python3
# CART415 — Grand Master ZIP Builder

import os, zipfile

SRC = "CART410_ZIPSTRUCT"
ZOUT = "grand_master.zip"

def main():
    with zipfile.ZipFile(ZOUT, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SRC):
            for file in files:
                fp = os.path.join(root, file)
                arc = fp.replace(f"{SRC}/", "")
                zipf.write(fp, arc)

    print("[CART415] Grand Master ZIP created → grand_master.zip")

if __name__ == "__main__":
    main()
