async function validateListing(listing, allListings){
    let textCheck = await textSafetyCheck(listing.description);
    if (!textCheck.safe) return {safe:false, reason:"text:"+textCheck.reason};

    let imgCheck = await imageSafetyCheck(listing.file);
    if (!imgCheck.safe) return {safe:false, reason:"image"};

    if (detectDuplicate(listing, allListings)){
        return {safe:false, reason:"duplicate"};
    }

    let hideCheck = autoHideCheck(listing);
    if (hideCheck.hidden){
        return {safe:false, reason:"risk:"+hideCheck.score};
    }

    return {safe:true};
}
