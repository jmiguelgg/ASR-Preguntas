<template>
    <div class="ui container">
        <table class="ui celled table">
            <thead>
                <th>Reinicio</th>
                <th>IP</th>
                <th>Nivel</th>
                <th>Fecha</th>
            </thead>
            <tbody>
                <tr v-for="item in data" :key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.ip}}</td>
                    <td>{{item.nivel}}</td>
                    <td>{{item.fecha}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props:{
        data: {}
    }
}
</script>