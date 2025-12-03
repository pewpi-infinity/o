async function loadDashboard(){
  let wrap = document.getElementById("dash");

  let listings  = await (await fetch("../../CART1103_LISTINGS.json")).json();
  let completed = await (await fetch("../../CART1124_COMPLETED.json")).json();
  let tokens    = await (await fetch("../../CART1114_TOKEN_LISTINGS.json")).json();

  wrap.innerHTML = `
    <h2>Active Listings</h2>
    <pre>${JSON.stringify(listings.listings,null,2)}</pre>

    <h2>Completed Sales</h2>
    <pre>${JSON.stringify(completed.completed,null,2)}</pre>

    <h2>Token Listings</h2>
    <pre>${JSON.stringify(tokens.token_listings,null,2)}</pre>
  `;
}
