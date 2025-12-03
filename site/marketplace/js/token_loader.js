async function loadTokenMeta(tokenId){
  let res = await fetch(`../../site/tokens/${tokenId}.json`).catch(()=>null);
  if (!res) return null;
  return await res.json();
}
