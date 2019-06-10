<template>
    <div class="ui container">
        <table class="ui celled table">
            <thead>
                <th>IP</th>
                <th>Fecha</th>
                <th>Hostname</th>
                <th>Información</th>
            </thead>
            <tbody>
                <tr :class="[item.info == '' ? 'error':'']" v-for="item in data" :key="item.ip">
                    <td>{{item.ip}}</td>
                    <td>{{item.fecha}}</td>
                    <td>{{item.hostname}}</td>
                    <td>{{item.info}}</td>
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