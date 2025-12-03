async function uploadCapsuleIPFS(file){
    if (!ipfs) await initIPFS();

    const added = await ipfs.add(file);
    const cid = added.cid.toString();

    localStorage.setItem("capsule_backup_cid", cid);

    alert("Capsule uploaded.\nCID: " + cid);

    return cid;
}
