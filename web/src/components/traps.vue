<template>
    <div class="ui container">
        <table class="ui celled striped table">
            <thead>
                <th>Trap</th>
                <th>Fecha</th>
                <th>Contenido</th>
            </thead>
            <tbody>
                <tr v-for="item in data" :key="item.id">
                    <td>{{item.id}}</td>
                    <td>{{item.fecha}}</td>
                    <td class="right aligned">{{item.trap}}</td>
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