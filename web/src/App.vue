<template>
  <div id="app" class="ui container">
    <form action="" @submit="PingPuller" class="ui form">
      <div class="fields">
        <div class="field">
          <label for="email">Correo de notificación</label>
          <input type="email" focus v-model="email" v-model.trim="email" placeholder="Correo" required />
        </div>
        <div class="field">
          <label for="numero">Número para WhatsApp</label>
          <input type="text" v-model="number" v-model.trim="number" minlength="13" placeholder="Numero celular" required />
        </div>
      </div>
      <div class="fields">
        <div class="field">
          <label for="ping">Numero de pings</label>
          <select v-model="numPing" class="ui dropdown" required>
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
</template>

<script>
export default {
  methods: {
    PingPuller() {
      let email = this.email;
      let number = this.number;
      let numPing = this.numPing;
      let timePing = this.timePing;
      console.log(email + " " + number + " " + numPing + " " + timePing);
    }
  },
  data() {
    return {
      options: 5,
      email: "",
      number: "",
      numPing: "",
      timePing: ""
    };
  }
};
</script>

<style>
</style>

