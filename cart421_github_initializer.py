#!/usr/bin/env python3
# CART421 — GitHub Repo Initializer

import os
import subprocess

REPO = "infinity_repo"

def run(cmd):
    subprocess.run(cmd, shell=True, check=False)

def main():
    if not os.path.exists(REPO):
        os.makedirs(REPO)

    os.chdir(REPO)

    if not os.path.exists(".git"):
        run("git init")

    # Configure if not set
    run('git config --global user.name "InfinityOS"')
    run('git config --global user.email "infinity@localhost"')

    print("[CART421] GitHub repo initialized → ./infinity_repo")

if __name__ == "__main__":
    main()
