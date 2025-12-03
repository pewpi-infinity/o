function computeRiskScore(listing){
    let score = 0;

    if (listing.price_usd < 1) score += 15;
    if (listing.title.length < 3) score += 20;
    if (!listing.description || listing.description.length < 10) score += 20;
    if (listing.history && listing.history.length > 10) score += 10;
    if (listing.rarity && listing.rarity === "mythic") score -= 10;

    return score; // 0–100 safe, 101+ risky
}
