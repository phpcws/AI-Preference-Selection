(function() {
    var myChart = echarts.init(document.querySelector(".map"));

    // 指定图表的配置项和数据
    window.dataList = [{
        name: "南海诸岛",
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '北京',
        value: 28,
        project985: 10,
        project211: 18,
        doubleTop: 18
    }, {
        name: '天津',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '上海',
        value: 15,
        project985: 5,
        project211: 10,
        doubleTop: 10
    }, {
        name: '重庆',
        value: 3,
        project985: 1,
        project211: 2,
        doubleTop: 2
    }, {
        name: '河北',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '河南',
        value: 1,
        project985: 0,
        project211: 1,
        doubleTop: 1
    }, {
        name: '云南',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '辽宁',
        value: 4,
        project985: 1,
        project211: 3,
        doubleTop: 3
    }, {
        name: '黑龙江',
        value: 2,
        project985: 0,
        project211: 2,
        doubleTop: 2
    }, {
        name: '湖南',
        value: 5,
        project985: 2,
        project211: 3,
        doubleTop: 3
    }, {
        name: '安徽',
        value: 4,
        project985: 1,
        project211: 3,
        doubleTop: 3
    }, {
        name: '山东',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '新疆',
        value: 2,
        project985: 0,
        project211: 2,
        doubleTop: 2
    }, {
        name: '江苏',
        value: 9,
        project985: 2,
        project211: 7,
        doubleTop: 7
    }, {
        name: '浙江',
        value: 104,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '江西',
        value: 36,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '湖北',
        value: 1052,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '广西',
        value: 33,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '甘肃',
        value: 7,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '山西',
        value: 9,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '内蒙古',
        value: 7,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '陕西',
        value: 22,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '吉林',
        value: 4,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '福建',
        value: 18,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '贵州',
        value: 5,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '广东',
        value: 98,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '青海',
        value: 1,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '西藏',
        value: 0,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '四川',
        value: 4,
        project985: 2,
        project211: 2,
        doubleTop: 2
    }, {
        name: '宁夏',
        value: 4,
        project985: 120,
        project211: 0,
        doubleTop: 2
    }, {
        name: '海南',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '台湾',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '香港',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }, {
        name: '澳门',
        value: 0,
        project985: 0,
        project211: 0,
        doubleTop: 0
    }];
    var option = {
        tooltip: {
            triggerOn: "click",
            formatter: function(e, t, n) {
                return e.name +
                    "<br />" + "985大学数：" + e.data['project985'] +
                    "<br />" + "211大学数：" + e.data['project211'] +
                    "<br />" + "双一流大学数：" + e.data['doubleTop']
            }
        },
        visualMap: {
            min: 0,
            max: 1000,
            left: 30,
            bottom: 50,
            showLabel: !0,
            text: ["高", "低"],
            pieces: [{
                gt: 20,
                color: "rgb(77, 144, 185)"
            }, {
                gt: 10,
                lte: 20,
                color: "rgb(104, 166, 204)"
            }, {
                gt: 5,
                lte: 10,
                color: "rgb(129, 188, 224)"
            }, {
                gte: 1,
                lte: 5,
                color: "rgb(179, 221, 248)"
            }, {
                value: 0,
                color: "rgb(208, 234, 252)"
            }],
            show: !0
        },
        geo: {
            map: "china",
            roam: !1,
            scaleLimit: {
                min: 1,
                max: 2
            },
            zoom: 1.23,
            top: 100,
            label: {
                normal: {
                    show: true,
                    fontSize: "12",
                    color: "#500404"
                }
            },
            itemStyle: {
                normal: {
                    //shadowBlur: 50,
                    shadowColor: 'rgba(0, 0, 0, 0.6)',
                    borderColor: "rgba(0, 0, 0, 0.3)"
                },
                emphasis: {
                    areaColor: "rgba(252, 157, 157,0.9)",
                    shadowOffsetX: 2,
                    shadowOffsetY: 1,
                    borderWidth: 0
                }
            }
        },
        series: [{
            name: "985/211大学数",
            type: "map",
            geoIndex: 0,
            data: dataList
        }]
    }; // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
})();