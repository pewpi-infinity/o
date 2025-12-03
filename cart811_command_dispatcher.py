#!/usr/bin/env python3
# CART811 — Command Dispatcher

import json, os, time

CMD = "CART806_TERMINAL_COMMAND.json"

def load(p,d): 
    return json.load(open(p)) if os.path.exists(p) else d

def call(script):
    os.system(f"python3 {script}")

def main():
    cmd = load(CMD, {"action":"none"})
    action = cmd.get("action")

    if action == "open_token":
        with open("CART811_DISPATCH.json","w") as f:
            json.dump({"route":"writer","id":cmd["token_id"]},f,indent=4)
        print("[CART811] Routing to writer.")
        return

    if action == "append":
        with open("CART811_APPEND.json","w") as f:
            json.dump(cmd,f,indent=4)
        call("cart803_writer_engine.py")
        print("[CART811] Append request sent.")
        return

    if action == "compile":
        call("cart813_research_compiler.py")
        print("[CART811] Compile triggered.")
        return

    if action == "post":
        call("cart815_token_register.py")
        call("cart814_feed_injector.py")
        print("[CART811] Post completed.")
        return

    if action == "writer_on":
        open("CART653_WRITER_MODE.json","w").write('{"writer_enabled":true}')
        print("[CART811] Writer ON.")
        return

    if action == "writer_off":
        open("CART653_WRITER_MODE.json","w").write('{"writer_enabled":false}')
        print("[CART811] Writer OFF.")
        return

    if action == "feed":
        call("cart804_feed_generator.py")
        print("[CART811] Feed update.")
        return

    if action == "preview":
        call("cart813_research_compiler.py")
        print("[CART811] Preview build.")
        return

    print("[CART811] Unknown or no action.")

if __name__ == "__main__":
    main()
