<template>
  <div id="app" class="ui container">
    <h1>Ping Puller</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader">
        <div class="ui text loader">Testeando la red</div>
      </div>
      <form action="" @submit="PingPuller" ref="form" class="ui form">
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
        <div class="three fields">
          <div class="field">
            <label for="file">Archivo con IP's</label>
            <input type="file" ref="ipsfile" @change="setFileiIPs" required />
          </div>
          <div class="field">
            <label for="ping">Numero de pings</label>
            <select v-model="numPing" class="ui dropdown" required>
              <option value="">Número</option>
              <option v-for="i in options" :key="i" :value="i">{{ i }}</option>
            </select>
          </div>
          <div class="field">
            <label for="timePing">Tiempo de ping</label>
            <input type="text" v-model="timePing" v-model.trim="timePing" placeholder="Tiempo limite (mili segundos)" required />
          </div>
        </div>
        <div class="fields">
          <div class="field">
            <input type="submit" class="positive ui button" value="Ping Puller" />
          </div>
        </div>
      </form>
    </div>
    <TableIPs :data="data"/>
  </div>
</template>

<script>
import {HTTP} from './http-common';
import TableIPs from './components/ips_ping_puller';
export default {
  components:{
    TableIPs
  },
  methods: {
    setFileiIPs(){
      this.file = this.$refs.ipsfile.files;
    },
    PingPuller() {
      var formData = new FormData();
      formData.append('file', this.file[0],this.file[0].name);
      formData.append('email',this.email);
      formData.append('number',this.number)
      formData.append('numPing',this.numPing);
      formData.append('timePing',this.timePing);
      this.active_loader = "active"
      HTTP.post('/Tabla3/P1',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(this.response_interaction,console.log)
      .catch(this.response_action);
    },
    response_action(){
      this.active_loader = "";
      this.$refs.form.reset();
      this.email = "";
      this.number = "";
      this.numPing = "";
      this.timePing = "";
    },
    response_interaction(response){
      this.response_action();
      this.data = response.data;
    }
  },
  data() {
    return {
      options: 5,
      email: "",
      number: "",
      numPing: "",
      timePing: "",
      file: "",
      active_loader: "",
      data: {}
    };
  }
};
</script>

<style>
</style>
