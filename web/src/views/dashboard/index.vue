<template>
  <div class="Echarts">
    <div id="main" style="width: 600px;height: 400px;"></div>
  </div>
</template>
 




<script>

import axios from 'axios';
console.log("21312")
export default {
  name: 'Echarts',
  methods: {
    myEcharts(){

      var myChart = this.$echarts.init(document.getElementById('main'));
      //配置图表
      function randomData() {
        now = new Date(+now + oneDay);
        value = value + Math.random() * 21 - 10;
        return {
          name: now.toString(),
          value: [
            [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'),
            Math.round(value)
          ]
        };
      }
      let data = [];
      let now = new Date(1997, 9, 3);
      let oneDay = 24 * 3600 * 1000;
      let value = Math.random() * 1000;
      for (var i = 0; i < 1000; i++) {
        data.push(randomData());
      }
      var option = {
        title: {
            text: 'Dynamic Data & Time Axis'
          },
          tooltip: {
            trigger: 'axis',
            formatter: function (params) {
              params = params[0];
              var date = new Date(params.name);
              return (
                date.getDate() +
                '/' +
                (date.getMonth() + 1) +
                '/' +
                date.getFullYear() +
                ' : ' +
                params.value[1]
              );
            },
            axisPointer: {
              animation: false
            }
          },
          xAxis: {
            type: 'time',
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            boundaryGap: [0, '50%'],
            splitLine: {
              show: false
            }
          },
          series: [
            {
              name: 'Fake Data',
              type: 'line',
              showSymbol: false,
              data: data
            }
          ]
    };
      setInterval(function () {
        for (var i = 0; i < 10; i++) {
          data.shift();
          data.push(randomData());
        }
        myChart.setOption({
          series: [
            {
              data: data
            }
          ]
        });
      }, 1000);
      myChart.setOption(option);
    },
    getData() {
      // 设置对应python的接口，这里使用的是localhost:5000
      const path = 'http://127.0.0.1:5000/server/testget';
      // 这里要使用 res =>表示返回的数据
      console.log(path);
      axios.get(path).then(res => {
        // 这里服务器返回response为一个json对象
        // 通过.data来访返回的数据，然后在通过.变量名进行访问
        // 可以直接通过response.data取得key-value
        // var msg = res.data.msg;
        // this.serverResponse = msg; // 因为不能直接使用this作为指针，因此在这之前将this赋给了then指针
        // alter('Success' + response.status + ',' + response.data + ',' + msg); // 成功后显示提示
        console.log("get success");
      }).catch(error => {
        console.error(error);
      });
    }
  },
  mounted(){
    this.myEcharts(), this.getData();
  }
}
</script>
 
<style>
 
</style>