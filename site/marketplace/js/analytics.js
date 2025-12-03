async function loadAnalytics(){
  let out = document.getElementById("out");

  let sales = await (await fetch("../../CART1124_COMPLETED.json")).json();
  let items = await (await fetch("../../CART1103_LISTINGS.json")).json();

  let avgPrice =
    items.listings.length ?
    (items.listings.reduce((a,b)=>a+b.usd,0) / items.listings.length) :
    0;

  out.innerText = JSON.stringify({
    total_listings: items.listings.length,
    completed_sales: sales.completed.length,
    avg_listing_price: avgPrice.toFixed(2)
  }, null, 2);
}
