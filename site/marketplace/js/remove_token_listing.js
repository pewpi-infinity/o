async function removeTokenListing(id){
  let res = await fetch("../../CART1114_TOKEN_LISTINGS.json");
  let data = await res.json();

  data.token_listings = data.token_listings.filter(t=>t.id != id);

  await fetch("../../CART1114_TOKEN_LISTINGS.json",{
    method:"POST",
    body: JSON.stringify(data,null,2)
  });
}
