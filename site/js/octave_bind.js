function bindOctave(){
    setInterval(()=>playSignature("HEARTBEAT"), 8000);

    document.addEventListener("INF_WRITE_EVENT", ()=>{
        playSignature("WRITE");
    });

    document.addEventListener("INF_MODE_CHANGED", (e)=>{
        playSignature("MODE_" + e.detail.mode);
    });

    document.addEventListener("INF_AUDIT_OK", ()=>{
        playSignature("AUDIT_OK");
    });

    document.addEventListener("INF_AUDIT_FAIL", ()=>{
        playSignature("AUDIT_FAIL");
    });
}
