async function finalizeINFBuy(listing){
  const buyer  = "CURRENT_USER"; // local-only placeholder
  const seller = listing.seller;

  const ok = await transferINF(buyer, seller, listing.inf);
  if (!ok){
    alert("INF balance is too low.");
    return false;
  }

  await completeSale(listing);
  await removeListing(listing.id);

  alert("INF Purchase Completed.");
  return true;
}
