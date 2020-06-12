<template>
  <div class="Cloud">
    <h3 style="font-size: 50px">邮件关键词</h3>
    <div id='wordCloudBox'></div>
  </div>
</template>
<script>
  import cloud from '@/assets/js/d3.layout.cloud.js'
  import DATA from '@/assets/data/content.json'
  export default {
    name: "Cloud",
    data() {
      return {}
    },
    methods: {
    },

    mounted() {
      var d3 = require('d3')
      var layout = cloud()
        .size([1500,1500])
        .words(DATA.map(function(d) {
          return {text: d.text, size: d.size/200};
        }))
        .padding(5)
        .rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .fontSize(function(d) { return d.size; })
        .on("end", draw);

      layout.start();

      function draw(words) {
        console.log(layout)
        d3.select("#wordCloudBox").append("svg")
          .attr("width", layout.size()[0])
          .attr("height", layout.size()[1])
          .append("g")
          .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
          .selectAll("text")
          .data(words)
          .enter().append("text")
          .style("font-size", function(d) { return d.size + "px"; })
          .style("font-family", "Impact")
          .attr("text-anchor", "middle")
          .attr("fill",function(d){
            return "#"+Math.floor(Math.random()*(256*256*256-1)).toString(16);
          })
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
          })
          .text(function(d) { return d.text; });
      }
    },


  }
</script>

<style scoped>

</style>
