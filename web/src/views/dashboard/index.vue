
<template>
  <div class="Echarts">
    <div id="button" style="left: 150px; top: 10px; ">
    <el-button type="primary" @click="onSubmit">Create</el-button>
    <el-button @click="onCancel">Cancel</el-button>
    </div>
    <div id="main" style="width: 100%;height: 800%; top: 50px; "></div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Echarts',
  methods: {
    async getData() {
      // 设置对应python的接口，这里使用的是localhost:5000
      const path = 'http://127.0.0.1:5000/server/gettestdata';
      // 这里要使用 res =>表示返回的数据
      var data;
      await axios.get(path, {params:{data_id : 1}}).then(res => {
        data = res.data;
        }).catch(error => {
          console.error(error);
      });
      return data;
    },
    async testmulti2() {
      var myChart = this.$echarts.init(document.getElementById('main'));
      var option;
      var res_data = await this.getData();
      res_data = res_data.data;

      const grids = [];
      const xAxes = [];
      const yAxes = [];
      const series = [];
      const titles = [];
      let count = 0;
      console.log("1", res_data[0]);
      let ncount = res_data[1].length / 100;
      for(let i = 0; i < res_data.length; i++){
        var data = [];
        var data2 = [];
        for (var j = 0; j < ncount; j++) {
          var x = j + 1;
          var y = res_data[count][j * 100] ;
          data.push([x * 100, y]);
          data2.push([x * 100, y * 1.3]);
          // data2.push([x * 100, y * (1 + (Math.random() - 0.5) / 5)]);
        }
        var data = [];
        var data2 = [];

        // var data = res_data[count];
        // console.log(data);
        grids.push({
          show: true,
          borderWidth: 0,
        });
        xAxes.push({
          type: 'value',
          show: true,
          min: 0,
          max: ncount * 100,
          gridIndex: count,
        });
        yAxes.push({
          type: 'value',
          show: true,
          gridIndex: count,
          // 调整y轴标签长度
          axisLabel: {
              color: '#444343',
              // 设置y轴的单位自适应调整
              formatter: function (value, index) {
                  var value
                  if (value >= 1000 && value < 10000) {
                      value = value / 1000 + 'k'
                  } else if (value >= 10000) {
                      value = value / 10000 + 'M'
                  } else if (value < 1000) {
                      value = value
                  }
                  return value
              },
              fontSize : 12,
          },
          splitNumber: 3,
        });
        series.push({
          name: count,
          type: 'line',
          xAxisIndex: count,
          yAxisIndex: count,
          data: data,
          showSymbol: false,
          animationDuration: 10000,
          animationThreshold: 200000,
          animationDurationUpdate: 10000,
          lineStyle: {

          },
        },{
          name: count + " predicted",
          type: 'line',
          xAxisIndex: count,
          yAxisIndex: count,
          data: data2,
          showSymbol: false,
          animationDuration: 5000,
          // 超过animationThreshold就不画图了
          animationThreshold: 200000,
          animationDurationUpdate: 10000,
          lineStyle: {
            type : 'dotted',
          },
        });
        titles.push({
          textAlign: 'center',
          text: count,
          textStyle: {
            fontSize: 12,
            fontWeight: 'normal'
          }
        });
        count++;
      }
      // var rowNumber = Math.ceil(Math.sqrt(count));
      var rowNumber = 4;
      var colNumber = 3;
      grids.forEach(function (grid, idx) {
        grid.left = ((idx % colNumber) / colNumber) * 100 + 2.5 + '%';
        // console.log(grid.left);
        grid.top = (Math.floor(idx / colNumber) / rowNumber) * 100 + 1.5 + '%';
        grid.width = (1 / colNumber) * 100 - 5 + '%';
        grid.height = (1 / rowNumber) * 100 - 10 + '%';
        console.log(grid.top, grid.left);
      });
      option = {
        tooltip: {
          trigger: 'axis',
          textStyle : {fontSize : 4},
          // axisPointer: {
          //   type: 'cross'
          // show : true,
          },
        title: titles.concat([
          {
            text: 'TTT',
            top: 'bottom',
            left: 'center'
          }
        ]),
        grid: grids,
        xAxis: xAxes,
        yAxis: yAxes,
        series: series,
        toolbox: {
          right: 10,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            xAxisIndex : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,],
          }
        ],
      };

      option && myChart.setOption(option);
      console.log("testclick");
      myChart.on('click', (params)=> {
        console.log("test log params");
        console.log(params);
      });
    },
    async testmulti() {
      var myChart = this.$echarts.init(document.getElementById('main'));
      var option;
      var res_data = await this.getData();
      res_data = res_data.data;

      const grids = [];
      const xAxes = [];
      const yAxes = [];
      const series = [];
      const titles = [];
      let count = 0;
      console.log("1", res_data[0]);
      let ncount = res_data[1].length;
      for(let i = 0; i < res_data.length; i++){
        var data = [];
        var data2 = [];
        for (var j = 0; j < ncount; j++) {
          var x = j + 1;
          var y = res_data[count][j] ;
          data.push([x , y]);
          
          data2.push([x, y * 1.1]);
        }
        // var data = [];
        // var data2 = [];
        // var data = res_data[count];
        // console.log(data);
        grids.push({
          show: true,
          borderWidth: 0,
        });
        xAxes.push({
          type: 'value',
          show: true,
          min: 0,
          max: ncount,
          gridIndex: count
        });
        yAxes.push({
          type: 'value',
          show: true,
          gridIndex: count,
          // 调整y轴标签长度
          axisLabel: {
              color: '#444343',
              // 设置y轴的单位自适应调整
              formatter: function (value, index) {
                  var value
                  if (value >= 1000 && value < 10000) {
                      value = value / 1000 + 'k'
                  } else if (value >= 10000) {
                      value = value / 10000 + 'M'
                  } else if (value < 1000) {
                      value = value
                  }
                  return value
              },
              fontSize : 12,
          },
          splitNumber: 3,
        });
        series.push({
          name: count,
          type: 'line',
          xAxisIndex: count,
          yAxisIndex: count,
          data: data,
          showSymbol: false,
          animationDuration: 10000,
          animationThreshold: 200000,
          // animationDurationUpdate: 10000,
          lineStyle: {
            // type: 'dotted'
          },
        },{
          name: count + " predicted",
          type: 'line',
          xAxisIndex: count,
          yAxisIndex: count,
          data: data2,
          showSymbol: false,
          animationDuration: 5000,
          animationThreshold: 200000,
          // animationDurationUpdate: 10000,
          lineStyle: {
            // type: 'dashed'
            type : 'dotted',
          },
        });
        titles.push({
          textAlign: 'center',
          text: count,
          textStyle: {
            fontSize: 12,
            fontWeight: 'normal'
          }
        });
        count++;
      }
      // var rowNumber = Math.ceil(Math.sqrt(count));
      var rowNumber = 4;
      var colNumber = 3;
      // grids.forEach(function (grid, idx) {
      //   // grid.left = ((idx % rowNumber) / rowNumber) * 100 + 0.5 + '%';
      //   // grid.top = 20 * (idx) + '%';
      //   grid.top = (Math.floor(idx / 1) / rowNumber) * 100 + 1.5 + '%';
      //   console.log(Math.floor(idx / 1), grid.top);
      //   grid.width = '100%';
      //   // grid.height = 15 * (idx) + '%';
      //   grid.height = (1 / rowNumber) * 100 - 5 + '%';
      // });

      // grids.forEach(function (grid, idx) {
      //   // grid.left = ((idx % rowNumber) / rowNumber) * 100 + 0.5 + '%';
      //   // grid.top = 20 * (idx) + '%';
      //   rowNumber = 5;
      //   grid.top = (Math.floor(idx / rowNumber) / rowNumber) * 100 + 1.5 + '%';
      //   console.log(Math.floor(idx / rowNumber), grid.top);
      //   grid.width = '40%';
      //   // grid.height = 15 * (idx) + '%';
      //   grid.height = (1 / rowNumber) * 100 - 5 + '%';
      // });
      grids.forEach(function (grid, idx) {
        grid.left = ((idx % colNumber) / colNumber) * 100 + 2.5 + '%';
        // console.log(grid.left);
        grid.top = (Math.floor(idx / colNumber) / rowNumber) * 100 + 1.5 + '%';
        
        grid.width = (1 / colNumber) * 100 - 5 + '%';
        grid.height = (1 / rowNumber) * 100 - 10 + '%';
        console.log(grid.top, grid.left);
        // titles[idx].left = parseFloat(grid.left) + parseFloat(grid.width) / 2 + '%';
        // titles[idx].top = parseFloat(grid.top) + '%';
      });
      option = {
        tooltip: {
          trigger: 'axis',
          textStyle : {fontSize : 4},
          // axisPointer: {
          //   type: 'cross'
          // show : true,
          },
        title: titles.concat([
          {
            text: 'TTT',
            top: 'bottom',
            left: 'center'
          }
        ]),
        grid: grids,
        xAxis: xAxes,
        yAxis: yAxes,
        series: series,
        toolbox: {
          right: 10,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            xAxisIndex : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,],
          }
        ],
      };
      myChart.clear();
      option && myChart.setOption(option);
      
      console.log("testclick");
      myChart.on('click', (params)=> {
        console.log("test log params");
        console.log(params);
      });
    },
    onSubmit() {
      this.$message('Strat!');
      this.testmulti();
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    }
  },
  mounted(){
    this.testmulti2();
  }
}
</script>
 
<style>
 
</style>