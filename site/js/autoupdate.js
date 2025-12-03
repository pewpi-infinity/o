async function INF_CheckForUpdates(){
    console.log("[∞] Checking for updates...");

    let local = await fetch("CART_UPDATE_INDEX.json").then(r=>r.json()).catch(()=>null);
    if(!local) return;

    let remote = await fetch("https://raw.githubusercontent.com/yourrepo/CART_UPDATE_INDEX.json")
        .then(r=>r.json())
        .catch(()=>null);

    if(!remote) return;

    if(remote.version > local.version){
        console.log("[∞] Update available:", remote.version);
        applyUpdate(remote);
    }
}

async function applyUpdate(remote){
    console.log("[∞] Applying update...");

    for(let cart of remote.carts){
        let text = await fetch(cart.url).then(r=>r.text());
        await fetch(cart.localPath, {
            method:"POST",
            body: text
        });
    }

    console.log("[∞] Update complete.");
}
