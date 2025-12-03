async function attemptLogin(){
    const user = document.getElementById("login_user").value;
    const pass = document.getElementById("login_pass").value;

    let status = document.getElementById("login_status");

    // Send password to python login handler via local FS
    const resp = await fetch("../../cart904_login.py", { method:"POST" });

    // This is a simulated login result
    // In your python equivalent, login success writes CURRENT_USER.json
    const check = await fetch("../../CURRENT_USER.json").catch(()=>null);

    if (!check){
        status.innerText = "Login failed.";
        return;
    }

    status.innerText = "Success! Loading terminal...";

    setTimeout(()=> window.location.href = "terminal.html", 500);
}
