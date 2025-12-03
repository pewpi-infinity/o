const OCTAVE_MAP = {
  "HEARTBEAT": [440],           // A4 pulse
  "WRITE": [587, 740],          // D5 + F#5
  "AUDIT_OK": [261, 329, 392],  // C4 major chord
  "AUDIT_FAIL": [261, 311, 392],// C minor
  "MODE_ENGINEER": [440, 523, 659],
  "MODE_ASSIMILATE": [370, 440, 554]
};

function playSignature(type){
  let sig = OCTAVE_MAP[type];
  if(!sig) return;
  sig.forEach(f => playTone(f));
}
