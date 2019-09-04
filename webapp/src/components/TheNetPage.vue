<template>
  <div>
    <div class="clearfix">
      <div class="internet-map">
        <span>网络图</span>
      </div>
      <ul>
        <li class="ip-item"  @click="drawData">网络总览</li>
        <li class="ip-item"  @click="drawData1">10.10.20.241</li>
        <li class="ip-item"  @click="drawData2">10.10.20.242</li>
        <li class="ip-item"  @click="drawData3">10.10.20.243</li>
        <li class="ip-item"  @click="drawData4">10.10.20.244</li>
        <li class="ip-item"  @click="drawData5">10.10.20.245</li>
        <li class="ip-item"  @click="drawData6">10.10.20.246</li>
        <li class="ip-item"  @click="drawData7">10.10.20.247</li>
        <li class="ip-item"  @click="drawData8">10.10.20.248</li>
        <li class="ip-item"  @click="drawData9">10.10.20.249</li>
        <li class="ip-item"  @click="drawData10">10.10.20.250</li>
      </ul>
    </div>
    <div id="main"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  export default {
    name: "TheStatePage",
    data(){
      return {
        arr: [],
        arrs: [],
      }
    },
    mounted(){
      this.getPush();
      this.drawLine('main')
    },
    methods: {
      drawData(){
        this.arr = [];
        let sum4 = 0;
        for(let i=0;i<10;i++){
          for(let item in this.arrs){
            sum4 += this.arrs[item][i];
          }
          this.arr.push(sum4);
          sum4 = 0;
        }
        this.drawLine1("main");
      },
      drawData1(){
        this.arr = this.arrs[0];
        this.drawLine("main");
      },
      drawData2(){
        this.arr = this.arrs[1];
        this.drawLine("main");
      },
      drawData3(){
        this.arr = this.arrs[2];
        this.drawLine("main");
      },
      drawData4(){
        this.arr = this.arrs[3];
        this.drawLine("main");
      },
      drawData5(){
        this.arr = this.arrs[4];
        this.drawLine("main");
      },
      drawData6(){
        this.arr = this.arrs[5];
        this.drawLine("main");
      },
      drawData7(){
        this.arr = this.arrs[6];
        this.drawLine("main");
      },
      drawData8(){
        this.arr = this.arrs[7];
        this.drawLine("main");
      },
      drawData9(){
        this.arr = this.arrs[8];
        this.drawLine("main");
      },
      drawData10(){
        this.arr = this.arrs[9];
        this.drawLine("main");
      },
      getRandom(){
        return   Math.round(100 * Math.random())
      },
      getPush(){
        for(let i=0; i<=9; i++){
          this.arr = [];
          for(let i=0;i<=8;i++){
            if(this.arr.length <= 9){
              this.arr.push(this.getRandom());
            }
          }
          if(this.arrs.length < 10){
            this.arrs.push(this.arr)
          }
        }
        console.log(this.arrs)
      },
      drawLine1(id) {
        let myChart = echarts.init(document.getElementById(id));
        let data = [
          [0, 0, 1, this.arr[0]],
          [0, 1, 2, this.arr[1]],
          [0, 2, 3, this.arr[2]],
          [1, 0, 4, this.arr[3]],
          [1, 1, 5, this.arr[4]],
          [1, 2, 6, this.arr[5]],
          [2, 0, 7, this.arr[6]],
          [2, 1, 8, this.arr[7]],
          [2, 2, 9, this.arr[8]],
        ];
        let option = {
          title: {
            text: '矩阵图',
          },
          backgroundColor: '#fff',
          tooltip: {},
          xAxis: {
            type: 'category',
            //	name: '客户贡献度',
            data: ['左', '中', '右'],
            axisLine: {          //坐标轴轴线相关设置。
              show: true,         //是否显示坐标轴轴线。
              symbol: ['none', 'none'],  //轴线两边的箭头。
              // symbolSize: [10, 10],     //轴线两边的箭头的大小
              // symbolOffset: [0, 5]      //轴线两边的箭头的偏移
            },
            axisTick: {      //坐标轴刻度相关设置。
              show: false      //是否显示坐标轴刻度。
            },
            // axisLabel: {      //坐标轴刻度标签的相关设置。
            //   show: false,
            //   rotate: 0      //刻度标签旋转的角度
            // },
            // splitLine: {
            //   show: true,      //坐标轴在 grid 区域中的分隔线。
            //   interval: '4',    //坐标轴分隔线的显示间隔
            //   lineStyle: {     //分隔线样式，
            //     color: ['#333'],
            //     width: 1,
            //     type: 'solid'
            //   }
            // },
            // splitArea: {    //坐标轴在 grid 区域中的分隔区域，默认不显示
            //   show: true
            // }
          },
          yAxis: {
            type: 'category',
            data: ['下', '中', '上'],
            axisLine: {
              show: true,
              symbol: ['none', 'none'],
            },
            axisTick: {
              show: false
            },
          },
          visualMap: [{
            min: 0,
            max: 100,
            calculable: true,  //是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
            orient: 'vertical',  //如何放置 visualMap 组件，水平（'horizontal'）或者竖直（'vertical'）
            seriesIndex: 1,
            // left: '91%',
            bottom: 50,
          }],
          series: [{
            type: 'heatmap',
            data: data,
            tooltip: {
              formatter: function(o) {
                let arr = [
                  '房间名称：' + o.value[2] + '<br/>',
                  '用户数量：' + o.value[3]
                ];
                return arr.join('');
              }
            },
            itemStyle: {
              color: '#fff',
              borderColor: '#000',
              borderWidth: 2,
              emphasis: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          },{
            type: 'effectScatter',
            data: data,
            symbolSize: function(value){
              return value[3]/10
            },
            rippleEffect:{
              scale:6,
            },
            tooltip: {
              formatter: function(o) {
                let arr = [
                  '房间名称：' + o.value[2] + '<br/>',
                  '用户数量：' + o.value[3]
                ];
                return arr.join('');
              }
            },
          }]
        };
        myChart.setOption(option)
      },
      drawLine(id) {
        let myChart = echarts.init(document.getElementById(id));
        let data = [
          [0, 0, 1, this.arr[0]],
          [0, 1, 2, this.arr[1]],
          [0, 2, 3, this.arr[2]],
          [1, 0, 4, this.arr[3]],
          [1, 1, 5, this.arr[4]],
          [1, 2, 6, this.arr[5]],
          [2, 0, 7, this.arr[6]],
          [2, 1, 8, this.arr[7]],
          [2, 2, 9, this.arr[8]],
        ];
        let option = {
          title: {
            text: '矩阵图',
          },
          backgroundColor: '#fff',
          tooltip: {},
          xAxis: {
            type: 'category',
            //	name: '客户贡献度',
            data: ['左', '中', '右'],
            axisLine: {          //坐标轴轴线相关设置。
              show: true,         //是否显示坐标轴轴线。
              symbol: ['none', 'none'],  //轴线两边的箭头。
              // symbolSize: [10, 10],     //轴线两边的箭头的大小
              // symbolOffset: [0, 5]      //轴线两边的箭头的偏移
            },
            axisTick: {      //坐标轴刻度相关设置。
              show: false      //是否显示坐标轴刻度。
            },
            // axisLabel: {      //坐标轴刻度标签的相关设置。
            //   show: false,
            //   rotate: 0      //刻度标签旋转的角度
            // },
            // splitLine: {
            //   show: true,      //坐标轴在 grid 区域中的分隔线。
            //   interval: '4',    //坐标轴分隔线的显示间隔
            //   lineStyle: {     //分隔线样式，
            //     color: ['#333'],
            //     width: 1,
            //     type: 'solid'
            //   }
            // },
            // splitArea: {    //坐标轴在 grid 区域中的分隔区域，默认不显示
            //   show: true
            // }
          },
          yAxis: {
            type: 'category',
            data: ['下', '中', '上'],
            axisLine: {
              show: true,
              symbol: ['none', 'none'],
            },
            axisTick: {
              show: false
            },
          },
          visualMap: [{
            min: 0,
            max: 100,
            calculable: true,  //是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
            orient: 'vertical',  //如何放置 visualMap 组件，水平（'horizontal'）或者竖直（'vertical'）
            seriesIndex: 1,
            // left: '91%',
            bottom: 50,
          }],
          series: [{
            type: 'heatmap',
            data: data,
            tooltip: {
              formatter: function(o) {
                let arr = [
                  '房间名称：' + o.value[2] + '<br/>',
                  '用户数量：' + o.value[3]
                ];
                return arr.join('');
              }
            },
            itemStyle: {
              color: '#fff',
              borderColor: '#000',
              borderWidth: 2,
              emphasis: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          },{
            type: 'effectScatter',
            data: data,
            symbolSize: function(value){
              return value[3]/2
            },
            rippleEffect:{
              scale:6,
            },
            tooltip: {
              formatter: function(o) {
                let arr = [
                  '房间名称：' + o.value[2] + '<br/>',
                  '用户数量：' + o.value[3]
                ];
                return arr.join('');
              }
            },
          }]
        };
        myChart.setOption(option)
      },
    }
  }
</script>

<style scoped>
  #main{
    width:800px;
    height:800px;
    padding:0 40px;
    margin: 0 auto;
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
