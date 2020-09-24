var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        window.dataList = [{
            name: "南海诸岛",
            value: [0,1,2],
            project985: 12
        }, {
            name: '北京',
            value: 54,
            project985: 210

        }, {
            name: '天津',
            value: 13,
            project985: 1200

        }, {
            name: '上海',
            value: 40,
            project985: 10

        }, {
            name: '重庆',
            value: 75,
            project985: 12

        }, {
            name: '河北',
            value: 13,
            project985: 12

        }, {
            name: '河南',
            value: 83,
            project985: 12

        }, {
            name: '云南',
            value: 11,
            project985: 12

        }, {
            name: '辽宁',
            value: 19,
            project985: 12

        }, {
            name: '黑龙江',
            value: 15,
            project985: 12

        }, {
            name: '湖南',
            value: 69,
            project985: 12

        }, {
            name: '安徽',
            value: 60,
            project985: 12

        }, {
            name: '山东',
            value: 39,
            project985: 12

        }, {
            name: '新疆',
            value: 4,
            project985: 12

        }, {
            name: '江苏',
            value: 31,
            project985: 12

        }, {
            name: '浙江',
            value: 104,
            project985: 120

        }, {
            name: '江西',
            value: 36,
            project985: 120

        }, {
            name: '湖北',
            value: 1052,
            project985: 120

        }, {
            name: '广西',
            value: 33,
            project985: 120

        }, {
            name: '甘肃',
            value: 7,
            project985: 120

        }, {
            name: '山西',
            value: 9,
            project985: 120

        }, {
            name: '内蒙古',
            value: 7,
            project985: 120

        }, {
            name: '陕西',
            value: 22,
            project985: 120

        }, {
            name: '吉林',
            value: 4,
            project985: 120

        }, {
            name: '福建',
            value: 18,
            project985: 120

        }, {
            name: '贵州',
            value: 5,
            project985: 120

        }, {
            name: '广东',
            value: 98,
            project985: 120

        }, {
            name: '青海',
            value: 1,
            project985: 120

        }, {
            name: '西藏',
            value: 0,
            project985: 120

        }, {
            name: '四川',
            value: [44,72],
            project985: 120

        }, {
            name: '宁夏',
            value: 4,
            project985: 120

        }, {
            name: '海南',
            value: 22,
            project985: 120

        }, {
            name: '台湾',
            value: 3,
            project985: 120

        }, {
            name: '香港',
            project985: 120,
            value: 5
        }, {
            name: '澳门',
            project985: 120,
            value: 5
        }];
        option = {
            tooltip: {
                triggerOn: "click",
                formatter: function(params) {
                    var myseries=option.series
                    var res=params.name+"\n985数量"
                    for (var i=0;i<myseries[0].data.length;i=i+1){
                        if(myseries[0].data[i].name==params.name){
                            return res+myseries[0].data[i].project985;
                        }
                    }

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
                    gt: 100,
                    label: "> 100 人",
                    color: "#04477C"
                }, {
                    gte: 10,
                    lte: 100,
                    label: "10 - 100 人",
                    color: "#065FB9"
                }, {
                    gte: 1,
                    lt: 10,
                    label: "1 - 9 人",
                    color: "#049FF1"
                }, {
                    gt: 0,
                    lt: 1,
                    label: "疑似",
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
        myChart.setOption(option);