/*eslint-disable */

import Vue from 'vue';
import ApolloClient from 'apollo-boost'
import VueApollo from 'vue-apollo';

require('bootstrap');

import App from './App.vue';
import router from './router';
import store from './store';
import './registerServiceWorker';

const apolloClient = new ApolloClient({
  uri: 'http://0.0.0.0:7000/api'
});

Vue.config.productionTip = false;
Vue.use(VueApollo);

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
});

new Vue({
  router,
  store,
  apolloProvider,
  render: h => h(App),
}).$mount('#app');
