async function initFilters(){}

async function runFilter(){
  let rarity = document.getElementById("rarity").value;
  let pattern = document.getElementById("pattern").value;
  let min = Number(document.getElementById("minPrice").value || 0);
  let max = Number(document.getElementById("maxPrice").value || 9999999);

  let res = await fetch("../../CART1114_TOKEN_LISTINGS.json");
  let store = await res.json();

  let out = document.getElementById("out");
  out.innerHTML = "";

  for (let entry of store.token_listings){
    let meta = await loadTokenMeta(entry.id);
    if (!meta) continue;

    let rare = computeInfinityRarity(meta);

    // Apply filters
    if (rarity && rare.tier !== rarity) continue;
    if (pattern && meta.pattern.type !== pattern) continue;
    if (entry.usd < min) continue;
    if (entry.usd > max) continue;

    let div = document.createElement("div");
    div.classList.add("listing_card");
    div.innerHTML = `
      <h3>Token #${entry.id}</h3>
      <p>Rarity: ${rare.tier}</p>
      <p>Pattern: ${meta.pattern.type}</p>
      <p>$${entry.usd} | ${entry.inf} INF</p>
    `;
    out.appendChild(div);
  }
}
