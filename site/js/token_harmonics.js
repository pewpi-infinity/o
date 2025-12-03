function tokenSignature(tokenMeta){
    let seed = tokenMeta.id || 1;
    let base = 200 + (seed % 400); // between 200–600 Hz

    return [
        base,
        base * 1.25,
        base * 1.5
    ];
}

function playTokenSignature(meta){
    tokenSignature(meta).forEach(f => playTone(f, 0.20));
}
