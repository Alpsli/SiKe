<template>
  <div class="login">
    <el-card class="box-card">
      <div slot="header"><b>欢迎登陆</b></div>
      <el-form :model="form"  @keydown.enter.native="enter">
        <el-form-item>
          <el-input placeholder="请输入内容" v-model="form.username">
            <template slot="prepend" class="icon"><i class="el-icon-user"></i></template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-input placeholder="请输入密码" v-model="form.password" show-password>
            <template slot="prepend" class="icon"><i class="el-icon-lock"></i></template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="button" @click="enter">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
  import qs from 'qs'
  import {get,post,del,put,err} from '../util/request.js'
  export default {
    data () {
      return {
        input1: '',
        input2: '',
        form: {
          username: '',
          password: '',
        }
      }
    },
    methods:{
      enter(){
        let params = {
          name: this.form.username,
          password: this.form.password
        }
        get('/login?' + qs.stringify(params)).then(json => {
          if(json.data === true){
            this.$router.push({ name: 'homepage'})
          }else{
            this.$message({
              showClose: true,
              message: '账号或者密码输入错误',
              type: 'error'
            });
          }
        }).catch(err => {
          this.$message({
            showClose: true,
            message: '请启动服务器',
            type: 'error'
          });
          handleErr(err);
        });
      },
    }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .login{
    width: 100%;
    height: 100%;
    background-image: url('../assets/login-bg.jpg');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    position: absolute;
  }
  .box-card{
    width:320px;
    opacity: 0.9;
    margin-top: 15%;
    margin-left: 50%;
  }
  .button{
    width: 280px;
  }
</style>
