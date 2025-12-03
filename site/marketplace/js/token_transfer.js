async function transferToken(tokenId, newOwner){
  let meta = await loadTokenMeta(tokenId);
  if (!meta) return;

  meta.owner = newOwner;
  meta.history = meta.history || [];
  meta.history.push({
    owner:newOwner,
    time:Date.now()
  });

  await fetch(`../../site/tokens/${tokenId}.json`,{
    method:"POST",
    body: JSON.stringify(meta,null,2)
  });
}
