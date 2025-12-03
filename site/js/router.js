function INF_Route(page){
    console.log("[∞] Routing to:", page);
    document.body.classList.add("fadeout");

    setTimeout(()=>{
        window.location.href = page;
    }, 200);
}
