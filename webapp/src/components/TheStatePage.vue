<template>
  <div>
    <div class="clearfix">
      <div class="internet-map">
        <span>网络图</span>
      </div>
      <ul>
        <li class="ip-item" @click="drawAll">网络总览</li>
        <li class="ip-item" @click="updateData0">10.10.20.241</li>
        <li class="ip-item" @click="updateData1">10.10.20.242</li>
        <li class="ip-item" @click="updateData2">10.10.20.243</li>
        <li class="ip-item" @click="updateData3">10.10.20.244</li>
        <li class="ip-item" @click="updateData4">10.10.20.245</li>
        <li class="ip-item" @click="updateData5">10.10.20.246</li>
        <li class="ip-item" @click="updateData6">10.10.20.247</li>
        <li class="ip-item" @click="updateData7">10.10.20.248</li>
        <li class="ip-item" @click="updateData8">10.10.20.249</li>
        <li class="ip-item" @click="updateData9">10.10.20.250</li>
      </ul>
    </div>
    <div id="date" v-if="datePicker">
      <el-date-picker
        v-model="value1"
        type="datetimerange"
        :picker-options="pickerOptions"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
        align="right">
      </el-date-picker>
      <el-button type="primary" @click="changeData">查看</el-button>
    </div>
    <div>
      <div id="main1"></div>
      <div id="main2"></div>
      <div id="main3"></div>
    </div>
  </div>
</template>


<script>
import echarts from 'echarts'
export default {
  name: "TheStatePage",
  data() {
    return {
      pickerOptions: {
        shortcuts: [
          {
            text: '一小时内',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000);
              picker.$emit('pick', [start, end]);
            }
          },
        ]
      },
      datePicker: true,
      value1: [],
      xData1: [],
      yData1: [],
      xxData1: [],
      yyData1: [],
      xxData2: [],
      yyData2: [],
      xxData3: [],
      yyData3: [],
      title: ''
    }
  },
  mounted(){
    this.setDate();
    for(let i=0;i<=59;i++){
      this.xData1.push(i)
    }
    for(let i=0;i<=9;i++){
      this.randomData1();
      this.randomData2();
      this.randomData3();
    }
    this.drawAll();
  },
  methods:{
    changeData(){
      this.yyData1 = [];
      this.yyData2 = [];
      this.yyData3 = [];
      this.xxData1 = [];
      this.xxData2 = [];
      this.xxData3 = [];
      for(let i=0;i<=59;i++){
        this.xData1.push(i)
      }
      for(let i=0;i<=9;i++){
        this.randomData1();
        this.randomData2();
        this.randomData3();
      }
      this.drawAll();
    },
    drawAll(){
      this.datePicker = true;
      this.xData1 = this.xxData1[0];
      this.yData1 = [];
      let sum1 = 0;
      for(let i=0;i<=59;i++){
        for(let arr in this.yyData1){
          sum1 += this.yyData1[arr][i];
        }
        this.yData1.push(sum1);
        sum1 = 0;
      }
      this.title = '网络整体健康度';
      this.drawLine("main1");
      this.yData1 = [];
      let sum2 = 0;
      for(let i=0;i<=59;i++){
        for(let arr in this.yyData2){
          sum2 += this.yyData2[arr][i];
        }
        this.yData1.push(sum2);
        sum2 = 0;
      }
      this.title = '站点健康度';
      this.drawLine("main2");
      this.yData1 = [];
      let sum3 = 0;
      for(let i=0;i<=59;i++){
        for(let arr in this.yyData3){
          sum3 += this.yyData3[arr][i];
        }
        this.yData1.push(sum3);
        sum3 = 0;
      }
      this.title = '用户网络健康度';
      this.drawLine("main3")
    },
    updateData0(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[0]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[0]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[0]
      this.drawLine("main3")
    },
    updateData1(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[1]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[1]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[1]
      this.drawLine("main3")
    },
    updateData2(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[2]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[2]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[2]
      this.drawLine("main3")
    },
    updateData3(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[9]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[9]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[9]
      this.drawLine("main3")
    },
    updateData4(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[3]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[3]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[3]
      this.drawLine("main3")
    },
    updateData5(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[4]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[4]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[4]
      this.drawLine("main3")
    },
    updateData6(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[5]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[5]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[5]
      this.drawLine("main3")
    },
    updateData7(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[6]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[6]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[6]
      this.drawLine("main3")
    },
    updateData8(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[7]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[7]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[7]
      this.drawLine("main3")
    },
    updateData9(){
      this.datePicker = false;
      this.title = '网络整体健康度';
      this.yData1 = this.yyData1[8]
      this.drawLine("main1");
      this.title = '站点健康度';
      this.yData1 = this.yyData2[8]
      this.drawLine("main2");
      this.title = '用户网络健康度';
      this.yData1 = this.yyData3[8]
      this.drawLine("main3")
    },
    setDate(){
      const end = new Date();
      const start = new Date();
      start.setTime(start.getTime() - 60 * 1000 * 60);
      this.value1 = [start, end];
    },
    randomData1(){
      let x = new Array(60);
      for(let i=0;i<x.length;i++){
        x[i] = i;
      }
      let n = 60;
      let y = new Array(n);
      let ymin = 0;
      let ymax = 99;

      y[0] = Math.round(100 * Math.random());
      for(let i = 0;i < n-1;i++){
        let dy =  0.2 * ymax * (Math.random()-0.5) ;
        y[i+1] = Math.round(y[i] + dy) ;
        y[i+1] = Math.max(ymin,Math.min(y[i+1],ymax)) ;
      }
      if(this.xxData1.length <= 10) {
        this.xxData1.push(x);
        this.yyData1.push(y);
      }
    },
    randomData2(){
      let x = new Array(60);
      for(let i=0;i<x.length;i++){
        x[i] = i;
      }
      let n = 60;
      let y = new Array(n);
      let ymin = 0;
      let ymax = 99;

      y[0] = Math.round(100 * Math.random());
      for(let i = 0;i < n-1;i++){
        let dy =  0.2 * ymax * (Math.random()-0.5) ;
        y[i+1] = Math.round(y[i] + dy) ;
        y[i+1] = Math.max(ymin,Math.min(y[i+1],ymax)) ;
      }
      if(this.xxData2.length <= 10) {
        this.xxData2.push(x);
        this.yyData2.push(y);
      }
    },
    randomData3(){
      let x = new Array(60);
      for(let i=0;i<x.length;i++){
        x[i] = i;
      }
      let n = 60;
      let y = new Array(n);
      let ymin = 0;
      let ymax = 99;

      y[0] = Math.round(100 * Math.random());
      for(let i = 0;i < n-1;i++){
        let dy =  0.2 * ymax * (Math.random()-0.5) ;
        y[i+1] = Math.round(y[i] + dy) ;
        y[i+1] = Math.max(ymin,Math.min(y[i+1],ymax)) ;
      }
      if(this.xxData3.length <= 10) {
        this.xxData3.push(x);
        this.yyData3.push(y);
      }
    },
    drawLine(id) {
      this.charts = echarts.init(document.getElementById(id));
      let option = {
        color: ['#00EE00'],
        tooltip: {
          trigger: 'axis',
          color: '#00EE00',
          formatter: function(o) {
            let arr = [
              '最近1小时第' + o[0].dataIndex + '分钟<br/>',
              '用户数量：' + o[0].data
            ];
            return arr.join('');
          }
        },
        title: {
          text: this.title,
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
          name: '时间(分钟)',
          boundaryGap: false,
          data: this.xData1,
        },
        yAxis: {
          type: 'value',
          name: '数量',
          minInterval: 1
        },
        visualMap: [{
          'show': false,
          'pieces': [{
            'gte':80,
            'lt': 100,
            'color': '#00EE00'
          }, {
            'gte':60,
            'lt': 80,
            'color': 'blue'
          },{
            'lt': 60,
            'gt': 0,
            'color': 'red'
         },{
            'lt': 1000,
            'gt': 800,
            'color': '#00EE00'
          },{
            'lt': 800,
            'gt': 600,
            'color': 'blue'
          },{
            'lt': 600,
            'gt': 100,
            'color': 'red'
          }]
        }],
        series: [{
          name: '个数',
          type: 'line',
          data: this.yData1,
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
  }
}
</script>
<style scoped>
  div#date{
    margin-left: 30%;
  }
  #main1,#main2,#main3{
    width:800px;
    height:300px;
    margin: 10px auto;
    padding: 20px;
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
    margin-right:100px;
    background-color: #FAFAFA;
    float: left;
    border-radius:20px
  }
  .internet-map{
    font-family: STXingkai;
    font-size: 30px;
    padding: 20px 0 0 20px;
  }
</style>
