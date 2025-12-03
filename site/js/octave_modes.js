const OCTAVE_MODES = {
    ENGINEER: {
        type: "sine",
        gain: 0.25,
        detune: 0
    },
    ASSIMILATE: {
        type: "triangle",
        gain: 0.22,
        detune: -50
    },
    CONSTRUCT: {
        type: "square",
        gain: 0.28,
        detune: +20
    },
    CONVERSATE: {
        type: "sine",
        gain: 0.18,
        detune: +5
    },
    OBSERVE: {
        type: "sine",
        gain: 0.08,
        detune: -5
    },
    ORACLE: {
        type: "sawtooth",
        gain: 0.12,
        detune: +40
    }
};

function applyModeTone(osc){
    let mode = localStorage.getItem("INF_MODE") || "ENGINEER";
    let cfg = OCTAVE_MODES[mode];

    osc.type = cfg.type;
    osc.detune.value = cfg.detune;
    return cfg.gain;
}
