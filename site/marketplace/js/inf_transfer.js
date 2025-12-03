async function transferINF(buyer, seller, amount){
  let res = await fetch("../../CART805_WALLET.json");
  let ledger = await res.json();

  if (ledger[buyer] < amount){
    alert("Insufficient INF.");
    return false;
  }

  ledger[buyer] -= amount;
  ledger[seller] = (ledger[seller] || 0) + amount;

  await fetch("../../CART805_WALLET.json",{
    method:"POST",
    body: JSON.stringify(ledger,null,2)
  });

  return true;
}
