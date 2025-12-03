#!/usr/bin/env python3
# CART802 — Button Routing Engine

import json

ROUTES = {
    "engineer":"engineer.html",
    "assimilate":"assimilate.html",
    "investigate":"investigate.html",
    "route":"route.html",
    "input":"input.html",
    "ceo":"ceo.html",
    "data":"data.html",
    "wallet":"wallet.html",
    "writer":"writer.html"
}

with open("site/data/routes.json","w") as f:
    json.dump(ROUTES,f,indent=4)

print("[CART802] Routes written → site/data/routes.json")
