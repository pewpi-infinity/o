function computeSellerTrust(seller){
    let trust = 50;

    if (seller.completed_sales > 10) trust += 20;
    if (seller.flags_received === 0) trust += 20;
    if (seller.listings_hidden === 0) trust += 10;

    return Math.min(100, trust);
}
