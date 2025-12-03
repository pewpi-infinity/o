async function runSearch(){
  let q = document.getElementById("s_query").value.toLowerCase();
  let sort = document.getElementById("filter_sort").value;

  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let filtered = data.listings.filter(L =>
    L.title.toLowerCase().includes(q) ||
    L.desc.toLowerCase().includes(q)
  );

  if (sort === "newest")
    filtered.sort((a,b)=> b.id - a.id);

  if (sort === "price_low")
    filtered.sort((a,b)=> a.usd - b.usd);

  if (sort === "price_high")  
    filtered.sort((a,b)=> b.usd - a.usd);

  displayResults(filtered);
}

function displayResults(list){
  let wrap = document.getElementById("results");
  wrap.innerHTML = "";

  list.forEach(L=>{
    let div = document.createElement("div");
    div.classList.add("listing_card");
    div.innerHTML = `
      <h3>${L.title}</h3>
      <p>${L.desc}</p>
      <p>$${L.usd} | ${L.inf} INF</p>
      <button onclick="window.location.href='view.html?id=${L.id}'">View</button>
    `;
    wrap.appendChild(div);
  });
}
