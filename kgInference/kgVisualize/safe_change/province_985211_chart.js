var province_985211_chart=echarts.init(document.querySelector(".chartbox"));
var datalist=[]
option = {
    title: {
        text: '\n各省市对应985211数量',//避免与后面图标重叠
        subtext: ''
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['985', '211','双一流']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
    },
    yAxis: {
        type: 'category',
        data:['河南省', '天津市', '海南省', '江苏省', '陕西省', '青海省', '澳门特别行政区', '香港特别行政区', '上海市', '山西省', '江西省', '黑龙江省', '浙江省', '贵州省', '西藏自治区', '山东省', '河北省', '辽宁省', '福建省', '新疆维吾尔自治区', '湖北省', '湖南省', '吉林省', '广东省', '北京市', '台湾省', '重庆市', '安徽省', '广西壮族自治区', '甘肃省', '宁夏回族自治区', '云南省', '四川省', '内蒙古自治区']

    },
    series: [
        {
            name: '985',
            type: 'bar',
            data: [0, 2, 0, 2, 3, 0, 0, 0, 4, 0, 0, 1, 1, 0, 0, 2, 0, 2, 1, 0, 2, 3, 1, 2, 8, 0, 1, 1, 0, 1, 0, 0, 2, 0]
        },
        {
            name: '211',
            type: 'bar',
            data: [1, 1, 1, 9, 5, 1, 0, 0, 6, 1, 1, 3, 0, 1, 1, 1, 2, 2, 1, 2, 5, 1, 2, 2, 18, 0, 1, 2, 1, 0, 1, 1, 3, 1]
        },
        {
            name: '双一流',
            type: 'bar',
            data: [2, 5, 1, 15, 8, 1, 0, 0, 14, 1, 1, 4, 3, 1, 1, 3, 2, 4, 2, 2, 7, 4, 3, 5, 29, 0, 2, 3, 1, 1, 0, 0, 8, 1]
        }
    ]
};
province_985211_chart.setOption(option)