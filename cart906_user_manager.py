#!/usr/bin/env python3
# CART906 — Multi-User Capsule Manager

import os, json, time, shutil

USERS = "site/users"

os.makedirs(USERS, exist_ok=True)

def save_capsule_as(username):
    shutil.copy("PEWPI_USER_CAPSULE.json", f"{USERS}/{username}.capsule")
    print("[CART906] Saved capsule:", f"{username}.capsule")

def list_users():
    print("[CART906] Users:")
    for f in os.listdir(USERS):
        print("  •", f)

def load_user(username):
    shutil.copy(f"{USERS}/{username}.capsule", "PEWPI_USER_CAPSULE.json")
    print("[CART906] Loaded:", username)

if __name__ == "__main__":
    print("CART906 Multi-User Manager Loaded.")
