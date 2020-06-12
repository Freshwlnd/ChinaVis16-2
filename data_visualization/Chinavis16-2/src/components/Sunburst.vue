<template>
  <div>
    <h3 style="font-size: 50px">各主题邮件数量</h3>
    <h3 style="font-size: 40px">{{name}}</h3>
    <h3 style="font-size: 40px">{{size}}</h3>
    <div id="pia"></div>
  </div>
</template>

<script>
  import data1 from '@/assets/data/content_sunburst1.json'
  import data2 from '@/assets/data/content_sunburst2.json'
    export default {
        name: "Sunburst",
      data(){
        return {
          name:'主题:',
          size:'邮件数量:'
        }
      },
      mounted() {
        this.$nextTick(function() {
          let da1=[]
          let da2=[]
          for(let i in data1)
            da1.push(data1[i].size)
          for(let i in data2)
            da2.push(data2[i].size)
          let width = 2000,
            height = 1500;
          let outerRadius = height / 2;
          let innerRadius = height/3;
          let innerRadius2 = height/6;

          let pie = d3.pie().sortValues(null); //饼图数据生成器，将数据生成 {"data":  1, "value":  1, "index": 6, "startAngle": 6.050474740247008, "endAngle": 6.166830023713296, "padAngle": 0},

          let c1 = d3
            .arc() //弧形生成器，将饼图生成的数据放在弧度生成器里使用。
            .innerRadius(innerRadius)
            .outerRadius(outerRadius)

          let c2 = d3
            .arc() //弧形生成器，将饼图生成的数据放在弧度生成器里使用。
            .innerRadius(innerRadius2)
            .outerRadius(innerRadius)

          let svg = d3
            .select("#pia")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

          let g = svg
            .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

          let arc = g
            .selectAll(".arc")
            .data(pie(da2))
            .enter()
            .append("g");

          arc
            .append("path")
            .attr("d", c1)
            .attr("fill", function(d){
              return "#"+Math.floor((Math.random()*(256*256*256/2))).toString(16);
            })
            .attr('id',(d,i)=>{return "pathCh"+i})
            .attr('opacity',0.3)
            .on("mouseover", (d, i) => {
              this.name='主题:'+data2[i].name
              this.size='邮件数量:'+data2[i].size
              d3.select('#pathCh'+i)
                .transition()
                .duration(500)
                .attr("opacity",1.0);
              if(i>=data1[0].children) {
                d3.select('#pathPa'+1)
                  .transition()
                  .duration(500)
                  .attr("opacity",1.0);
              } else {
                d3.select('#pathPa'+0)
                  .transition()
                  .duration(500)
                  .attr("opacity",1.0);
              }
            })
            .on("mouseout", (d,i) => {
              this.name='主题:'
              this.size='邮件数量:'
              d3.select('#pathCh'+i)
                .transition()
                .duration(500)
                .attr("opacity",0.3);
              if(i>=data1[0].children) {
                d3.select('#pathPa'+1)
                  .transition()
                  .duration(500)
                  .attr("opacity",0.3);
              } else {
                d3.select('#pathPa'+0)
                  .transition()
                  .duration(500)
                  .attr("opacity",0.3);
              }
            })



          let arc2 = g
            .selectAll(".arc")
            .data(pie(da1))
            .enter()
            .append("g");

          arc2
            .append("path")
            .attr("d", c2)
            .attr("fill", function(d){
              return "#"+Math.floor((Math.random()*(256*256*256/2))+(256*256*256/2)).toString(16);
            })
            .attr('id',(d,i)=>{return "pathPa"+i})
            .attr("opacity",0.3)
            .on("mouseover", (d, i) => {
              this.name='主题:'+data1[i].name
              this.size='邮件数量:'+data1[i].size
              d3.select('#pathPa'+i)
                .transition()
                .duration(500)
                .attr("opacity",1.0);
            })
            .on("mouseout", (d,i) => {
              this.name='主题:'
              this.size='邮件数量:'
              d3.select('#pathPa'+i)
                .transition()
                .duration(500)
                .attr("opacity",0.3);
            })



        });
      },
    }
</script>

<style scoped>

</style>
