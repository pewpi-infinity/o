async function textSafetyCheck(text){
    const forbidden = [
        "weapon", "gun", "cocaine", "heroin",
        "stolen", "fake passport", "explosive",
        "child", "explicit", "adult only",
        "bomb", "anarchy"
    ];

    text = text.toLowerCase();

    for (let bad of forbidden){
        if (text.includes(bad)){
            return { safe:false, reason:bad };
        }
    }

    return { safe:true };
}
