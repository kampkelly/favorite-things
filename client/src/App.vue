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
  name: 'signup',
  components: {
    Header,
  },
}
</script>

<style lang="scss">
body {
  margin: 0px;
  overflow-x: hidden;
  background: rgb(235, 235, 235);
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  a {
    text-decoration: none;
  }
}
#nav {
  a {
    font-weight: bold;
    color: white;
    &.router-link-exact-active {
      color: #cfcfcf;
    }
  }
}
main {
  margin-top: 50px;
}
</style>
