async function loadToken(){
  let params = new URLSearchParams(window.location.search);
  let id = params.get("id");

  let meta = await loadTokenMeta(id);
  if (!meta){
    document.getElementById("token_wrap").innerText = "Token not found.";
    return;
  }

  let rare = computeInfinityRarity(meta);

  document.getElementById("token_wrap").innerHTML = `
    <h1>INF Token #${id}</h1>
    <img src="tokens/${id}.png" style="width:200px"><br>

    <p><b>Rarity:</b> ${rare.tier}</p>
    <p><b>Rarity Score:</b> ${rare.score}</p>

    <p><b>Generation:</b> ${meta.generation}</p>
    <p><b>Writes:</b> ${meta.writes}</p>
    <p><b>Pattern:</b> ${meta.pattern.type || "None"}</p>

    <p><b>Description:</b></p>
    <pre>${meta.description || "(empty)"}</pre>

    <h3>Buy Options</h3>
    <button onclick="buyTokenUSD('${id}')">Buy with USD (PayPal)</button>
    <button onclick="buyTokenINF('${id}')">Buy with INF</button>
  `;
}

function buyTokenUSD(id){
  alert("PayPal token purchase flow here.");
}

function buyTokenINF(id){
  alert("Perform INF ledger transfer here.");
}
