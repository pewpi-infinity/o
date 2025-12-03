function INF_Heartbeat(){
    console.log("[∞] Heartbeat tick");
    // autoFeedRefresh();  // removed to stop error
}

setInterval(INF_Heartbeat, 5000);
