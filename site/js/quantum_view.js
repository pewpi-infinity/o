function quantumView(state){
    return {
        basis: state,
        superposition:[
            {state: state, amplitude: 0.82},
            {state: "adjacent", amplitude: 0.18}
        ],
        collapsed: state
    };
}
