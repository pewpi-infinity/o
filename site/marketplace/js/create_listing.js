async function createListing(){
  let title = document.getElementById("title").value;
  let desc = document.getElementById("desc").value;
  let usd  = Number(document.getElementById("usd").value);
  let inf  = Number(document.getElementById("inf").value);

  let res = await fetch("../../CART1103_LISTINGS.json");
  let data = await res.json();

  let id = Date.now();

  data.listings.push({
    id,
    title,
    desc,
    usd,
    inf,
    image:`${id}.png`
  });

  await fetch("../../CART1103_LISTINGS.json",{
    method:"POST",
    body: JSON.stringify(data,null,2)
  });

  document.getElementById("status").innerText = "Listing Created!";
}
