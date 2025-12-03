async function initTerminal(){
    displayCurrentUser();
    loadFeed();
}

async function sendTerminalCmd(){
    let input = document.getElementById("terminal_input").value;
    if (!input) return;

    // Write command into the input file
    await fetch("../../CART806_INPUT.txt", { method:"POST", body: input });

    // Trigger python pipeline
    await fetch("../../run_cart831", { method:"POST" });

    setTimeout(loadFeed, 400);
}
