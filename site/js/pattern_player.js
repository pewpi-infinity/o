let patternInterval = null;

function playPattern(mode){
    stopPattern();

    let seq = OCTAVE_PATTERNS[mode];
    if(!seq) return;

    let index = 0;
    patternInterval = setInterval(()=>{
        playTone(seq[index], 0.18);
        index = (index + 1) % seq.length;
    }, 600);
}

function stopPattern(){
    if(patternInterval){
        clearInterval(patternInterval);
        patternInterval = null;
    }
}
