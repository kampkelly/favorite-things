<template>
    <div>
        <header>
            <nav class="">
                <div>
                    <h2><router-link to="/favorites">Favorite Things</router-link></h2>
                </div>
                <div>
                    <router-link to="/add-favorite" v-if="isAuthenticated == true">Add Favorite Thing</router-link>
                    <a href="#" v-on:click="showAuditLogs" v-if="isAuthenticated == true">Show Audit Logs</a>
                    <a href="#logout" class="" v-on:click="logout" v-if="isAuthenticated == true">Logout</a>
                </div>
            </nav>
        </header>
        <div class="logs-container">
            <i class="fas fa-times-circle" v-on:click="closeLogsContainer" v-show="closeLogButton"></i>
            <ul class="list-group">
                <li class="list-group-item" v-for="log in logs" v-bind:key="log.id">
                    {{log.log}} <br>
                    <span>Date: {{logDate(log)}}</span>
                </li>
            </ul>
            <p class="no-logs" v-if="!logs.length">You have no logs yet!</p>
        </div>
    </div>
</template>

<script>
// eslint-disable-next-line
import gql from 'graphql-tag';
import moment from 'moment';
import { LOGOUT, SET_APP_ERROR_MESSAGE } from '../mutationTypes';


const getUserLogs = gql`query {
  getUserLogs {
    id
    log
    createdDate
  }
}
`;

export default {
  data() {
    return {
      logs: [],
      closeLogButton: false,
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
  apollo: {
    getUserLogs: {
      query: getUserLogs,
      skip() {
        return this.skipQuery;
      },
    },
  },
  methods: {
    async logout(event) {
      event.preventDefault();
      await this.$store.dispatch(LOGOUT);
      this.$router.push('/');
      this.$router.push('/registration/signin');
    },
    async showAuditLogs() {
      $('.logs-container').animate({ right: '0%' }, 200);
      this.$apollo.queries.getUserLogs.skip = false;
      let logs = [];
      try {
        logs = await this.$apollo.queries.getUserLogs.refetch();
        this.logs = logs.data.getUserLogs;
        this.closeLogButton = true;
      } catch (err) {
        this.closeLogButton = true;
        this.$store.dispatch(SET_APP_ERROR_MESSAGE, err.message.split(':')[1]);
      }
    },
    closeLogsContainer() {
      $('.logs-container').animate({ right: '-25%' }, 500);
      this.closeLogButton = false;
    },
    logDate(log) {
      return moment(String(log.createdDate)).format('hh:mm a MM/D/YY');
    },
  },
};
</script>

<style lang="scss" scoped>
 header {
     position: fixed;
     z-index: 20;
     top: 0;
     width: 100%;
     height: 50px;
     margin-bottom: 50px;
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
             flex: 1;
             h2 {
                 text-align: left;
                 padding-top: 5px;
                 padding-left: 150px;
                 margin-top: 0px;
                 margin-bottom: 0px;
             }
         }
         > div:nth-child(2) {
             flex: 1;
             text-align: right;
             padding-top: 15px;
             a {
                 padding-right: 15px;
             }
         }
     }
 }
 .logs-container {
     width: 25%;
     position: absolute;
     height: 100vh;
     max-height: 100%;
     overflow-y: scroll;
     z-index: 10;
     background: #d8d8d8;
     right: -25%;
     top: 50px;
     font-size: 0.8em;
     ul {
         width: 100%;
         background: green;
         li {
             background: #d8d8d8;
             span {
                 font-style: italic;
             }
         }
     }
     i {
         position: fixed;
         z-index: 14;
         right: 22%;
         top: 60px;
         font-size: 2em;
         float: left;
         color: grey;
         cursor: pointer;
     }
     .no-logs {
         padding-top: 50px;
         font-size: 1.7em;
         opacity: 0.7;
     }
 }
</style>
