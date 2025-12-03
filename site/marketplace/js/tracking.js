async function addTracking(id, trackingNumber){
  let res = await fetch("../../CART1124_COMPLETED.json");
  let data = await res.json();

  let sale = data.completed.find(x=>x.id == id);
  if (!sale) return;

  sale.tracking = trackingNumber;

  await fetch("../../CART1124_COMPLETED.json",{
    method:"POST",
    body: JSON.stringify(data,null,2)
  });
}
