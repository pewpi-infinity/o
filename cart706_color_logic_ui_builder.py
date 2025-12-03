#!/usr/bin/env python3
# CART706 — Color Logic UI Builder

import os

# 1. HTML page
html = """
<html>
<head>
<title>Color Logic</title>
<link rel='stylesheet' href='css/style.css'>
<script src='js/colors_panel.js'></script>
</head>
<body>
<h1>Color Logic</h1>
<div id='color_map'></div>
</body>
</html>
"""
os.makedirs("site", exist_ok=True)
with open("site/colors.html", "w") as f:
    f.write(html)

# 2. JS panel
js = """
async function loadColors(){
    const panel = document.getElementById("color_map");
    const files = [
        "../CART602_COLOR_BIAS_EVOLVED.json",
        "../C13B0_COLOR_MAP.json"
    ];

    for (let f of files){
        try{
            let res = await fetch(f);
            if (!res.ok) continue;
            let data = await res.json();
            let div = document.createElement("div");
            div.innerHTML = "<h3>"+f+"</h3><pre>"+JSON.stringify(data,null,2)+"</pre>";
            panel.appendChild(div);
        } catch(e){
            console.log("Could not load",f);
        }
    }
}
window.onload = loadColors;
"""
os.makedirs("site/js", exist_ok=True)
with open("site/js/colors_panel.js", "w") as f:
    f.write(js)

print("[CART706] Color logic UI built.")
