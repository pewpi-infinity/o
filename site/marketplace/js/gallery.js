async function loadGallery(){
  let wrap = document.getElementById("grid");

  let items = await (await fetch("../../CART1103_LISTINGS.json")).json();
  let tokens = await (await fetch("../../CART1114_TOKEN_LISTINGS.json")).json();

  wrap.innerHTML = "";

  // Item Listings
  items.listings.forEach(L=>{
    let div = document.createElement("div");
    div.classList.add("listing_card");
    div.innerHTML = `
      <h4>${L.title}</h4>
      <p>$${L.usd}</p>
    `;
    wrap.appendChild(div);
  });

  // Tokens
  for (let T of tokens.token_listings){
    let R = await loadTokenMeta(T.id);
    let div = document.createElement("div");
    div.classList.add("listing_card");
    div.innerHTML = `
      <h4>Token #${T.id}</h4>
      <p>${R ? R.pattern.type : "Unknown"}</p>
    `;
    wrap.appendChild(div);
  }
}
