function detectDuplicate(listing, allListings){
    for (let L of allListings){
        if (L.id !== listing.id){
            if (L.title === listing.title &&
                L.description === listing.description &&
                L.price_usd === listing.price_usd){
                    return true;
            }
        }
    }
    return false;
}
