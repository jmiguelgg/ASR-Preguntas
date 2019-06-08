import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      meta: { layout: "-noNavBar" },
      component: require("@/views/Login.vue").default
    },
    {
      path: "/proyecto",
      name: "proyecto",
      meta: { layout: "" },
      component: require("@/views/Main.vue").default
    },
    {
      path: "/newuser",
      name: "newuser",
      meta: { layout: "-noNavBar" },
      component: require("@/views/NewUser.vue").default
    },
    {
      path: "*",
      name: "404*",
      component: require("@/views/Error.vue").default
    }
  ]
});
