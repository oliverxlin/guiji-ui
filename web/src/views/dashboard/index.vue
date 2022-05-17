<template>
  <div class="Echarts">
    <div id="main" style="width: 600px;height: 400px;"></div>
  </div>
</template>

<script>

import axios from 'axios';
// import $ from 'jquery';
console.log("test")
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
    },
    test() {
      var myChart = this.$echarts.init(document.getElementById('main'));
      var option;
      // prettier-ignore
      const data = [["2000-06-05", 116], ["2000-06-06", 129], ["2000-06-07", 135], ["2000-06-08", 86], ["2000-06-09", 73], ["2000-06-10", 85], ["2000-06-11", 73], ["2000-06-12", 68], ["2000-06-13", 92], ["2000-06-14", 130], ["2000-06-15", 245], ["2000-06-16", 139], ["2000-06-17", 115], ["2000-06-18", 111], ["2000-06-19", 309], ["2000-06-20", 206], ["2000-06-21", 137], ["2000-06-22", 128], ["2000-06-23", 85], ["2000-06-24", 94], ["2000-06-25", 71], ["2000-06-26", 106], ["2000-06-27", 84], ["2000-06-28", 93], ["2000-06-29", 85], ["2000-06-30", 73], ["2000-07-01", 83], ["2000-07-02", 125], ["2000-07-03", 107], ["2000-07-04", 82], ["2000-07-05", 44], ["2000-07-06", 72], ["2000-07-07", 106], ["2000-07-08", 107], ["2000-07-09", 66], ["2000-07-10", 91], ["2000-07-11", 92], ["2000-07-12", 113], ["2000-07-13", 107], ["2000-07-14", 131], ["2000-07-15", 111], ["2000-07-16", 64], ["2000-07-17", 69], ["2000-07-18", 88], ["2000-07-19", 77], ["2000-07-20", 83], ["2000-07-21", 111], ["2000-07-22", 57], ["2000-07-23", 55], ["2000-07-24", 60]];
      const dateList = data.map(function (item) {
        return item[0];
      });
      const valueList = data.map(function (item) {
        return item[1];
      });
      let xlist= [];
      for(let i = 1,len=200;i<=100;i++){xlist.push(i)};
      let ylist1 = [];
      for(let i = 1,len=200;i<=100;i++){ylist1.push(Math.random() * 10)};
      let ylist2 = [];
      for(let i = 1,len=200;i<=100;i++){ylist2.push(Math.random() * 10)};
      option = {
        // Make gradient line here
        animationDuration: 10000,
        // visualMap: [
        //   {
        //     show: false,
        //     type: 'continuous',
        //     seriesIndex: 0,
        //     min: 0,
        //     max: 100
        //   },
        //   {
        //     show: false,
        //     type: 'continuous',
        //     seriesIndex: 1,
        //     dimension: 0,
        //     min: 0,
        //     max: 100
        //   },

        // ],
        title: [
          {
            top: '8%',
            left: 'center',
            text: 'test p 1'
          },
          {
            top: '52%',
            left: 'center',
            text: 'test p 2'
          },
        ],
        tooltip: {
          trigger: 'axis'
        },
        xAxis: [
          {
            data: xlist
          },
          {
            data: xlist,
            gridIndex: 1
          },
        ],
        yAxis: [
          {},
          {
            gridIndex: 1
          }
        ],
        grid: [
          {
            bottom: '60%'
          },
          {
            top: '60%'
          },
        ],
        series: [
          {
            type: 'line',
            showSymbol: false,
            data: ylist1
          },
          {
            type: 'line',
            showSymbol: false,
            data: ylist2,
            xAxisIndex: 1,
            yAxisIndex: 1
          },
          // {
          //   type: 'line',
          //   showSymbol: false,
          //   data: ylist2,
          //   xAxisIndex: 1,
          //   yAxisIndex: 1
          // },
        ]
      };

      option && myChart.setOption(option);

    }
  },
  mounted(){
    this.test();

    // this.getData()
  }
}
</script>
 
<style>
 
</style>