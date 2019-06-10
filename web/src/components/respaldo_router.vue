<template>
    <div class="ui container">
        <table class="ui celled table">
            <thead>
                <th>IP</th>
                <th>Fecha</th>
                <th>Status</th>
            </thead>
            <tbody>
                <tr :class="[item.status ? 'error':'']" v-for="item in data" :key="item.ip">
                    <td>{{item.ip}}</td>
                    <td>{{item.fecha}}</td>
                    <td>{{item.status}}</td>
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