#!/usr/bin/env python3
# CART902 — AES-256-GCM Pewpi Crypto

import os, base64, json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def encrypt_pw(passphrase, data):
    salt = os.urandom(16)
    key = PBKDF2(passphrase, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(json.dumps(data).encode())
    return base64.b64encode(salt + cipher.nonce + tag + ciphertext).decode()

def decrypt_pw(passphrase, encoded):
    raw = base64.b64decode(encoded)
    salt = raw[:16]
    nonce = raw[16:32]
    tag = raw[32:48]
    ciphertext = raw[48:]
    key = PBKDF2(passphrase, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return json.loads(data.decode())

print("[CART902] Pewpi crypto loaded.")
