async function loadListings(){
  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let wrap = document.getElementById("listing_container");
  wrap.innerHTML = "";

  data.listings.forEach(L=>{
    let div = document.createElement("div");
    div.classList.add("listing_card");

    div.innerHTML = `
      <h3>${L.title}</h3>
      <p>${L.desc}</p>
      <p>Price (USD): $${L.usd}</p>
      <p>Price (INF): ${L.inf}</p>
      <button onclick="window.location.href='view.html?id=${L.id}'">View</button>
    `;

    wrap.appendChild(div);
  });
}
