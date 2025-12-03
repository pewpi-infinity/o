#!/usr/bin/env python3
# CART651 — Production Push Gatekeeper

import os, json, hashlib

GRAND = "grand_master.zip"
HAZARDS = "CART508_HAZARD_LOG.json"
STATE = "CART501_STATE.json"
FREEZE = "CART652_FREEZE_MODE.json"
OUT = "CART651_PUSH_GATE.json"

def filehash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while c := f.read(8192):
            h.update(c)
    return h.hexdigest()

def main():
    gate = {
        "allow_push": False,
        "reason": ""
    }

    # freeze mode check
    if os.path.exists(FREEZE):
        with open(FREEZE, "r") as f:
            fr = json.load(f)
        if fr.get("mode") == "frozen":
            gate["reason"] = "System in freeze mode"
            with open(OUT, "w") as f:
                json.dump(gate, f, indent=4)
            print("[CART651] Push blocked: freeze mode")
            return

    # check grand_master.zip
    if not os.path.exists(GRAND):
        gate["reason"] = "grand_master.zip missing"
    else:
        try:
            sha = filehash(GRAND)
        except:
            gate["reason"] = "Failed to hash grand_master.zip"
            sha = None

    # check hazards
    if os.path.exists(HAZARDS):
        with open(HAZARDS, "r") as f:
            hz = json.load(f)
        if len(hz) > 0:
            gate["reason"] = "Hazards detected"
    else:
        gate["reason"] = "Missing hazard log"

    # check kernel state
    if os.path.exists(STATE):
        with open(STATE, "r") as f:
            st = json.load(f)
        if st.get("status") != "alive":
            gate["reason"] = "Kernel not alive"

    # if no reason assigned → allow push
    if gate["reason"] == "":
        gate["allow_push"] = True
        gate["reason"] = "All conditions satisfied"

    with open(OUT, "w") as f:
        json.dump(gate, f, indent=4)

    print("[CART651] Push gate evaluated →", gate)

if __name__ == "__main__":
    main()
