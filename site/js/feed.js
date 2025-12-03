async function loadFeed(){
    let feed = document.getElementById("feed_panel");
    let res = await fetch("../../CART804_FEED_BUFFER.json").catch(()=>null);
    if (!res){
        feed.innerHTML = "<p>No feed available.</p>";
        return;
    }

    const data = await res.json();
    feed.innerHTML = "";

    data.tiles.slice().reverse().forEach(tile=>{
        let div = document.createElement("div");
        div.classList.add("feed_item");
        div.innerHTML = `
            <div class='feed_time'>${new Date(tile.time*1000).toLocaleString()}</div>
            <div class='feed_type'>${tile.type}</div>
            <pre class='feed_msg'>${tile.message}</pre>
        `;
        feed.appendChild(div);
    });
}
