
//var myChart = echarts.init(document.getElementById('main'));

var mapChart = echarts.init(document.querySelector(".mapbox"));
        // 指定图表的配置项和数据
        window.dataList = [{
            name: "河南",
            value: 2,
            project985: 0,
            project211: 1,
            doubleTop: 2
        },{
            name: "天津",
            value: 5,
            project985: 2,
            project211: 1,
            doubleTop: 5
        },{
            name: "海南",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "江苏",
            value: 15,
            project985: 2,
            project211: 9,
            doubleTop: 15
        },{
            name: "陕西",
            value: 8,
            project985: 3,
            project211: 5,
            doubleTop: 8
        },{
            name: "青海",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "澳门",
            value: 0,
            project985: 0,
            project211: 0,
            doubleTop: 0
        },{
            name: "香港",
            value: 0,
            project985: 0,
            project211: 0,
            doubleTop: 0
        },{
            name: "上海",
            value: 14,
            project985: 4,
            project211: 6,
            doubleTop: 14
        },{
            name: "山西",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "江西",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "黑龙江",
            value: 4,
            project985: 1,
            project211: 3,
            doubleTop: 4
        },{
            name: "浙江",
            value: 3,
            project985: 1,
            project211: 0,
            doubleTop: 3
        },{
            name: "贵州",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "西藏",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "山东",
            value: 3,
            project985: 2,
            project211: 1,
            doubleTop: 3
        },{
            name: "河北",
            value: 2,
            project985: 0,
            project211: 2,
            doubleTop: 2
        },{
            name: "辽宁",
            value: 4,
            project985: 2,
            project211: 2,
            doubleTop: 4
        },{
            name: "福建",
            value: 2,
            project985: 1,
            project211: 1,
            doubleTop: 2
        },{
            name: "新疆",
            value: 2,
            project985: 0,
            project211: 2,
            doubleTop: 2
        },{
            name: "湖北",
            value: 7,
            project985: 2,
            project211: 5,
            doubleTop: 7
        },{
            name: "湖南",
            value: 4,
            project985: 3,
            project211: 1,
            doubleTop: 4
        },{
            name: "吉林",
            value: 3,
            project985: 1,
            project211: 2,
            doubleTop: 3
        },{
            name: "广东",
            value: 5,
            project985: 2,
            project211: 2,
            doubleTop: 5
        },{
            name: "北京",
            value: 29,
            project985: 8,
            project211: 18,
            doubleTop: 29
        },{
            name: "台湾",
            value: 0,
            project985: 0,
            project211: 0,
            doubleTop: 0
        },{
            name: "重庆",
            value: 2,
            project985: 1,
            project211: 1,
            doubleTop: 2
        },{
            name: "安徽",
            value: 3,
            project985: 1,
            project211: 2,
            doubleTop: 3
        },{
            name: "广西",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "甘肃",
            value: 1,
            project985: 1,
            project211: 0,
            doubleTop: 1
        },{
            name: "宁夏",
            value: 0,
            project985: 0,
            project211: 1,
            doubleTop: 0
        },{
            name: "云南",
            value: 0,
            project985: 0,
            project211: 1,
            doubleTop: 0
        },{
            name: "四川",
            value: 8,
            project985: 2,
            project211: 3,
            doubleTop: 8
        },{
            name: "内蒙古",
            value: 1,
            project985: 0,
            project211: 1,
            doubleTop: 1
        },{
            name: "南海诸岛",
            value: 0,
            project985: 0,
            project211: 0,
            doubleTop: 0
        }];
        option = {
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
                left: 26,
                bottom: 40,
                showLabel: !0,
                text: ["高", "低"],
                pieces: [{
                    gt: 20,
                    //label: "> 100 人",
                    color: "#04477C"
                }, {
                    gte: 10,
                    lte: 20,
                    //label: "10 - 100 人",
                    color: "#065FB9"
                }, {
                    gte: 1,
                    lt: 10,
                    //label: "1 - 9 人",
                    color: "#049FF1"
                }, {
                    gt: 0,
                    lt: 1,
                    //label: "疑似",
                    color: "#CBF3FB"
                }, {
                    value: 0,
                    color: "#ffffff"
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
                top: 120,
                label: {
                    normal: {
                        show: !0,
                        fontSize: "14",
                        color: "rgba(0,0,0,0.7)"
                    }
                },
                itemStyle: {
                    normal: {
                        //shadowBlur: 50,
                        //shadowColor: 'rgba(0, 0, 0, 0.2)',
                        borderColor: "rgba(0, 0, 0, 0.4)"
                    },
                    emphasis: {
                        areaColor: "#f2d5ad",
                        shadowOffsetX: 0,
                        shadowOffsetY: 0,
                        borderWidth: 0
                    }
                }
            },
            series: [{
                name: "985/211大学数",
                type: "map",
                geoIndex: 0,
                data: window.dataList
            }]
        }; // 使用刚指定的配置项和数据显示图表。
        mapChart.setOption(option);