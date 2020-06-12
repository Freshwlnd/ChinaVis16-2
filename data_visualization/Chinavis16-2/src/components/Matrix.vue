<template>

  <div id='svgContainer' style="">
    <div class="every">
      <h3 style="font-size: 50px">公司发展历程2（工作主题）</h3>
      <el-col :span="2">
        <div id="sun"></div>
      </el-col>
      <el-col :span="22">
        <div id="xz"></div>
        <div class="svg" id="partition"></div>
      </el-col>
    </div>
  </div>
</template>

<script>
  import * as d3 from 'd3'
  import DATA from '@/assets/data/period_content.json'
  import data1 from '@/assets/data/content_sunburst3.json'

  export default {
    name: "Matrix",
    data() {
      return {}
    },
    methods: {
      partition() {
        let width = 2400
        let height = 1500
        let da1 = []
        for (let i in data1)
          da1.push(data1[i].size)
        let color = [
          "#ffffff",
          "#ebfbfa",
          "#c5f5f0",
          "#9fefe7",
          "#79e9de",
          "#53e3d4",
          "#40e0d0",
          "#ffc100",
          "#ff9a00",
          "#ff7400",
          "#ff4d00",
          "#ff0000"
        ];

        let svg2 = d3
          .select("#xz")
          .append("svg")
          .attr("width", 2400)
          .attr("height", 120);
        let rect
        for (let i in color) {
          rect = svg2.append("rect")  //添加一个矩形
            .attr("x", 10 + i * 45)
            .attr("y", 0)
            .attr("width", 50)
            .attr("height", 50)
            .attr("fill", color[i])
            .attr("transform", "translate(100,0)")
        }
        svg2.append("text")
          .attr('x', 0)
          .attr('y', 0)
          .attr('dx', 10)
          .attr('dy', 30)
          .attr('font-size', '24px')
          .attr("transform", "translate(100,0)")
          .text('低');
        svg2.append("text")
          .attr('x', 580)
          .attr('y', 0)
          .attr('dx', 10)
          .attr('dy', 30)
          .attr('font-size', '24px')
          .attr("transform", "translate(100,0)")
          .text('高')


        let xScale = d3
          .scaleBand()
          .domain([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,])
          .range([0, 2300]); //像素


        //定义坐标轴
        //四个值：axisBottom  axisLeft axisRight axisTop

        let axisX = d3
          .axisBottom()
          .scale(xScale) //使用上面定义的比例尺

        let gAxisX = svg2
          .append("g")
          .attr("class", "x-axis")
          .attr("transform", "translate(100,80)")
          .style('font-size', '20px')


        axisX(gAxisX);


        //饼图
        let pie = d3.pie().sortValues(null);
        let svg3 = d3
          .select("#sun")
          .append("svg")
          .attr("width", 400)
          .attr("height", 400)
          .attr("transform", "translate(200,200)");
        let c1 = d3
          .arc() //弧形生成器，将饼图生成的数据放在弧度生成器里使用。
          .innerRadius(0)
          .outerRadius(200)
        let g2 = svg3
          .append("g")
          .attr("transform", "translate(200,200)");
        let arc = g2
          .selectAll(".arc")
          .data(pie(da1))
          .enter()
          .append("g");

        arc
          .append("path")
          .attr("d", c1)
          .attr("fill", function (d) {
            return "#" + Math.floor((Math.random() * (256 * 256 * 256 / 2)) + (256 * 256 * 256 / 2)).toString(16);
          })
          .attr('id', (d, i) => {
            return "pathCh" + i
          })
          .attr("opacity", 0.6)
          .on("mouseover", (d, i) => {
            d3.selectAll('#pathCh' + i)
              .transition()
              .duration(500)
              .attr("opacity", 1.0);
          })
          .on("mouseout", (d, i) => {
            d3.selectAll('#pathCh' + i)
              .transition()
              .duration(500)
              .attr("opacity", 0.3);
          })
        arc.append('text')
          .attr('x', 0)
          .attr('y',0)
          .attr('dx', function (d) {
            return 30
          }) // 文字水平居中
          .attr('dy', function (d) {
            return 10
          }) // 文字垂直居中,有点瑕疵
          .attr('font-size', '40px')
          .attr('fill', "#ffffff")
          .text(data1[0].name)

        arc.append('text')
          .attr('x',0)
          .attr('y',0)
          .attr('dx', function (d) {
            return -150
          }) // 文字水平居中
          .attr('dy', function (d) {
            return 10
          }) // 文字垂直居中,有点瑕疵
          .attr('font-size', '40px')
          .attr('fill', "#ffffff")
          .text(data1[1].name)

        // 公式
        let partition = d3.partition()
          .size([height, width])
        let hierarchyData = d3.hierarchy(DATA)
        // 数据转化,取所有节点的数组
        let partitionData = partition(hierarchyData).descendants()
        // 绘图
        let svg = d3.select('#partition')
          .append('svg')
          .attr('width', width)
          .attr('height', height)


        let g = svg.selectAll('g')
          .data(partitionData)
          .enter()
          .append('g')
        g.append('rect')
          .attr('x', function (d) {
            return d.y0
          })
          .attr('y', function (d) {
            return d.x0
          })
          .attr('width', '100px')
          .attr('height', '100px')
          .attr("opacity", 0.3)
          .attr('id', (d, i) => {
            if ((i+12) % 13 < data1[0].children) {
              return "pathCh" + 0
            }
            else
              return "pathCh" + 1
          })
          .style('stroke', '#ffffff')
          .style('stroke-width', '0px')
          .style('rx', '20px')
          .style('ry', '20px')
          .style('fill', function (d) {
            return color[d.data.num]
          })
        g.append('text')
          .attr('x', function (d) {
            return d.y0
          })
          .attr('y', function (d) {
            return d.x0
          })
          .attr('dx', function (d) {
            return 10
          }) // 文字水平居中
          .attr('dy', function (d) {
            return 60
          }) // 文字垂直居中,有点瑕疵
          .attr('font-size', '24px')
          .text(function (d) {
            return d.data.topic
          })
      }
    },
    mounted() {
      this.partition()
    }
  }
</script>

<style lang="less">

  .svgContainer {
    width: 100%;
    height: 100%;

    .every {
      width: 400px;
      height: 425px;
      margin: 15px;
      float: left;

      h3 {
        margin: 0;

        .button {
          float: right;
          margin-right: 20px;
          font-size: 14px;
          cursor: pointer;
          padding: 2px 8px;
          background: yellowgreen;
          border-radius: 4px;

          &
          :hover {
            background: violet;
          }

        }
      }
      .svg {
        width: 400px;
        height: 400px;
      }

    }
  }
</style>
