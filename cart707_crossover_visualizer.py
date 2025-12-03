#!/usr/bin/env python3
# CART707 — Crossover Visualizer

import os

html = """
<html>
<head>
<title>Crossover Map</title>
<script src='https://d3js.org/d3.v7.min.js'></script>
<script src='js/crossover.js'></script>
</head>
<body>
<h1>Crossover Evolution Map</h1>
<svg id='graph' width='1200' height='800'></svg>
</body>
</html>
"""

os.makedirs("site", exist_ok=True)
with open("site/crossover.html", "w") as f:
    f.write(html)

js = """
async function drawGraph(){
    const svg = d3.select("#graph");
    const width = +svg.attr("width");
    const height = +svg.attr("height");

    let res = await fetch("../CART603_CROSSOVER_EVOLVED.json");
    let data = await res.json();
    let latest = data.history[data.history.length-1].state;

    // convert RUO → links into graph edges
    let nodes = {};
    let edges = [];

    for (let ruo in latest){
        nodes[ruo] = {id: ruo};
        latest[ruo].forEach(link=>{
            nodes[link.target] = {id: link.target};
            edges.push({source: ruo, target: link.target, value: link.weight});
        });
    }

    let nodeList = Object.values(nodes);

    const simulation = d3.forceSimulation(nodeList)
        .force("link", d3.forceLink(edges).id(d=>d.id).distance(120))
        .force("charge", d3.forceManyBody().strength(-200))
        .force("center", d3.forceCenter(width/2, height/2));

    const link = svg.append("g")
        .selectAll("line")
        .data(edges)
        .enter().append("line")
        .style("stroke", "#aaa")
        .style("stroke-width", d=>Math.sqrt(d.value));

    const node = svg.append("g")
        .selectAll("circle")
        .data(nodeList)
        .enter().append("circle")
        .attr("r", 6)
        .style("fill","#6fa8dc");

    const text = svg.append("g")
        .selectAll("text")
        .data(nodeList)
        .enter().append("text")
        .text(d=>d.id)
        .attr("font-size","10px");

    simulation.on("tick", ()=>{
        link.attr("x1",d=>d.source.x)
            .attr("y1",d=>d.source.y)
            .attr("x2",d=>d.target.x)
            .attr("y2",d=>d.target.y);

        node.attr("cx",d=>d.x).attr("cy",d=>d.y);
        text.attr("x",d=>d.x+8).attr("y",d=>d.y+3);
    });
}

window.onload = drawGraph;
"""

os.makedirs("site/js", exist_ok=True)
with open("site/js/crossover.js", "w") as f:
    f.write(js)

print("[CART707] Crossover visualizer built.")
