#!/usr/bin/env python3
# CART708 — Zip Directory Explorer UI

import os

html = """
<html>
<head>
<title>ZIP Explorer</title>
<script src='js/jszip.min.js'></script>
<script src='js/zip_explorer.js'></script>
</head>
<body>
<h1>Grand Master ZIP Explorer</h1>
<div id='tree'></div>
</body>
</html>
"""

os.makedirs("site", exist_ok=True)
with open("site/explorer.html", "w") as f:
    f.write(html)

js = """
async function loadZip(){
    const res = await fetch("../grand_master.zip");
    const buf = await res.arrayBuffer();
    const zip = await JSZip.loadAsync(buf);

    const tree = document.getElementById("tree");
    let html = "<ul>";

    zip.forEach((path)=>{
        html += "<li>"+path+"</li>";
    });

    html += "</ul>";
    tree.innerHTML = html;
}

window.onload = loadZip;
"""

os.makedirs("site/js", exist_ok=True)
with open("site/js/zip_explorer.js", "w") as f:
    f.write(js)

print("[CART708] ZIP Explorer built.")
