function autoFeedRefresh(){
    let evt = new CustomEvent("INF_FEED_REFRESH");
    document.dispatchEvent(evt);

    console.log("[∞] Feed auto-refreshed");
}
