function computeInfinityRarity(token){
  let score = 0;

  if (token.generation < 5) score += 20;
  if (token.writes === 0) score += 25;
  if (token.pattern && token.pattern.type !== "none") score += 15;
  if (token.lottery_pull === true) score += 50;
  if (token.history && token.history.length > 3) score += 10;

  let tier = "Common";
  if (score >= 30) tier = "Uncommon";
  if (score >= 50) tier = "Rare";
  if (score >= 70) tier = "Ultra-Rare";
  if (score >= 100) tier = "Mythic";

  return {score, tier};
}
