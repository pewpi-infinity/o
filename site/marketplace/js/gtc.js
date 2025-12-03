function isGTC(listing){
  let THIRTY_DAYS = 30 * 24 * 3600 * 1000;
  return (Date.now() - listing.id) > THIRTY_DAYS;
}
