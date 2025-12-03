let resonanceTimer = null;

function startResonance(){
    stopResonance();

    let mode = getMode();
    let patterns = RESONANCE_MAP[mode];
    if(!patterns || patterns.length === 0) return;

    let index = 0;
    resonanceTimer = setInterval(()=>{
        let chord = patterns[index];
        chord.forEach(f => playTone(f, 0.4));

        index = (index + 1) % patterns.length;
    }, 4500);
}

function stopResonance(){
    if(resonanceTimer){
        clearInterval(resonanceTimer);
        resonanceTimer = null;
    }
}
