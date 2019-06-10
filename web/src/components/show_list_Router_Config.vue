<template>
    <div class="ui container">
        <table class="ui celled table">
            <thead>
                <th>ID</th>
                <th>Fecha</th>
                <th>Hostname</th>
                <th>Show</th>
            </thead>
            <tbody>
                <tr v-for="item in data" :key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.fecha}}</td>
                    <td>{{item.data.hostname}}</td>
                    <td>
                        <input type="button" class="ui teal button" @click="showConfig(item.data)" value="Show">
                    </td>
                </tr>
            </tbody>
        </table>
        <ShowRouterConfig :data="dataConf"/>
    </div>
</template>

<script>
import ShowRouterConfig from '@/components/show_Router_Config';
export default {
    props:{
        data: {}
    },
    components:{
        ShowRouterConfig
    },
    methods:{
        showConfig(data){
            this.dataConf = data
        }
    },
    data(){
        return{
            dataConf: {}
        }
    }
}
</script>