async function loadStorefront(){
  let params = new URLSearchParams(window.location.search);
  let seller = params.get("seller");

  document.getElementById("store_title").innerText =
    "Storefront of @" + seller;

  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let wrap = document.getElementById("store_list");
  wrap.innerHTML = "";

  let sales = data.listings.filter(L => L.seller === seller);

  sales.forEach(L=>{
    let div = document.createElement("div");
    div.classList.add("listing_card");
    div.innerHTML = `
      <h3>${L.title}</h3>
      <p>$${L.usd} | ${L.inf} INF</p>
      <button onclick="window.location.href='view.html?id=${L.id}'">
        View
      </button>
    `;
    wrap.appendChild(div);
  });
}
