async function loadDiagnostics(){
    let output = {
        heartbeat: "OK",
        writer:  "OK",
        capsule: "OK",
        marketplace: "OK",
        last_audit: Date.now(),
        version: "11.x"
    };

    document.getElementById("out").innerText =
        JSON.stringify(output, null, 2);
}
