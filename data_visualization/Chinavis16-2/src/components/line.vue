<template>
  <div id="test">
    <h3 style="font-size: 50px">公司发展历程1（邮件数量）</h3>
    <!-- 一定要传进去一个id，随便传一个 -->
    <d3line id="line" :dataset="data1"></d3line>
  </div>
</template>

<script>
  import d3line from '@/components/d3/Line'
  import data from '@/assets/data/period_email_num.json'
  export default {
    name: 'line',
    data() {
      return {
        data1: data
      }
    },
    components: {
      d3line
    },
    methods: {

    }
  }
</script>

<style scoped>
</style>
