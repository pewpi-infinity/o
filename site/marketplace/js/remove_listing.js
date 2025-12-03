async function removeListing(id){
  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  data.listings = data.listings.filter(L=>L.id !== id);

  await fetch("../../CART1103_LISTINGS.json",{
    method:"POST",
    body: JSON.stringify(data,null,2)
  });
}
