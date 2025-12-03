#!/usr/bin/env python3
# CART710 — GitHub Pages Deployer

import os, json, sys

def main():
    os.system("touch site/.nojekyll")
    os.system("git add site")
    os.system("git commit -m 'Update site for Infinity-OS UI'")
    os.system("git push")

    print("[CART710] GitHub Pages deployment complete.")

if __name__ == "__main__":
    main()
