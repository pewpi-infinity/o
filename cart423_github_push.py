#!/usr/bin/env python3
# CART423 — GitHub Push Engine

import os
import sys
import subprocess
import shutil

REPO = "infinity_repo"
PAYLOAD = "grand_master.zip"

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: ./cart423_github_push.py <repo-url>")
        return

    url = sys.argv[1]

    if not os.path.exists(PAYLOAD):
        raise FileNotFoundError("[CART423] grand_master.zip missing")

    if not os.path.exists(REPO):
        raise FileNotFoundError("[CART423] Repo not initialized. Run CART421 first")

    shutil.copy(PAYLOAD, f"{REPO}/grand_master.zip")

    os.chdir(REPO)
    run("git add .")
    run('git commit -m "InfinityOS: Grand Master ZIP Upload"')
    run(f"git remote remove origin 2>/dev/null || true")
    run(f"git remote add origin {url}")
    run("git push -u origin master")

    print("[CART423] Successfully pushed to GitHub")

if __name__ == "__main__":
    main()
