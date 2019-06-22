import Vue from 'vue';
import Vuex from 'vuex';
import { LOGIN } from './mutationTypes'
import { LOGOUT } from './mutationTypes'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: '',
    token: localStorage.getItem('token') || '',
  },
  mutations: {
    LOGOUT(state) {
      state.token = '';
    },
    LOGIN(state, payload) {
      state.user = payload.user;
      state.token = payload.token;
    }
  },
  actions: {
    LOGIN({ commit }, payload) {
      commit(LOGIN, payload);
      localStorage.setItem('token', payload.token)
    },
    LOGOUT({ commit }) {
      commit(LOGOUT);
      localStorage.removeItem('token');
    },
  },
  getters : {
    isAuthenticated: state => !!state.token,
  },
});
