function addToWatchlist(id){
  let L = JSON.parse(localStorage.getItem("watchlist") || "[]");
  if (!L.includes(id)) L.push(id);
  localStorage.setItem("watchlist", JSON.stringify(L));
  notify("Added to Watchlist.");
}

function getWatchlist(){
  return JSON.parse(localStorage.getItem("watchlist") || "[]");
}
