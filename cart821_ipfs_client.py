#!/usr/bin/env python3
# CART821 — Browser IPFS Client Generator

import os

os.makedirs("site/js", exist_ok=True)

client = """
// CART821 — IPFS Browser Client

let ipfs = null;

async function initIPFS(){
    try {
        ipfs = await window.Ipfs.create({
            repo: 'infinity-os-ipfs-' + Math.random(),
            EXPERIMENTAL: { pubsub: true }
        });
        console.log("[IPFS] Node ready.");
    } catch(e){
        console.error("IPFS init failed", e);
    }
}
"""

with open("site/js/ipfs_client.js","w") as f:
    f.write(client)

print("[CART821] IPFS client created.")
