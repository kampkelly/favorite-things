<template>
  <div class="home">
    <h5 class="mb-3">My Favorite Things</h5>
     
    <div class="favorites-list-container">
      <span>Filter by:</span>
      <div class="bar">
          <router-link to="/favorites/all">All favorites</router-link>
          <router-link to="/favorites/category">Category</router-link>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

export default {
  name: 'home',
};
</script>

<style lang="scss" scoped>
  .favorites-list-container {
    width: 80%;
    margin: auto;
    background: white;
    padding: 1.2em 5em 1em 5em;
    span {
      float: left;
    }
    .bar {
      width: 30%;
      display: flex;
      a {
        flex: 1;
      }
    }
  }
</style>
