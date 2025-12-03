async function finalizeTokenPurchase(listing, method){
  if (method === "INF"){
    let ok = await finalizeINFBuy(listing);
    if (!ok) return false;
  }

  // After PayPal success you'd call this:
  await transferToken(listing.id, "CURRENT_USER");

  // remove listing
  await removeTokenListing(listing.id);

  alert("Token purchase completed successfully.");
}
