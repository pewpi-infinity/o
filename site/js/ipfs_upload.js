// CART832 — Browser IPFS Upload

async function publishToIPFS(tokenObj){
    if (!ipfs){
        await initIPFS();
    }
    const file = new Blob([JSON.stringify(tokenObj,null,2)], {type:"application/json"});
    const { cid } = await ipfs.add(file);
    console.log("[CART832] Published CID:", cid.toString());
    return cid.toString();
}
