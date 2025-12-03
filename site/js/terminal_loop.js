// CART835 — Terminal UX Loop

async function sendCommand(){
    let input = document.getElementById("terminal_input").value;
    if (!input) return;

    // write command to input file
    await fetch("../CART806_INPUT.txt", {
        method:"POST",
        body: input
    });

    // run action runner server-side equivalent
    fetch("../run_cart831", {method:"POST"}); // pseudo — wired through local FS

    // wait small moment for pipeline
    setTimeout(renderFeed, 500);
}
