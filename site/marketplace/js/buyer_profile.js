async function loadBuyerProfile(){
  const wrapWatch = document.getElementById("watchlist");
  const wrapOrders = document.getElementById("purchases");

  let watch = getWatchlist();
  wrapWatch.innerHTML = "";

  // Load Listings
  let listData = await (await fetch("../../CART1103_LISTINGS.json")).json();
  let listings = listData.listings;

  watch.forEach(id=>{
    let item = listings.find(L=>L.id == id);
    if (item){
      let div = document.createElement("div");
      div.classList.add("listing_card");
      div.innerHTML =
        `<h4>${item.title}</h4>
         <p>$${item.usd} | ${item.inf} INF</p>`;
      wrapWatch.appendChild(div);
    }
  });

  // Purchases (completed)
  let comp = await (await fetch("../../CART1124_COMPLETED.json")).json();
  wrapOrders.innerHTML = JSON.stringify(comp.completed, null, 2);
}
