<template>
  <div class="line wrap">
    <el-menu
      :default-active="$route.path"
      :unique-opened="true"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="homepage"><i class="el-icon-star-off"></i>首页</el-menu-item>
      <el-menu-item index="CircularScatter" ><i class="el-icon-user-solid"></i>员工工作时间特征</el-menu-item>
      <el-menu-item index="Cloud"><i class="el-icon-chat-dot-square"></i>邮件关键词</el-menu-item>
      <el-menu-item index="Sunburst"><i class="el-icon-chat-line-square"></i>各关键词邮件数量</el-menu-item>
      <el-menu-item index="line"><i class="el-icon-video-camera-solid"></i>公司发展历程1（邮件数量）</el-menu-item>
      <el-menu-item index="Matrix"><i class="el-icon-video-camera"></i>公司发展历程2（工作主题）</el-menu-item>
    </el-menu>
    <div>
      <transition name="move" mode="out-in"><router-view></router-view></transition>
    </div>
  </div>
</template>

<script>
    export default {
      data:function () {
        return {}
      },

      components:{

      },
      created(){

      },
      methods:{
        handleSelect(key, keyPath) {
          this.$router.push(key);
        }
      }
    }
</script>

<style scoped>
  .line{
    margin-top: -55px;
  }
  .wrap{
    position: relative;
    height:400px;
    width: 100%;
    background-size: cover;
  }
</style>
