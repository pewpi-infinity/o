async function flagListing(id, reason){
    let res = await fetch("../../cart1156_flags.json");
    let data = await res.json();

    data.flags.push({
        id,
        reason,
        time: Date.now()
    });

    await fetch("../../cart1156_flags.json", {
        method:"POST",
        body: JSON.stringify(data, null, 2)
    });

    alert("Listing flagged.");
}
