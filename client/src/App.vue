<template>
  <div id="app">
    <div id="nav">
      <Header></Header>
      <div class="alert alert-danger w-50 m-auto" v-show="this.$store.getters.showAppErrorMessage" role="alert">
        {{this.$store.getters.appErrorMessage}}
      </div>
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
};
</script>

<style lang="scss">
body {
  margin: 0px;
  overflow-x: hidden;
  background: rgb(235, 235, 235);
  min-height: 100vh;
  padding-top: 50px;
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
  }
}
main {
  margin-top: 50px;
}
a {
  &.router-link-exact-active {
      color: #a5a5a5 !important;
    }
}
.vs__dropdown-toggle {
    width: 100%;
}
.no-favorite-text {
    font-size: 1.7em;
    opacity: 0.5;
  }
</style>
