<template>
    <div class="ui container">
        <table class="ui celled table">
            <thead>
                <th>ID</th>
                <th>Nombre</th>
                <th>Show</th>
            </thead>
            <tbody>
                <tr v-for="item in data" :key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.nombre}}</td>
                    <td>
                        <input type="button" class="ui teal button" @click="showConfig(item.data)" value="Show">
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="ui container segment">
            <p>{{this.dataPrint}}</p>
        </div>
    </div>
</template>

<script>
export default {
    props:{
        data: {}
    },
    methods:{
        showConfig(data){
            this.dataPrint = data
        }
    },
    data(){
        return{
            dataPrint: ''
        }
    }
}
</script>
