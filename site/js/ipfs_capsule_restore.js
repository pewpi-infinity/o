async function restoreCapsuleFromCID(cid){
    if (!cid) return alert("Enter a CID.");

    const url = "https://ipfs.io/ipfs/" + cid;
    const res = await fetch(url).catch(()=>null);

    if (!res){
        alert("Failed to fetch capsule.");
        return;
    }

    const text = await res.text();

    await fetch("../../PEWPI_USER_CAPSULE.json", {
        method:"POST",
        body: text
    });

    alert("Capsule restored. Please login now.");
}
