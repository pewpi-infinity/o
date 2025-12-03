async function loadUnsold(){
  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let wrap = document.getElementById("out");
  wrap.innerHTML = "";

  let unsold = data.listings.filter(L => isGTC(L));

  unsold.forEach(L=>{
    let d = document.createElement("div");
    d.classList.add("listing_card");

    d.innerHTML = `
      <h3>${L.title}</h3>
      <p>${L.desc}</p>
      <p>USD: $${L.usd}</p>
      <p>INF: ${L.inf}</p>
      <button onclick="window.location.href='view.html?id=${L.id}'">View</button>
    `;

    wrap.appendChild(d);
  });
}
