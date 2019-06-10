<template>
  <div class="ui container full">
    
    <div class="ui middle aligned center aligned grid full">
      <div class="column">
        <div class="ui inverted dimmer" :class="active_loader ? 'active':''">
          <div class="ui text loader">Login</div>
        </div>
        <h2 class="ui teal image header">
          <div class="content">
            Entra a tu cuenta
          </div>
        </h2>
        <form v-on:submit.prevent="login" class="ui large form">
          <div class="ui stacked segment">
            <div class="field">
              <div class="ui left icon input">
                <i class="user icon"></i>
                <input type="email" placeholder="Correo" v-model="email" required>
              </div>
            </div>
            <div class="field">
              <div class="ui left icon input">
                <i class="lock icon"></i>
                <input type="password" placeholder="Contraseña" v-model="pass" required>
              </div>
            </div>
            <input type="submit" value="Entrar" class="ui fluid large teal submit button">
          </div>
          <div class="ui error message"></div>
        </form>
        <div class="ui message">
          ¿Nuevo con nosotros? <a href="/newuser">Crea una cuenta</a>
        </div>
        <div class="ui segment center aligned" v-show="isItemVisible">
          <h3 class="ui header red">{{errorMessage}}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {HTTP_EXPRESS} from '@/http-common';
const SHA256 = require("crypto-js/sha256");
export default {
  methods:{
    login(){
      let sendData = {
        correo: this.email,
        pass: SHA256(this.pass).toString()
      }
      this.active_loader = true
      HTTP_EXPRESS.post('/login',sendData)
        .then(res =>{
          this.active_loader = false
          if (res.data.length != 0) {
            this.$session.start()
            this.$session.set('user',res.data[0])
            this.$router.push('/proyecto')
          }
          else{
            this.errorMessage = 'Correo o contraseña no valido'
            this.isItemVisible = true
          }
        })
        .catch(err =>{
          this.active_loader = false
          console.log(err)
        })
    }
  },
  data(){
    return{
      email: '',
      pass: '',
      errorMessage: '',
      active_loader: false,
      isItemVisible: false
    }
  }
}
</script>


<style scoped lang="css">
  .full{
    height: 1000px;
  }
  .column{
    max-width: 450px;
  }
</style>
