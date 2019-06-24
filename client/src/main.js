/*eslint-disable */

import Vue from 'vue';
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';
import { InMemoryCache } from 'apollo-cache-inmemory';
import VueApollo from 'vue-apollo';
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';

Vue.component('v-select', vSelect)

try {
  window.$ = window.jQuery = require('jquery');
} catch (e) {}
window.Popper = require('popper.js');
require('bootstrap');

import App from './App.vue';
import router from './router';
import store from './store';
import './registerServiceWorker';

const httpLink = new HttpLink({ uri: 'http://0.0.0.0:7000/api' });

const authLink = setContext(({ headers }) => {
  const token = localStorage.getItem('token');
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      "access-token": token ? token : "",
    }
  }
});

const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
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
