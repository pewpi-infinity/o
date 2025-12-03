async function viewListing(){
  let params = new URLSearchParams(window.location.search);
  let id = Number(params.get("id"));

  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let L = data.listings.find(x=>x.id===id);
  let wrap = document.getElementById("content");

  wrap.innerHTML = `
    <h2>${L.title}</h2>
    <p>${L.desc}</p>
    <p>USD: $${L.usd}</p>
    <p>INF: ${L.inf}</p>

    <button onclick="buyUSD(${L.id})">Buy with USD (PayPal)</button>
    <button onclick="buyINF(${L.id})">Buy with INF</button>
  `;
}

function buyUSD(id){
  alert("PayPal purchase flow will open here.");
}

function buyINF(id){
  alert("INF local token transfer will happen here.");
}
