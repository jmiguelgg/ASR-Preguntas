<template>
  <div class="ui">
    <div class="ui grid">
      <div class="four wide column">
        <div class="ui vertical fluid tabular menu">
          <a class="item" :class="{ active : item.status }" v-for="item in tablas" :key="item.id" @click="changeTable(item.id)">{{ item.name }}</a>
        </div>
      </div>
      <div class="twelve wide stretched column">
        <div class="ui segment">
          <Tabla3 v-show="tablas[0].status" />
          <Tabla4 v-show="tablas[1].status" />
          <Tabla6 v-show="tablas[3].status" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Tabla3 from "@/Tablas/Tabla3";
import Tabla4 from "@/Tablas/Tabla4";
import Tabla6 from "@/Tablas/Tabla6";
export default {
  components: {
    Tabla3, Tabla4, Tabla6
  },
  data() {
    return {
      tablas: [
        { id: "1", name: "Tres", status: true },
        { id: "2", name: "Cuatro", status: false },
        { id: "3", name: "Cinco", status: false },
        { id: "4", name: "Seis", status: false },
        { id: "5", name: "Siete", status: false }
      ]
    };
  },
  mounted(){
    if(this.$session.get('user') == null)
      this.$router.push('/')
  },
  methods: {
    changeTable(id) {
      for (let index = 0; index < this.tablas.length; index++) {
        this.tablas[index].status = false;
      }
      let tmp = this.tablas.find( elem =>{
        return elem.id == id;
      })
      tmp.status = true
    }
  }
}
</script>
