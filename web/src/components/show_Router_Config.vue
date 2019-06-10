<template>
    <div class="ui container segment">
        <div v-if="!(Object.entries(data).length === 0 && data.constructor === Object)">
            <p>hostname $ &#123; {{this.data.hostname}} &#125;</p>
            <p>router ospf $ &#123; {{this.data.idOSPF}} &#125;</p>
            <p v-for="elem in this.data.networks" :key="elem.id">
                network $ &#123; {{elem.network}} &#125; $ &#123; {{elem.wildcard}} &#125; area $ &#123; {{elem.area}} &#125;
            </p>
            <p>logging trap ${debugging}</p>
            <p>logging $ &#123; {{this.data.server_syslogs}} &#125;</p>
            <p>username $ &#123; {{this.data.user_name}} &#125; privilege ${15} password 0 $ &#123; {{this.data.pass}} &#125;</p>
            <p v-for="elem in this.data.interfaces" :key="elem.id">
                interface $ &#123; {{elem.tipo}}{{elem.identificador}} &#125; ip address $ &#123; {{elem.address}} &#125; $ &#123; {{elem.mascara}} &#125;
            </p>
        </div>
    </div>
</template>

<script>
export default {
    props:{
        data: {}
    }
}
</script>
