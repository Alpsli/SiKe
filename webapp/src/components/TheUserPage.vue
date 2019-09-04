<template>
  <div>
    <div class="clearfix">
      <div class="internet-map">
        <span>网络图</span>
      </div>
      <ul>
        <li class="ip-item"  @click="computedData">网络总览</li>
        <li class="ip-item"  @click="drawData0">10.10.20.241</li>
        <li class="ip-item"  @click="drawData1">10.10.20.242</li>
        <li class="ip-item"  @click="drawData2">10.10.20.243</li>
        <li class="ip-item"  @click="drawData3">10.10.20.244</li>
        <li class="ip-item"  @click="drawData4">10.10.20.245</li>
        <li class="ip-item"  @click="drawData5">10.10.20.246</li>
        <li class="ip-item"  @click="drawData6">10.10.20.247</li>
        <li class="ip-item"  @click="drawData7">10.10.20.248</li>
        <li class="ip-item"  @click="drawData8">10.10.20.249</li>
        <li class="ip-item"  @click="drawData9">10.10.20.250</li>
      </ul>
    </div>
    <div id="main"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  export default {
    name: "TheUserPage",
    data(){
      return{
        xData:[],
        yData:[],
        xxData: [],
        yyData: [],
        charts:''
      }
    },
    mounted(){
      for(let i=0;i<=9;i++){
        this.getData();
      }
      this.computedData();
    },
    // watch: {
    //   yData: function(){
    //     console.log(this.yData)
    //   }
    // },
    methods:{
      computedData(){
        this.xData = this.xxData[0];
        this.yData = [];
        let sum = 0;
        for(let i=0;i<=59;i++){
          for(let arr in this.yyData){
            sum += this.yyData[arr][i];
          }
          this.yData.push(sum);
          sum = 0
        }
        this.drawLine("main");
      },
      drawData0(){
        this.xData = this.xxData[0];
        this.yData = this.yyData[0];
        this.drawLine("main");
      },
      drawData1(){
        this.xData = this.xxData[1];
        this.yData = this.yyData[1];
        this.drawLine("main");
      },
      drawData2(){
        this.xData = this.xxData[2];
        this.yData = this.yyData[2];
        this.drawLine("main");
      },
      drawData3(){
        this.xData = this.xxData[3];
        this.yData = this.yyData[3];
        this.drawLine("main");
      },
      drawData4(){
        this.xData = this.xxData[4];
        this.yData = this.yyData[4];
        this.drawLine("main");
      },
      drawData5(){
        this.xData = this.xxData[5];
        this.yData = this.yyData[5];
        this.drawLine("main");
      },
      drawData6(){
        this.xData = this.xxData[6];
        this.yData = this.yyData[6];
        this.drawLine("main");
      },
      drawData7(){
        this.xData = this.xxData[7];
        this.yData = this.yyData[7];
        this.drawLine("main");
      },
      drawData8(){
        this.xData = this.xxData[8];
        this.yData = this.yyData[8];
        this.drawLine("main");
      },
      drawData9(){
        this.xData = this.xxData[9];
        this.yData = this.yyData[9];
        this.drawLine("main");
      },
      drawLine(id) {
        this.charts = echarts.init(document.getElementById(id));
        let option = {
          color: ['#00EE00'],
          tooltip: {trigger: 'axis', color: '#00EE00',},
          title: {
            text: "用户数量统计",
            left: 'center',
          },
          grid: {
            left: '10%',
            right: '10%',
            bottom: '10%',
            top: '10%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            name: '时间',
            boundaryGap: false,
            data: this.xData,
          },
          yAxis: {
            type: 'value',
            name: '数量',
            minInterval: 1
          },
          series: [{
            name: '个数',
            type: 'line',
            data: this.yData,
            emphasis: {
              itemStyle: {
                // 高亮时点的颜色。
                color: '#FF6A6A'
              }
            },
          }]
        };
        this.charts.setOption(option);
      },
      getData(){
        let x = new Array(60);
        for(let i=0;i<x.length;i++){
          x[i] = i;
        }
        let n = 60;
        let y = new Array(n);
        let ymin = 0;
        let ymax = 100;

        y[0] = Math.round(100 * Math.random());
        for(let i = 0;i < n-1;i++){
          let dy =  0.2 * ymax * (Math.random()-0.5) ;
          y[i+1] = Math.round(y[i] + dy) ;
          y[i+1] = Math.max(ymin,Math.min(y[i+1],ymax)) ;
        }
        if(this.xxData.length <= 10){
          this.xxData.push(x);
          this.yyData.push(y);
        }
      },
    }
  }
</script>

<style scoped>
  #main{
    width:1000px;
    height:600px;
    margin: 0 auto;
    display:inline-block;
    vertical-align: middle;
  }
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
    display: inline-block;
    vertical-align: middle;
    background-color: #FAFAFA;
    border-radius:20px
  }
  .internet-map{
    font-family: STXingkai;
    font-size: 30px;
    padding: 20px 0 0 20px;
  }
</style>
