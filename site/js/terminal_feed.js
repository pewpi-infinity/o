// CART834 — Terminal Feed Renderer

async function renderFeed(){
    let target = document.getElementById("terminal_feed");
    if (!target) return;

    let res = await fetch("../CART804_FEED_BUFFER.json");
    let data = await res.json();

    target.innerHTML = "";

    data.tiles.slice().reverse().forEach(tile=>{
        let div = document.createElement("div");
        div.classList.add("feed_tile");

        div.innerHTML = `
            <div class='tile_time'>${new Date(tile.time*1000).toLocaleString()}</div>
            <div class='tile_type'>${tile.type}</div>
            <pre class='tile_preview'>${tile.preview || tile.message || ""}</pre>
        `;
        target.appendChild(div);
    });
}
