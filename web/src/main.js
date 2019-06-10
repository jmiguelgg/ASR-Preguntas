import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Default from "@/layouts/Default";
import Default_NoNavBar from "@/layouts/Default-NoNavBar";
import "./semantic/dist/semantic.min.css";
import VueSession from 'vue-session'
import VueApexCharts from 'vue-apexcharts'

Vue.component("default", Default);
Vue.component('apexchart', VueApexCharts);
Vue.component("default-noNavBar", Default_NoNavBar);
Vue.config.productionTip = false;
Vue.use(VueSession,{persist:true})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
