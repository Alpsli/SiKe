<template>
  <div id="login-in-layout">
    <div class="head-line">
<!--      <img src="../assets/BUPT_logo.png" draggable="false" class="bupt-img"/>-->
      <el-popover
        placement="top-end"
        width="30"
        trigger="click">
        <pre class="popovertext">用户名: {{username}}</pre>
        <pre class="popovertext">状&nbsp态: {{state}}</pre>
        <pre class="popovertext quit" @click="toLogin">&nbsp注&nbsp销</pre>
        <el-avatar slot="reference" class="user-icon" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png">
        </el-avatar>
      </el-popover>
      <div class="system-title">管理系统</div>
    </div>
    <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" active-text-color="deepskyblue" background-color="#FAFAFA">
      <el-menu-item index="/in/homepage" class="nav-item" @click="toHome">首页</el-menu-item>
      <el-menu-item index="/in/userpage" class="nav-item" @click="toUser">用户</el-menu-item>
      <el-menu-item index="/in/netpage" class="nav-item" @click="toNet">网络</el-menu-item>
      <el-menu-item index="/in/statepage" class="nav-item" @click="toState">网络状态</el-menu-item>
<!--      <el-menu-item index="/in/mappage" class="nav-item" @click="toMap">网络拓扑图</el-menu-item>-->
    </el-menu>
    <el-divider></el-divider>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        activeIndex:'/in/homepage',
        state: '在线',
        username: 'lihao'
      };
    },
    methods:{
      toHome(){
        this.$router.push({name:'homepage'})
      },
      toUser(){
        this.$router.push({name:'userpage'})
      },
      toNet(){
        this.$router.push({name:'netpage'})
      },
      toState(){
        this.$router.push({name:'statepage'})
      },
      toLogin(){
        this.$router.push({name:'login'})
      },
    }
 }
</script>

<style>
  *{
    margin:0;
    padding:0;
  }
  html {
    overflow-y: scroll;/*这一行代码会被 代码1 覆盖，我觉得是可以删除的，可能作者考虑到有可能下面的失效，那么不管有没有滚动条，在右边都会有一个灰色的区域，这也是一种解决方案，就是不管有没有滚动条，都预留位置，但是很难看啊*/
  }
  :root {
    overflow-y: auto;/*代码1*/
    overflow-x: hidden;/*横向就不使用滚动条*/
  }
  :root body {
    position: absolute;/*很不好意思，至今我仍然不知道为什么要这句代码，知道了我再补充*/
  }
  body {
    width: 100vw;
    overflow: hidden;/*超出100vw的内容都隐藏，实际我们设计的页面都不会超过100vw，而且一般会边距，所以一般滚动条的出现不会遮盖到内容*/
  }
  #login-in-layout{
    width:80%;
    margin: 0 auto;
  }
  .bupt-img{
    width:40%;
    height:160px;
    margin-top:30px;
  }
  .head-line{
    width:100%;
    height:100px;
  }
  .user-icon{
    float:right;
    width: 60px;
    height: 60px;
    margin: 10px 100px 0 0;
    cursor: pointer;
  }
  .system-title{
    font-family: STXingkai ;
    width: 40%;
    font-size: 70px;
    color: deepskyblue;
    margin:60px 0;
    letter-spacing:10px;
  }
  .nav-item{
    font-size: 20px;
  }
  .popovertext{
    text-align: center;
  }
  .quit:hover{
    color:red;
  }

</style>
