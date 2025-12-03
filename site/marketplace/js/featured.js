async function loadFeatured(){
  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let list = data.listings;

  let featured = list.sort((a,b)=> b.usd - a.usd).slice(0,3);

  let wrap = document.getElementById("featured");
  wrap.innerHTML = "";

  featured.forEach(L=>{
    let d = document.createElement("div");
    d.classList.add("listing_card");
    d.innerHTML = `
      <h3>${L.title}</h3>
      <p>$${L.usd}</p>
      <button onclick="window.location.href='view.html?id=${L.id}'">View</button>
    `;
    wrap.appendChild(d);
  });
}
