let vizCanvas, vizCtx;
let bars = [];

function initVisualizer(){
    vizCanvas = document.getElementById("viz");
    vizCtx = vizCanvas.getContext("2d");

    // Listen for tone events
    document.addEventListener("OCTAVE_PLAYED", e => {
        bars.push({
            freq: e.detail.freq,
            ttl: 40
        });
    });

    renderLoop();
}

function renderLoop(){
    vizCtx.clearRect(0,0,vizCanvas.width,vizCanvas.height);

    bars.forEach((b,i)=>{
        let height = Math.min(b.freq / 2, vizCanvas.height);
        let x = (i*25) % vizCanvas.width;

        vizCtx.fillStyle = "hsl(" + (b.freq % 360) + ", 80%, 60%)";
        vizCtx.fillRect(
            x,
            vizCanvas.height - height,
            20,
            height
        );

        b.ttl--;
    });

    bars = bars.filter(b => b.ttl > 0);

    requestAnimationFrame(renderLoop);
}
