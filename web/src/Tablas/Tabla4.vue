<template>
  <div class="ui container">
    <h1>Información Router</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader1 ? 'active':''">
        <div class="ui text loader">Consultando los routers</div>
      </div>
      <form v-on:submit.prevent="infoRouter" ref="form" class="ui form">
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
            <input type="file" ref="ipsfile" @change="setFileiIPs" required />
          </div>
          <div class="field">
              <label>Pedir</label>
            <input type="submit" class="positive ui button" value="Traer info" />
          </div>
        </div>
      </form>
    </div>
    <TableInfoRouter :data="data"/>
    <h1>Respaldo de configuración de los Routers</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader2 ? 'active':''">
        <div class="ui text loader">Consultando los routers</div>
      </div>
      <form v-on:submit.prevent="configuracionRouters" ref="form" class="ui form">
        <div class="two fields">
          <div class="field">
            <label for="file">Archivo con IP's</label>
            <input type="file" ref="ipsfile2" @change="setFileiIPs2" required />
          </div>
          <div class="field">
              <label>Pedir</label>
            <input type="submit" class="positive ui button" value="Respaldar" />
          </div>
        </div>
      </form>
    </div>
    <TableRespaldoRouter :data="data2"/>
    <h1>Detección de cambio en dispositivos por Syslogs</h1>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader3 ? 'active':''">
        <div class="ui text loader">Captando Syslogs</div>
      </div>
      <form v-on:submit.prevent="CaptSyslogs" class="ui form">
        <div class="three fields">
          <div class="field">
            <label>Tiepo de captura de Syslogs</label>
            <input type="text" placeholder="Tiempo en segundos" maxlength="4" v-model="timeSyslogs" required>
          </div>
          <div class="field">
            <label for="file">Archivo con IP's</label>
            <input type="file" ref="ipsfile2" @change="setFileiIPs2" required />
          </div>
          <div class="field">
            <label>Inicio</label>
            <input type="submit" value="Comenzar" class="ui button positive">
          </div>
        </div>
      </form>
    </div>
    <TableSyslogLevel :data="data3"/>
    <h1>Crear templates de configuración de routers</h1>
    <h4>El protocolo de enrutamiento disponible es OSPF version 3</h4>
    <div class="ui segment">
      <div class="ui inverted dimmer" :class="active_loader4 ? 'active':''">
        <div class="ui text loader">Crecando template</div>
      </div>
      <form v-on:submit.prevent="CrearTemplate" class="ui form">
        <div class="three fields">
          <div class="field">
            <input type="text" placeholder="Hostname" v-model="hostname" required>
          </div>
          <div class="field">
            <input type="text" placeholder="Id OSPF" v-model="idOSPF" required>
          </div>
          <div class="field">
            <input type="text" placeholder="IP servidor de syslogs" v-model="server_syslogs">
          </div>
        </div>
        <h3>Usuario del router</h3>
        <div class="two fields">
          <div class="field">
            <input type="text" placeholder="Nombre de usuario" v-model="user_name" required>
          </div>
          <div class="field">
            <input type="text" placeholder="Contraseña" v-model="pass" required>
          </div>
        </div>
        <h3>Networks conocidas</h3>
        <div class="four fields" v-for="elem in listaNetworks" :key="elem.id">
          <div class="field">
            <input type="text" placeholder="Network" v-model="elem.network" required>
          </div>
          <div class="field">
            <input type="text" placeholder="Wildcard mask" v-model="elem.wildcard" required>
          </div>
          <div class="field">
            <input type="text" placeholder="Área de conexión" v-model="elem.area" required>
          </div>
          <div class="field">
            <input type="button" class="ui button positive" @click="pushNetwork" value="+">
            <input type="button" class="ui button negative" @click="popNetwork" value="-">
          </div>
        </div>
        <h3>Interfaces</h3>
        <div class="five fields" v-for="elem in listaInterfaces" :key="elem.id">
          <div class="field">
            <select class="ui dropdown" v-model="elem.tipo" required>
              <option value="FastEthernet" selected>FastEthernet</option>
              <option value="Serial">Serial</option>
            </select>
          </div>
          <div class="field">
            <input type="text" placeholder="Ejm. 0/0" v-model="elem.identificador" required>
          </div>
          <div class="field">
            <input type="text" placeholder="Address" v-model="elem.address" required>
          </div>
          <div class="field">
            <input type="text" placeholder="Mascara" v-model="elem.mascara" required>
          </div>
          <div class="field">
            <input type="button" class="ui button positive" @click="pushInterface" value="+">
            <input type="button" class="ui button negative" @click="popInterface" value="-">
          </div>
        </div>
        <div class="fields">
          <div class="field">
            <input type="submit" value="Crear" class="ui button big positive">
            <input type="reset" value="Borrar" class="ui orange button big">
          </div>
        </div>
      </form>
    </div>
    <ShowRouterConfig :data="data4"/>
    <h1>Mostrar templates creados</h1>
    <ShowListRouterConfig :data="data5"/>
    <h1>Archivos de configuración almacenados</h1>
    <ShowListConfigOriginal :data="data6"/>
  </div>
</template>

<script>
import {HTTP_PYTHON,HTTP_EXPRESS_TABLA_4} from '@/http-common';
import TableInfoRouter from '@/components/info_router';
import TableRespaldoRouter from '@/components/respaldo_router';
import TableSyslogLevel from '@/components/syslog_nivel';
import ShowRouterConfig from '@/components/show_Router_Config';
import ShowListRouterConfig from '@/components/show_list_Router_Config';
import ShowListConfigOriginal from '@/components/show_list_Config_Original';
const dateFormat = require('dateformat');
export default {
  components:{
    TableInfoRouter,
    TableRespaldoRouter,
    TableSyslogLevel,
    ShowRouterConfig,
    ShowListRouterConfig,
    ShowListConfigOriginal
  },
  mounted(){
    let user = this.$session.get('user')
    this.userId = user._id
    this.email = user.correo
    this.number = user.numero
    this.getTemplates()
    this.getArchivosConfig()
  },
  methods: {
    pushInterface(){
      let id = this.listaInterfaces.length
      this.listaInterfaces.push({
        id: id + 1,
        tipo: 'FastEthernet',
        identificador: '',
        address: '',
        mascara: ''})
    },
    popInterface(){
      let id = this.listaInterfaces.length
      if (id != 1)
        this.listaInterfaces.pop()
    },
    pushNetwork(){
      let id = this.listaNetworks.length
      this.listaNetworks.push({
        id: id + 1,
        network:'',
        wildcard: '',
        area: 0})
    },
    popNetwork(){
      let id = this.listaNetworks.length
      if (id != 1)
        this.listaNetworks.pop()
    },
    setFileiIPs(){
      this.file = this.$refs.ipsfile.files;
    },
    setFileiIPs2(){
      this.file2 = this.$refs.ipsfile2.files;
    },
    getTemplates(){
      HTTP_EXPRESS_TABLA_4.post('/templates',{userId: this.userId})
      .then(res =>{
        this.data5 = res.data
      })
      .catch(err =>{
        console.log(err)
      })
    },
    getArchivosConfig(){
      HTTP_PYTHON.get('/Tabla4/P2')
      .then(res =>{
        this.data6 = res.data
      })
      .catch(err =>{
        console.log(err)
      })
    },
    CrearTemplate(){
      this.active_loader4 = true
      let templateConfig = {
        hostname: this.hostname,
        idOSPF: this.idOSPF,
        user_name: this.user_name,
        pass: this.pass,
        server_syslogs: this.server_syslogs,
        networks: this.listaNetworks,
        interfaces: this.listaInterfaces
      }
      this.data4 = templateConfig
      var now = new Date();
      let tmp = {
        id: this.data5.length+1,
        fecha: dateFormat(now,"dd/mm/yy HH:MM:ss"),
        data: templateConfig
      }
      HTTP_EXPRESS_TABLA_4.post('/newTemplate',{userId: this.userId,template:tmp})
      .then(() =>{
        this.active_loader4 = false
        this.getTemplates()
      })
      .catch(err =>{
        this.active_loader4 = false
        console.log(err)
      })
    },
    infoRouter() {
      let formData = new FormData();
      formData.append('file', this.file[0],this.file[0].name);
      formData.append('email',this.email);
      formData.append('number',this.number)
      this.active_loader1 = true
      HTTP_PYTHON.post('/Tabla4/P1',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(res =>{
          this.active_loader1 = false;
          this.data = res.data;
      },console.log)
      .catch(/*this.response_action*/);
    },
    configuracionRouters() {
      let formData = new FormData();
      formData.append('file', this.file2[0],this.file2[0].name);
      formData.append('email',this.email);
      formData.append('number',this.number)
      this.active_loader2 = true
      HTTP_PYTHON.post('/Tabla4/P2',formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(res =>{
          this.active_loader2 = false;
          this.data2 = res.data;
      },console.log)
      .catch(/*this.response_action*/);
    },
    CaptSyslogs(){
      this.active_loader3 = true
      let formData = new FormData();
      formData.append('file', this.file2[0],this.file2[0].name);
      formData.append('email',this.email);
      formData.append('number',this.number);
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
    response_action(){
      this.active_loader1 = false;
      this.$refs.form.reset();
      this.email = "";
      this.number = "";
      this.numPing = "";
      this.timePing = "";
    }
  },
  data() {
    return {
      options: 5,
      userId: "",
      email: "",
      number: "",
      file: "",
      file2: "",
      active_loader1: false,
      active_loader2: false,
      active_loader3: false,
      active_loader4: false,
      data: {},
      data2: {},
      data3: {},
      data4: {},
      data5: {},
      data6: {},
      timeTraps: 0,
      timeSyslogs: 0,
      timeRestart: 0,
      hostname: '',
      idOSPF: '',
      server_syslogs: '',
      user_name: '',
      pass: '',
      listaNetworks: [{
        id: 1,
        network:'',
        wildcard: '',
        area: 0
      }],
      listaInterfaces: [{
        id: 1,
        tipo: 'FastEthernet',
        identificador: '',
        address: '',
        mascara: ''
      }]
    };
  }
};
</script>
