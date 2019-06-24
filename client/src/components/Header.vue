<template>
    <div>
        <header>
            <nav class="">
                <div>
                    <h2><router-link to="/">Favorite Things</router-link></h2>
                </div>
                <div>
                    <router-link to="/add-favorite" v-if="isAuthenticated == true">Add Favorite</router-link>
                    <a href="#logout" class="" v-on:click="logout" v-if="isAuthenticated == true">Logout</a>
                    <i class="fas fa-ellipsis-v"></i>
                </div>
            </nav>
        </header>
    </div>
</template>

<script>
import { LOGOUT } from '../mutationTypes'

export default {
    computed : {
      isAuthenticated : function() { 
        return this.$store.getters.isAuthenticated
      }
    },
    methods: {
      async logout(event) {
        event.preventDefault();
        await this.$store.dispatch(LOGOUT);
        this.$router.push('/');
        this.$router.push('/registration/signin');
      }
    },
};
</script>

<style lang="scss" scoped>
 header {
     height: 50px;
     nav {
         color: white;
         margin: 0px;
         height: 100%;
         background: #6202EE;
         display: flex;
         padding: 0em 1em 0em 1em;
         a {
             color: white;
         }
         > div:nth-child(1) {
             flex: 5;
             h2 {
                 text-align: center;
                 padding-top: 5px;
                 margin-top: 0px;
                 margin-bottom: 0px;
             }
         }
         > div:nth-child(2) {
             flex: 1;
             text-align: right;
             a {
                 padding-right: 15px;
             }
             i {
                 font-size: 1.5em;
                 padding-top: 13px;
             }
         }
     }
 }
</style>
