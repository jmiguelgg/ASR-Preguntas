<template>
  <div id="app">
    <component :is="layout">
      <router-view/>
    </component>
  </div>
</template>

<script>
const default_layout = "default"
export default {
  computed:{
    layout(){
      return default_layout + this.$route.meta.layout
    }
  }
}
</script>
