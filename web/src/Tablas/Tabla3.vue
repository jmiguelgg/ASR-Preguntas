<template>
  <div class="ui container">
    <h1>Ping Puller</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader1 ? 'active':''">
        <div class="ui text loader">Testeando la red</div>
      </div>
      <form v-on:submit.prevent="PingPuller" ref="form" class="ui form">
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
    <h1>Capturando TRAP's</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader2 ? 'active':''">
        <div class="ui text loader">Captando TRAP's</div>
      </div>
      <form v-on:submit.prevent="CaptTraps" class="ui form">
        <div class="two fields">
          <div class="field">
            <label>Tiepo de captura de traps</label>
            <input type="text" placeholder="Tiempo en segundos" maxlength="4" v-model="timeTraps" required>
          </div>
          <div class="field">
            <label>Inicio</label>
            <input type="submit" value="Comenzar" class="ui button positive">
          </div>
        </div>
      </form>
    </div>
    <TableTraps :data="data2"/>
    <h1>Capturando Syslogs</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader3 ? 'active':''">
        <div class="ui text loader">Captando Syslogs</div>
      </div>
      <form v-on:submit.prevent="CaptSyslogs" class="ui form">
        <div class="two fields">
          <div class="field">
            <label>Tiepo de captura de Syslogs</label>
            <input type="text" placeholder="Tiempo en segundos" maxlength="4" v-model="timeSyslogs" required>
          </div>
          <div class="field">
            <label>Inicio</label>
            <input type="submit" value="Comenzar" class="ui button positive">
          </div>
        </div>
      </form>
    </div>
    <TableSyslogLevel :data="data3"/>
    <h1>Capturando reinicio de router por Syslogs</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader4 ? 'active':''">
        <div class="ui text loader">Captando reinicio de router</div>
      </div>
      <form v-on:submit.prevent="CaptRestart" class="ui form">
        <div class="two fields">
          <div class="field">
            <label>Tiepo de captura de reinicios</label>
            <input type="text" placeholder="Tiempo en segundos" maxlength="4" v-model="timeRestart" required>
          </div>
          <div class="field">
            <label>Inicio</label>
            <input type="submit" value="Comenzar" class="ui button positive">
          </div>
        </div>
      </form>
    </div>
    <TableSyslogRestart :data="data4" />
  </div>
</template>

<script>
import {HTTP_PYTHON} from '@/http-common';
import TableIPs from '@/components/ips_ping_puller';
import TableTraps from '@/components/traps';
import TableSyslogLevel from '@/components/syslog_nivel';
import TableSyslogRestart from '@/components/syslog_restart';
export default {
  components:{
    TableIPs, TableTraps, TableSyslogLevel, TableSyslogRestart
  },
  mounted(){
    let user = this.$session.get('user')
    this.email = user.correo
    this.number = user.numero
  },
  methods: {
    CaptRestart(){
      this.active_loader4 = true
      let formData = new FormData();
      formData.append('correo',this.email);
      formData.append('numero',this.number)
      formData.append('tiempo',this.timeRestart);
      HTTP_PYTHON.post('Tabla3/P3',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(res =>{
        this.data4 = res.data
        this.active_loader4 = false
      })
      .catch()
    },
    CaptTraps(){
      this.active_loader2 = true
      let formData = new FormData();
      formData.append('correo',this.email);
      formData.append('numero',this.number)
      formData.append('tiempo',this.timeTraps);
      HTTP_PYTHON.post('Tabla3/P2',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(res =>{
        this.data2 = res.data
        this.active_loader2 = false
      })
      .catch()
    },
    CaptSyslogs(){
      this.active_loader3 = true
      let formData = new FormData();
      formData.append('correo',this.email);
      formData.append('numero',this.number)
      formData.append('tiempo',this.timeSyslogs);
      HTTP_PYTHON.post('Tabla3/P3',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(res =>{
        this.data3 = res.data
        this.active_loader3 = false
      })
      .catch()
    },
    setFileiIPs(){
      this.file = this.$refs.ipsfile.files;
    },
    PingPuller() {
      let formData = new FormData();
      formData.append('file', this.file[0],this.file[0].name);
      formData.append('email',this.email);
      formData.append('number',this.number)
      formData.append('numPing',this.numPing);
      formData.append('timePing',this.timePing);
      this.active_loader1 = true
      HTTP_PYTHON.post('/Tabla3/P1',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(this.response_interaction,console.log)
      .catch(this.response_action);
    },
    response_action(){
      this.active_loader1 = false;
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
      active_loader1: false,
      active_loader2: false,
      active_loader3: false,
      active_loader4: false,
      data: {},
      data2: '',
      data3: '',
      data4: '',
      timeTraps: 0,
      timeSyslogs: 0,
      timeRestart: 0
    };
  }
};
</script>
