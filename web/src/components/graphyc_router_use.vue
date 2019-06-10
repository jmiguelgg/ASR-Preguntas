<template>
    <div class="ui container segment">
        <div id="chart">
            <apexchart type="area" height="350" :options="chartOptions" :series="series">
            </apexchart>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            series: [{
                name: 'series1',
                data: [31, 40, 28, 51, 42, 109, 100]
            },
            {
                name: 'series2',
                data: [11, 32, 45, 32, 34, 52, 41]
            },
            {
                name: 'series3',
                data: [21, 12, 45, 16, 37, 56, 150]
            }
            ],
            chartOptions: {
                dataLabels: {
                    enabled: true
                },
                stroke: {
                    curve: 'smooth'
                },
                xaxis: {
                    type: 'datetime',
                    categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00",
                    "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00",
                    "2018-09-19T06:30:00"
                    ],
                },
                tooltip: {
                    x: {
                        format: 'dd/MM/yy HH:mm'
                    },
                }
            }
        }
    }
}
</script>
