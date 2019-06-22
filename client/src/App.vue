<template>
  <div id="app">
    <div id="nav">
      <Header></Header>
    </div>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
export default {
  name: 'App',
  components: {
    Header,
  },
}
</script>

<style lang="scss">
body {
  margin: 0px;
  overflow-x: hidden;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
main {
  margin-top: 50px;
}
</style>
