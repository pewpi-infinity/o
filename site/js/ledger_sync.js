// CART833 — Global Ledger IPFS Sync

async function syncWorldLedger(){
    let res = await fetch("../WORLD_TOKEN_LEDGER.json");
    let ledger = await res.json();

    if (!ipfs){
        await initIPFS();
    }
    const file = new Blob([JSON.stringify(ledger,null,2)], {type:"application/json"});
    const { cid } = await ipfs.add(file);

    console.log("[CART833] Ledger CID:", cid.toString());
    return cid.toString();
}
