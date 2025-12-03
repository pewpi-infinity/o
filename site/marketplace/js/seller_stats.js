function computeSellerStats(seller, completedSales){
  let sales = completedSales.filter(x=>x.seller==seller);
  let total = sales.length;
  let volume = sales.reduce((a,b)=>a+b.price_usd,0);

  return {
    total_sales: total,
    volume_usd: volume.toFixed(2),
    rating: (total>0 ? Math.min(5, 3 + total/10).toFixed(1) : "N/A")
  };
}
