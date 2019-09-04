<template>
  <div>
    <svg width="1000" height="700"></svg>
  </div>
</template>

<script>
  import * as d3 from 'd3'
  import dagreD3 from 'dagre-d3'
  export default {
    name: "TheMapPage",
    mounted(){
      this.drawMap();
    },
    methods:{
      drawMap(){
        var g = new dagreD3.graphlib.Graph().setGraph({rankdir: 'TB'}).setDefaultEdgeLabel(function () {
          return {};
        });
        g.setNode(0, {label: "DNA Center 1.2.10"});
        g.setNode(1, {label: "Public Internet"});
        g.setNode(2, {label: "C-3850"});
        g.setNode(3, {label: "C9300-24UX-1"});
        g.setNode(4, {label: "C9300-24UX-2"});
        g.setNode(5, {label: "HOST-1"});
        g.setNode(6, {label: "HOST-2"});

        g.setEdge(0, 1, { arrowhead: 'undirected' });
        g.setEdge(1, 2, { arrowhead: 'undirected' });
        g.setEdge(2, 3, { arrowhead: 'undirected' });
        g.setEdge(2, 4, { arrowhead: 'undirected' });
        g.setEdge(3, 5, { arrowhead: 'undirected' });
        g.setEdge(4, 6, { arrowhead: 'undirected' });
        var render = new dagreD3.render();
        // 创建SVG中的g元素，以便渲染.
        var svg = d3.select("svg"),
          svgGroup = svg.append("g");
        // 启动渲染器
        render(d3.select("svg g"), g);
        var xCenterOffset = (svg.attr("width") - g.graph().width) / 2;
        svgGroup.attr("transform", "translate(" + xCenterOffset + ", 20)");
        svg.attr("height", g.graph().height + 40);
      }
    }
  }
</script>

<style>
  text {
    font-weight: 300;
    font-family: "Times New Roman";
    font-size: 14px;
    fill: black;
  }
  g.node {
    stroke: #333;
    fill: deepskyblue;
  }
  g.node:hover{
    stroke-width: 2px;
    stroke: black;
  }
  .edgePath path {
    stroke: #00BFFF;
    stroke-width: 1.5px;
  }
</style>
