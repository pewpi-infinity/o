async function listToken(){
  let id  = document.getElementById("tokenID").value;
  let usd = Number(document.getElementById("usd").value);
  let inf = Number(document.getElementById("inf").value);

  let res = await fetch("../../CART1114_TOKEN_LISTINGS.json");
  let data = await res.json();

  data.token_listings.push({
    id,
    usd,
    inf,
    time: Date.now()
  });

  await fetch("../../CART1114_TOKEN_LISTINGS.json",{
    method:"POST",
    body: JSON.stringify(data,null,2)
  });

  document.getElementById("status").innerText = "Token listed!";
}
