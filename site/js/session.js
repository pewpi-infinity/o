async function getCurrentUser(){
    let res = await fetch("../../CURRENT_USER.json").catch(()=>null);
    if (!res) return null;
    return await res.json();
}

async function displayCurrentUser(){
    const user = await getCurrentUser();
    const disp = document.getElementById("current_user_display");
    if (user){
        disp.innerText = "Logged in as: @" + user.user;
    }
}
