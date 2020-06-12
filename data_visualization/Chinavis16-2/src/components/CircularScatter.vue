<template>
  <div>
    <h3 style="font-size: 50px">员工工作时间特征</h3>
    <el-row>
      <el-col :span="1">
        <div id="yzz"></div>
      </el-col>
      <el-col :span="20">
        <div id="xzz"></div>
        <div id="pic"></div>
      </el-col>
    </el-row>

  </div>
</template>
<script>
  import DATA from '@/assets/data/people_work_time.json'
  export default {
    name: "CircularScatter",
    data(){
      return {

      }
    },
    methods:{
      partition()
      {
        let width = 2400
        let height = 1900
        // 公式

        let svg2 = d3
          .select("#xzz")
          .append("svg")
          .attr("width", 2400)
          .attr("height", 50)
          .attr("transform", "translate(200,0)");

        let xScale = d3
          .scaleBand()
          .domain(['0点','1点','2点','3点','4点','5点','6点','7点','8点','9点','10点','11点','12点','13点','14点','15点','16点','17点','18点','19点','20点','21点','22点','23点'])
          .range([0, 2400]); //像素


        let axisX = d3
          .axisBottom()
          .scale(xScale) //使用上面定义的比例尺

        let gAxisX = svg2
          .append("g")
          .attr("class", "x-axis")
          .attr("transform", "translate(-20,10)")
          .style('font-size', '40px')


        axisX(gAxisX);

        let svg3 = d3
          .select("#yzz")
          .append("svg")
          .attr("width", 400)
          .attr("height", 2000)
          .attr("transform", "translate(200,0)");

        let yScale = d3
          .scaleBand()
          .domain(["alessio scarafile", "amministrazione", "antonella capaldo", "daniel maglietta", "david vincenzetti", "delivery", "fabio busatto", "giancarlo russo", "list", "lucia rana", "marco bettini", "marco valleri", "massimiliano luppi", "mostapha maana", "ornella-dev", "rsales", "simonetta gallucci", "staff", "support", "vince"])
          .range([1830, 0]); //像素
        //定义坐标轴
        //四个值：axisBottom  axisLeft axisRight axisTop
        let axisY = d3
          .axisLeft()
          .scale(yScale) //使用上面定义的比例尺
        let gAxisY = svg3
          .append("g")
          .attr("class", "y-axis")
          .attr("transform", "translate(400,50)")
          .style('font-size', '40px')
        axisY(gAxisY);

        let partition = d3.partition()
          .size([width, height])
        let color = [
          "#98abc5",
          "#8a89a6",
          "#7b6888",
          "#6b486b",
          "#ff8760",
          "#e4ad8a",
          "#ff8c00",
          "#ffb02a",
          "#a258ff",
          "#7c21ff"
        ]
        let hierarchyData = d3.hierarchy(DATA)
        // 数据转化,取所有节点的数组

        console.log(hierarchyData)
        let partitionData = partition(hierarchyData).descendants()
        // 绘图
        let svg = d3.select('#pic')
          .append('svg')
          .attr('width', width)
          .attr('height', height)
          .attr("transform", "translate(200,0)");



        let g = svg.selectAll('g')
          .data(partitionData)
          .enter()
          .append('g')
        g.append('rect')
          .attr('x', function (d) {
            return d.x0-d.data.num/80+20
          })
          .attr('y', function (d) {
            return d.y0-d.data.num/80-40
          })
          .attr('width',function (d) {
            return 10+d.data.num/45
          })
          .attr('height',function (d) {
            return 10+d.data.num/45
          })
          .style('stroke', '#ffffff')
          .style('stroke-width',0)
          .style('rx','200px')
          .style('ry','200px')
          .style('fill', function (d) {
            return color[d.data.id]
          })
        g.append('text')
          .attr('x', function (d) {
            return d.x0
          })
          .attr('y', function (d) {
            return d.y0
          })
          .attr('dx', function (d) {
            return 0
          }) // 文字水平居中
          .attr('dy', function (d) {
            return 60
          }) // 文字垂直居中,有点瑕疵
          .attr('font-size', '24px') // 文字按深度缩小
          .text(function (d) {
            console.log(d)
            return
          })
      }
    },
    mounted() {
      this.partition()
    }
  }
</script>

<style scoped>
</style>
