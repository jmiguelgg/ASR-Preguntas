<template>
    <div class="ui container">
        <table class="ui celled striped table">
            <thead>
                <th>Hostname</th>
                <th>Contenido</th>
            </thead>
            <tbody>
                <tr v-for="item in data" :key="item.id">
                    <td>{{item.hostname}}</td>
                    <td>
                        <p v-for="elem in item.info" :key="elem.data">{{elem.data}}</p>
                    </td>
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