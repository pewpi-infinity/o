function autoHideCheck(listing){
    let score = computeRiskScore(listing);

    if (score > 100){
        return {hidden:true, score};
    }
    return {hidden:false, score};
}
