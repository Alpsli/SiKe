<template>
  <div>
    <el-table :data="tableData" border>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="age" label="年龄" ></el-table-column>
      <el-table-column prop="from" label="籍贯" ></el-table-column>
      <el-table-column prop="teacher" label="老师"></el-table-column>
    </el-table>
  </div>
</template>

<script>
  import {get,post,del,put,err} from '../util/request.js'
  import _ from 'lodash'
  export default {
    name: "TheTableData",
    data(){
      return{
        tableData:[]
      }
    },
    mounted(){
      get('/data').then(json => {
        this.tableData = _.cloneDeep(json.data)
      }).catch(err => {
        handleErr(err);
      });
    }
  }
</script>

<style scoped>

</style>
