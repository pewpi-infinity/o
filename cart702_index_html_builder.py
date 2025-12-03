#!/usr/bin/env python3
# CART702 — index.html Builder (Zip Reader Enabled)

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Infinity‑OS — Research Interface</title>
<link rel="stylesheet" href="css/style.css">
<script src="js/jszip.min.js"></script>
<script src="js/interface.js"></script>
</head>
<body>
<h1>Infinity‑OS Research Navigator</h1>
<div id="status">Loading grand_master.zip...</div>
<div id="content"></div>
</body>
</html>
"""

with open("site/index.html", "w") as f:
    f.write(html)

print("[CART702] index.html created.")
