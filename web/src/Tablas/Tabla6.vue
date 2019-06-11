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
        <ShowListTrafic :data="data1"/>
        <h1>Estadísticas del CPU</h1>
        <div class="ui segment">
            <div class="ui inverted dimmer" :class="active_loader2 ? 'active':''">
                <div class="ui text loader">Consultando los routers</div>
            </div>
            <form v-on:submit.prevent="graphCPU" ref="form" class="ui form">
                <div class="two fields">
                    <div class="field">
                        <label for="file">Archivo con IP's</label>
                        <input type="file" ref="ipsfile2" @change="setFileiIPs(2)" required />
                    </div>
                    <div class="field">
                        <label>Pedir</label>
                        <input type="submit" class="positive ui button" value="Consultar" />
                    </div>
                </div>
            </form>
        </div>
        <GraphycRouterUse :data="data2" v-if="flag"/>
    </div>
</template>

<script>
import {HTTP_PYTHON} from '@/http-common';
import GraphycRouterUse from '@/components/graphyc_router_use';
import ShowListTrafic from '@/components/show_list_trafic';
export default {
    components:{
        GraphycRouterUse,
        ShowListTrafic
    },
    methods:{
        graphRouters(){
            let formData = new FormData();
            formData.append('file', this.file1[0],this.file1[0].name);
            formData.append('email',this.email);
            formData.append('number',this.number)
            this.active_loader1 = true
            HTTP_PYTHON.post('/Tabla6/P1',formData,{
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            })
            .then(res =>{
                this.active_loader1 = false;
                this.data1 = res.data;
            },console.log)
            .catch(/*this.response_action*/);
        },
        graphCPU(){
            let formData = new FormData();
            formData.append('file', this.file2[0],this.file2[0].name);
            formData.append('email',this.email);
            formData.append('number',this.number)
            this.active_loader2 = true
            HTTP_PYTHON.post('/Tabla6/P2',formData,{
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            })
            .then(res =>{
                this.active_loader2 = false;
                this.data2 = res.data;
                this.flag = true
            },console.log)
            .catch(/*this.response_action*/);
        },
        setFileiIPs(file){
            switch (file) {
                case 1:
                    this.file1 = this.$refs.ipsfile1.files;
                    break;
                case 2:
                    this.file2 = this.$refs.ipsfile2.files;
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
            file1: [],
            file2: [],
            active_loader1: false,
            active_loader2: false,
            data1: {},
            data2: {},
            flag: false
        }
    }
}
</script>

