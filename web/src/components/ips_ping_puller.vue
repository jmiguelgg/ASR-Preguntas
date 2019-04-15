<template>
    <div class="ui container">
        <table class="ui celled table">
            <thead>
                <th>Direccion IP</th>
                <th>Numero de Pings</th>
                <th>¿Respondió?</th>
                <th>Ping respuesta</th>
            </thead>
            <tbody>
                <tr :class="[!item.response? 'error':'']" v-for="item in data" :key="item.ip">
                    <td>{{item.ip}}</td>
                    <td>{{item.numPingTotal}}</td>
                    <td>{{item.response}}</td>
                    <td>{{item.ping}}</td>
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
