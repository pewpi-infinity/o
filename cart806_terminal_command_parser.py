#!/usr/bin/env python3
# CART806 — Terminal Command Parser

import json, os, time

OUT = "CART806_TERMINAL_COMMAND.json"

def parse(cmd):
    c = cmd.strip().lower()

    if c.startswith("open token"):
        token_id = c.replace("open token","").strip()
        return {"action":"open_token","token_id":token_id}

    if c.startswith("append "):
        text = cmd[7:]
        return {"action":"append","text":text}

    if c == "compile":
        return {"action":"compile"}

    if c == "post":
        return {"action":"post"}

    if c == "writer on":
        return {"action":"writer_on"}

    if c == "writer off":
        return {"action":"writer_off"}

    if c == "balance":
        return {"action":"balance"}

    if c == "feed":
        return {"action":"feed"}

    if c == "preview":
        return {"action":"preview"}

    if c == "help":
        return {"action":"help"}

    return {"action":"unknown","raw":cmd}

def main():
    # This reads a temp input file the UI writes
    if not os.path.exists("CART806_INPUT.txt"):
        print("[CART806] No input.")
        return

    with open("CART806_INPUT.txt","r") as f:
        line = f.read().strip()

    result = parse(line)

    with open(OUT,"w") as f:
        json.dump(result,f,indent=4)

    print("[CART806] Parsed:", result)

if __name__ == "__main__":
    main()
