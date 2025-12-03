#!/usr/bin/env python3
# CART810 — Button‑Linked Logic Page Generator

import os

buttons = {
    "engineer":"Engineer Mode",
    "assimilate":"Assimilate Mode",
    "investigate":"Investigate Mode",
    "route":"Route Builder",
    "input":"Input Mode",
    "ceo":"CEO Mode",
    "data":"Data Mode"
}

for key, title in buttons.items():
    html = f"""
<html>
<head>
<title>{title}</title>
<script src='js/interface.js'></script>
</head>
<body>
<h1>{title}</h1>
<div id='feed'></div>
</body>
</html>
    """
    with open(f"site/{key}.html","w") as f:
        f.write(html)

print("[CART810] Logic pages generated.")
