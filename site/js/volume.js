let INF_MASTER_VOL = 0.6;
let INF_MUTED = false;

function initVolume(){
    let slider = document.getElementById("volSlider");

    // Load saved volume
    let saved = localStorage.getItem("INF_MASTER_VOL");
    if(saved !== null){
        INF_MASTER_VOL = parseFloat(saved);
        slider.value = Math.floor(INF_MASTER_VOL * 100);
    }

    slider.addEventListener("input", ()=>{
        INF_MASTER_VOL = slider.value / 100;
        localStorage.setItem("INF_MASTER_VOL", INF_MASTER_VOL);
        updateStatus();
    });

    updateStatus();
}

function toggleMute(){
    INF_MUTED = !INF_MUTED;
    updateStatus();
}

function getMasterGain(){
    return INF_MUTED ? 0 : INF_MASTER_VOL;
}

function updateStatus(){
    let status = document.getElementById("status");
    status.innerText =
       "Volume: " + Math.floor(INF_MASTER_VOL*100) +
       (INF_MUTED ? " (Muted)" : "");
}
