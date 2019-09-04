<template>
  <div>
    <div class="homepage">
      <div class="clearfix">
        <div class="internet-map">
          <span>网络图</span>
        </div>
        <ul>
          <li class="ip-item"  @click="showNumber1">网络总览</li>
          <li class="ip-item"  @click="showNumber2">10.10.20.241</li>
          <li class="ip-item"  @click="showNumber3">10.10.20.242</li>
          <li class="ip-item"  @click="showNumber4">10.10.20.243</li>
          <li class="ip-item"  @click="showNumber5">10.10.20.244</li>
          <li class="ip-item"  @click="showNumber6">10.10.20.245</li>
          <li class="ip-item"  @click="showNumber7">10.10.20.246</li>
          <li class="ip-item"  @click="showNumber8">10.10.20.247</li>
          <li class="ip-item"  @click="showNumber9">10.10.20.248</li>
          <li class="ip-item"  @click="showNumber10">10.10.20.249</li>
          <li class="ip-item"  @click="showNumber11">10.10.20.250</li>
        </ul>
      </div>
      <div class="assets-table">
        <el-table
          :data="tableData"
          v-if="show"
          border
          :header-row-style="tableHeaderColor"
          :row-style="{height: '60px'}"
          style="width: 751px">
          <el-table-column
            prop="name"
            label="资产清单"
            align="center"
            width="250">
          </el-table-column>
          <el-table-column
            prop="number"
            label="数量"
            align="center"
            width="250">
          </el-table-column>
          <el-table-column
            label="操作"
            align="center"
            width="250">
            <template slot-scope="scope">
              <el-button
                size="small"
                @click.native.prevent="showDetail(scope.row)">
                查看
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <el-table
        :data="tableData2"
        v-if="!show"
        :header-row-style="tableHeaderColor"
        :row-style="{height: '60px'}"
        border
        style="width: 751px">
        <el-table-column
          property="ip"
          label="IP地址"
          width="200"
          align="center">
        </el-table-column>
        <el-table-column
          property="macaddress"
          label="MAC地址"
          width="200"
          align="center">
        </el-table-column>
        <el-table-column
          property="id"
          label="ID"
          width="350"
          align="center">
        </el-table-column>
      </el-table>
      <el-dialog
        :visible.sync="dialogTableVisible">
        <el-table
          :data="tableData1"
          :header-row-style="tableHeaderColor"
          v-loading="loading1">
          <el-table-column
            property="hostname"
            label="设备名称"
            width="150"
            align="center">
          </el-table-column>
          <el-table-column
            property="type"
            label="设备类型"
            width="200"
            align="center">
          </el-table-column>
          <el-table-column
            property="managementIpAddress"
            label="IP地址"
            align="center">
          </el-table-column>
          <el-table-column
            property="macAddress"
            label="MAC地址"
            align="center">
          </el-table-column>
          <el-table-column
            property="id"
            label="ID"
            align="center">
          </el-table-column>
        </el-table>
      </el-dialog>
      </div>
   </div>
</template>

<script>
  import {get,post,del,put,err} from '../util/request.js'
  import _ from 'lodash'
  import {handleErr} from "../util/request";
  export default {
    name: "homepage",
    data(){
      return{
        loading1: true,
        dialogTableVisible:false,
        show: true,
        tableData:[{name: '无线控制器', number: 1}, {name: '交换机', number: 3}, {name: '网络', number: 10}],
        tableData1:[],
        tableData2:[],
        rowdetail:[],
        getData1: [],
        i: 0,
      }
    },
    methods:{
      getData(){
        get('http://127.0.0.1:3000/host').then(json =>{
          let data3 = _.cloneDeep(json);
          let arr = data3.slice(this.i, this.i+1);
          this.tableData2 = arr[0].link.sort(this.compare('ip'))
          }).catch(err=>{
            handleErr(err)
        })
      },
      compare(pro) {
        return function (obj1, obj2) {
          var val1 = obj1[pro];
          var val2 = obj2[pro];
          if (val1 < val2 ) { //正序
            return -1;
          } else if (val1 > val2 ) {
            return 1;
          } else {
            return 0;
          }
        }
      },
      showDetail(row) {
        this.dialogTableVisible = true;
        get('http://localhost:3000/devices').then(json =>{
          let data = _.cloneDeep(json.devices);
          if(row.number === 1){
            this.tableData1 = data.slice(0,1);
            this.loading1 = false;
          }else if(row.number === 3){
            this.tableData1 = data.slice(1,4).sort(this.compare('managementIpAddress'));
            this.loading1 = false;
          }else{
            this.tableData1 = data.slice(4).sort(this.compare('managementIpAddress'));
            this.loading1 = false;
          }}).catch(err=>{
          handleErr(err)
        });
        if(this.dialogTableVisible === true){
          this.loading1 = true;
        }
      },
      tableHeaderColor({ row, column, rowIndex, columnIndex }) {
        if (rowIndex === 0) {
          return 'color:deepskyblue;font-size: 18px;'
        }
      },
      showNumber1(){
        this.show = true;
      },
      showNumber2(){
        this.show = false;
        this.i = 2;
        this.getData();
      },
      showNumber3(){
        this.show = false;
        this.i = 4;
        this.getData();
      },
      showNumber4(){
        this.show = false;
        this.i = 5;
        this.getData();
      },
      showNumber5(){
        this.show = false;
        this.i = 6;
        this.getData();
      },
      showNumber6(){
        this.show = false;
        this.i = 7;
        this.getData();
      },
      showNumber7(){
        this.show = false;
        this.i = 8;
        this.getData();
      },
      showNumber8(){
        this.show = false;
        this.i = 9;
        this.getData();
      },
      showNumber9(){
        this.show = false;
        this.i = 10;
        this.getData();
      },
      showNumber10(){
        this.show = false;
        this.i = 11;
        this.getData();
      },
      showNumber11(){
        this.show = false;
        this.i = 3;
        this.getData();
      },
    }
  }
</script>

<style scoped>
  .ip-item{
    list-style: none;
    padding: 20px;
    color: deepskyblue;
    cursor: pointer;
  }
  .ip-item:hover{
    color: red;
    background-color: #CCFFFF;
  }
  .clearfix{
    text-align: left;
    width: 200px;
    margin-right:100px;
    background-color: #FAFAFA;
    float: left;
    border-radius:20px
  }
  .assets-table{
    display: inline-block;
    vertical-align: middle;
    margin-top: 40px;
  }
  .internet-map{
    font-family: STXingkai;
    font-size: 30px;
    padding: 20px 0 0 20px;
  }
</style>
