<template>
    <div id="app" class="ui container">
        <div class="ui middle aligned grid full">
            <form v-on:submit.prevent="crearUsuario" class="ui form column segment">
                <div class="ui inverted dimmer" :class="active_loader ? 'active':''">
                    <div class="ui text loader">Creando nuevo usuario</div>
                </div>
                <div class="field">
                    <label>Nombre</label>
                    <div class="two fields">
                        <div class="field">
                            <input type="text" placeholder="Nombres" v-model="name" required>
                        </div>
                        <div class="field">
                            <input type="text" placeholder="Apellidos" v-model="last_name" required>
                        </div>
                    </div>
                    <div class="two fields">
                        <div class="field">
                            <label>Dirección de correo</label>
                            <input type="email" placeholder="correo@correo.com" v-model="email" required>
                        </div>
                        <div class="field">
                            <label>Teléfono</label>
                            <input type="text" placeholder="5215511111111" maxlength="13" v-model="phone" required>
                        </div>
                    </div>
                    <label>Contraseña</label>
                    <div class="two fields">
                        <div class="field">
                            <input type="password" minlength="8" placeholder="Contraseña" v-model="pass" required>
                        </div>
                        <div class="field">
                            <input type="password" minlength="8" placeholder="Confirma contraseña" v-model="pass_confirm" required>
                        </div>
                    </div>
                    <div class="field">
                        <input type="submit" value="Registrar" class="big positive ui button">
                    </div>
                </div>
            </form>
        </div>
        <div class="ui segment center aligned" v-show="isItemVisible1">
            <h3 class="ui header">¡Felicidades {{name}} tu cuenta ha sido creada con éxito!</h3>
            <form>
            <input type="submit" formaction="http://localhost:8080/" class="positive ui button" value="Iniciar seción">
            </form>
        </div>
        <div class="ui segment center aligned" v-show="isItemVisible2">
            <h3 class="ui header red">{{errorMessage}}</h3>
        </div>
    </div>
</template>

<script>
import {HTTP_EXPRESS} from '@/http-common';
const SHA256 = require("crypto-js/sha256");
export default {
    methods:{
        crearUsuario(){
            if (this.verifyPass()){
                let dataSend = {
                    nombres: this.name,
                    apellidos: this.last_name,
                    correo: this.email,
                    numero: this.phone,
                    pass: SHA256(this.pass).toString()
                }
                this.active_loader = true
                HTTP_EXPRESS.post('/newuser',dataSend)
                    .then(res =>{
                        this.cleanData()
                        this.active_loader = false
                        this.isItemVisible2 = false
                        this.isItemVisible1 = true
                    })
                    .catch(err =>{
                        this.errorMessage = '¡Ha ocurrido un problema con tu registro, intentalo de nuevo!'
                        this.active_loader = false
                        this.isItemVisible1 = false
                        this.isItemVisible2 = true
                        console.log(err)
                    })
            }
            else{
                this.active_loader = false
                this.isItemVisible1 = false
                this.isItemVisible2 = true
                this.errorMessage = '¡Verifica tu contraseña!'
            }
        },
        verifyPass(){
            return this.pass === this.pass_confirm
        },
        cleanData(){
            this.name = ''
            this.last_name = ''
            this.email = ''
            this.phone = ''
            this.pass = ''
            this.pass_confirm = ''
        }
    },
    data(){
        return{
            name: '',
            last_name: '',
            email: '',
            phone: '',
            pass: '',
            pass_confirm: '',
            errorMessage: '',
            active_loader: false,
            isItemVisible1: false,
            isItemVisible2: false,
        }
    }
}
</script>


<style scoped lang="css">
  .full{
    height: 500px;
  }
  .column{
    max-width: 100%;
  }
</style>
