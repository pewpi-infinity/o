#!/usr/bin/env python3
# CART807 — Token Viewer Page + JS

import os

html = """
<html>
<head>
<title>Token Viewer</title>
<script src='js/token_viewer.js'></script>
</head>
<body>
<h1>Token Viewer</h1>
<div id='token'></div>
</body>
</html>
"""

os.makedirs("site/js", exist_ok=True)

with open("site/token_view.html","w") as f:
    f.write(html)

js = """
async function loadToken(){
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    if (!id){
        document.getElementById("token").innerHTML = "No token ID.";
        return;
    }

    let res = await fetch("../CART803_TOKENS.json");
    let data = await res.json();

    if (!data.tokens[id]){
        document.getElementById("token").innerHTML = "Token not found.";
        return;
    }

    document.getElementById("token").innerHTML =
        "<pre>"+JSON.stringify(data.tokens[id],null,2)+"</pre>";
}

window.onload = loadToken;
"""

with open("site/js/token_viewer.js","w") as f:
    f.write(js)

print("[CART807] Token viewer built.")
