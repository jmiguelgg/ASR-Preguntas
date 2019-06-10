<template>
    <div class="ui container">
        <h1>Estadísticas de tráfico en cada interfaz</h1>
        <div class="ui segment">
            <div class="ui inverted dimmer" :class="active_loader1 ? 'active':''">
                <div class="ui text loader">Consultando los routers</div>
            </div>
            <form v-on:submit.prevent="graphRouters" ref="form" class="ui form">
                <div class="two fields">
                    <div class="field">
                        <label for="email">Correo de notificación</label>
                        <input type="email" v-model="email" v-model.trim="email" placeholder="Correo" required />
                    </div>
                    <div class="field">
                        <label for="numero">Número para WhatsApp</label>
                        <input type="text" v-model="number" v-model.trim="number" minlength="13" placeholder="Numero celular" required />
                        <div class="ui pointing label">
                            Clave del país + numero de región + lada local + número celular
                        </div>
                    </div>
                </div>
                <div class="two fields">
                    <div class="field">
                        <label for="file">Archivo con IP's</label>
                        <input type="file" ref="ipsfile1" @change="setFileiIPs(1)" required />
                    </div>
                    <div class="field">
                        <label>Pedir</label>
                        <input type="submit" class="positive ui button" value="Consultar" />
                    </div>
                </div>
            </form>
        </div>
        <GraphycRouterUse/>
    </div>
</template>

<script>
import {HTTP_PYTHON} from '@/http-common';
import GraphycRouterUse from '@/components/graphyc_router_use'
export default {
    components:{
        GraphycRouterUse
    },
    methods:{
        graphRouters(){
            //HTTP_PYTHON.post('')
        },
        setFileiIPs(file){
            switch (file) {
                case 1:
                    this.file1 = this.$refs.ipsfile1.files;
                    break;
            }
        }
    },
    mounted(){
        let user = this.$session.get('user')
        this.userId = user._id
        this.email = user.correo
        this.number = user.numero
    },
    data(){
        return{
            email: "",
            number: "",
            file1: "",
        }
    }
}
</script>

