document.addEventListener("INF_TOKEN_OPENED", (e)=>{
    playTokenSignature(e.detail.meta);
});

document.addEventListener("INF_FEED_REFRESH", ()=>{
    playSignature("WRITE");
});

document.addEventListener("INF_HEARTBEAT", ()=>{
    playSignature("HEARTBEAT");
});
