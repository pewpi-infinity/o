#!/usr/bin/env python3
# CART808 — Writer UI Builder

import os

html = """
<html>
<head>
<title>Writer</title>
<script src='js/writer.js'></script>
</head>
<body>
<h1>Writer</h1>
<div id='panel'></div>
<textarea id='append_box' rows='8' cols='60'></textarea>
<button onclick='appendText()'>Append</button>
<button onclick='saveToken()'>Save / Rehash</button>
</body>
</html>
"""

os.makedirs("site/js", exist_ok=True)

with open("site/writer.html","w") as f:
    f.write(html)

js = """
let currentToken = null;

async function loadToken(){
    const p = new URLSearchParams(window.location.search);
    const id = p.get("id");
    if (!id) return;

    let res = await fetch("../CART803_TOKENS.json");
    let data = await res.json();

    currentToken = data.tokens[id] || null;

    if (currentToken){
        document.getElementById("panel").innerHTML =
            "<pre>"+JSON.stringify(currentToken,null,2)+"</pre>";
    }
}

async function appendText(){
    const txt = document.getElementById("append_box").value;
    if (!currentToken) return;

    currentToken.text = (currentToken.text || "") + "\\n" + txt;
    document.getElementById("panel").innerHTML =
        "<pre>"+JSON.stringify(currentToken,null,2)+"</pre>";
}

async function saveToken(){
    if (!currentToken) return;

    const hash = await sha256(currentToken.text || "");
    currentToken.hash = hash;
    
    const res = await fetch("../CART803_TOKENS.json");
    let data = await res.json();

    data.tokens[currentToken.id] = currentToken;

    await fetch("../CART803_TOKENS.json",{
        method:"POST",
        body: JSON.stringify(data,null,2)
    });

    alert("Token saved.");
}

async function sha256(message){
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest("SHA-256", msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
}

window.onload = loadToken;
"""

with open("site/js/writer.js","w") as f:
    f.write(js)

print("[CART808] Writer UI created.")
