#!/usr/bin/env python3
# CART709 — Navigation System Generator

import os, json

nav = """
<div id='nav'>
<ul>
<li><a href='index.html'>Home</a></li>
<li><a href='colors.html'>Color Logic</a></li>
<li><a href='crossover.html'>Crossover Map</a></li>
<li><a href='explorer.html'>ZIP Explorer</a></li>
<li><a href='hash_token_panel.html'>Hash / Token</a></li>
</ul>
</div>
"""

os.makedirs("site/js", exist_ok=True)
os.makedirs("site/assets", exist_ok=True)

with open("site/assets/nav.html", "w") as f:
    f.write(nav)

print("[CART709] Navigation system built.")
