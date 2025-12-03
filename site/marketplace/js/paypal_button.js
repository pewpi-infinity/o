function renderPayPalButton(containerId, amountUSD, description){
  paypal.Buttons({
    createOrder: function(data, actions){
      return actions.order.create({
        purchase_units:[{
          amount:{ value: amountUSD.toFixed(2) },
          description: description
        }]
      });
    },
    onApprove: function(data, actions){
      return actions.order.capture().then(function(details){
        alert("Purchase completed.");
      });
    }
  }).render('#'+containerId);
}
