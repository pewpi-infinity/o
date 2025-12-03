async function completeSale(item){
  let res = await fetch("../../CART1124_COMPLETED.json");
  let data = await res.json();

  data.completed.push({
    id: item.id,
    title: item.title,
    price_usd: item.usd,
    price_inf: item.inf,
    time: Date.now()
  });

  await fetch("../../CART1124_COMPLETED.json", {
    method:"POST",
    body: JSON.stringify(data,null,2)
  });
}
