#!/usr/bin/env python3
# CART826 — IPFS Gateway Selector

import json, os

GATEWAYS = [
    "https://ipfs.io/ipfs/",
    "https://cloudflare-ipfs.com/ipfs/",
    "https://gateway.pinata.cloud/ipfs/"
]

with open("site/js/gateway_list.js","w") as f:
    f.write("window.IPFS_GATEWAYS = " + json.dumps(GATEWAYS,indent=4))

print("[CART826] Gateway list written.")
