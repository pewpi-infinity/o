let audio = new (window.AudioContext || window.webkitAudioContext)();

function playTone(freq, duration=0.15){
    let osc = audio.createOscillator();
    let gainNode = audio.createGain();

    // apply mode personality shaping
    let modeGain = applyModeTone(osc);

    // apply master volume
    let finalGain = modeGain * getMasterGain();

    osc.frequency.value = freq;
    gainNode.gain.setValueAtTime(finalGain, audio.currentTime);

    osc.connect(gainNode);
    gainNode.connect(audio.destination);

    osc.start();

    // visualizer event
    let evt = new CustomEvent("OCTAVE_PLAYED", { detail:{freq} });
    document.dispatchEvent(evt);

    // fade out then stop
    setTimeout(()=>{
        gainNode.gain.exponentialRampToValueAtTime(
            0.0001,
            audio.currentTime + 0.05
        );
        osc.stop(audio.currentTime + 0.06);
    }, duration * 1000);
}
