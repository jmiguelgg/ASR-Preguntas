<template>
    <div class="ui container segment">
        <div id="chart">
            <apexchart type="bar" height="350" :options="chartOptions" :series="series">
            </apexchart>
        </div>
    </div>
</template>

<script>
export default {
    props:{
        data: []
    },
    /*watch:{
        data: function(datos){
            let tmp1 = []
            let tmp2 = []
            for (const elem in datos) {
                tmp1.push(datos[elem].hostname)
                tmp2.push(datos[elem].porcentaje)
            }
            this.chartOptions.xaxis.categories = tmp1
            this.series.data = tmp2
        }
    },*/
    mounted(){
        let tmp1 = []
        let tmp2 = []
        for (const elem in this.data) {
            tmp1.push(this.data[elem].hostname)
            tmp2.push(this.data[elem].porcentaje)
        }
        this.chartOptions.xaxis.categories = tmp1
        this.series[0].data = tmp2
    },
    data(){
        return{
            series: [{
                name: 'Servings',
                data: []
            }],
            chartOptions: {
                annotations: {
                    points: [{
                        x: 'Bananas',
                        seriesIndex: 0,
                        label: {
                            borderColor: '#775DD0',
                            offsetY: 0,
                            style: {
                                color: '#fff',
                                background: '#775DD0',
                            },
                            text: 'Bananas are good',
                        }
                    }]
                },
                chart: {
                    height: 350,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                        columnWidth: '50%',
                        endingShape: 'rounded'	
                    }
                },
                dataLabels: {
                    enabled: true
                },
                stroke: {
                    width: 2
                },
                grid: {
                    row: {
                        colors: ['#fff', '#f2f2f2']
                    }
                },
                xaxis: {
                    labels: {
                        rotate: -45
                    },
                    categories: [],
                },
                yaxis: {
                    title: {
                        text: 'Servings',
                    },
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'light',
                        type: "horizontal",
                        shadeIntensity: 0.25,
                        gradientToColors: undefined,
                        inverseColors: true,
                        opacityFrom: 0.85,
                        opacityTo: 0.85,
                        stops: [50, 0, 100]
                    },
                }
            }
        }
    }
}
</script>
