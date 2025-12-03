async function loadTokenListings(){
  let wrap = document.getElementById("token_listings");

  let res = await fetch("../../CART1114_TOKEN_LISTINGS.json");
  let data = await res.json();

  wrap.innerHTML = "";

  data.token_listings.forEach(L=>{
    let div = document.createElement("div");
    div.classList.add("listing_card");

    div.innerHTML = `
      <h3>Token #${L.id}</h3>
      <p>USD: $${L.usd}</p>
      <p>INF: ${L.inf}</p>

      <button onclick="window.location.href='token.html?id=${L.id}'">
        View Token
      </button>
    `;

    wrap.appendChild(div);
  });
}
