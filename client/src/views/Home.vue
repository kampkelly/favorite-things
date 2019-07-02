<template>
  <div class="home">
    <h5 class="mb-3">My Favorite Things</h5>

    <div class="favorites-list-container">
      <span>Filter by:</span>
      <router-link to="/add-favorite"><i class="fas fa-plus-circle"></i></router-link>
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
  @keyframes pulse {
    0%   {
      transform: scaleX(1);
    }
    50%  {
      transform: scale3d(1.05,1.05,1.05);
    }
    100%  {
      transform: scaleX(1);
    }
  }
  .favorites-list-container {
    width: 80%;
    margin: auto;
    background: white;
    padding: 1.2em 5em 1em 5em;
    span {
      float: left;
    }
    i {
        float: right;
        font-size: 2em;
        color: #6202EE;
        animation-name: pulse;
        animation-duration: 1s;
        animation-iteration-count: infinite;
    }
    .bar {
        width: 30%;
        display: flex;
        a {
          flex: 1;
          text-decoration: underline !important;
        }
    }
  }
</style>
