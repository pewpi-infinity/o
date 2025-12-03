function setMode(mode){
    localStorage.setItem("INF_MODE", mode);

    let event = new CustomEvent("INF_MODE_CHANGED", { detail:{mode} });
    document.dispatchEvent(event);

    playSignature("MODE_" + mode);
    playPattern(mode);   
    startResonance();    // <-- NEW

    const status = document.getElementById("status");
    if(status){
        status.innerText = "Mode set to: " + mode;
    }
}

function getMode(){
    return localStorage.getItem("INF_MODE") || "ENGINEER";
}
