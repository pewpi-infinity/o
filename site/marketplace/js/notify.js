function notify(msg){
  let div = document.createElement("div");
  div.classList.add("notify");
  div.innerText = msg;
  document.body.appendChild(div);
  setTimeout(()=>div.remove(),4000);
}
