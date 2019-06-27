import Vue from 'vue';
import Vuex from 'vuex';
import { LOGIN, LOGOUT, SET_APP_ERROR_MESSAGE } from './mutationTypes'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: '',
    token: localStorage.getItem('token') || '',
    appErrorMessage: '',
    showAppErrorMessage: false
  },
  mutations: {
    LOGOUT(state) {
      state.token = '';
    },
    LOGIN(state, payload) {
      state.user = payload.user;
      state.token = payload.token;
    },
    SET_APP_ERROR_MESSAGE(state, payload) {
      state.appErrorMessage = payload;
      state.showAppErrorMessage = 'true';
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
    SET_APP_ERROR_MESSAGE({ commit }, payload) {
      commit(SET_APP_ERROR_MESSAGE, payload);
    },
  },
  getters : {
    isAuthenticated: state => !!state.token,
    appErrorMessage: state => {
      return state.appErrorMessage
    },
  showAppErrorMessage: state => {
      return state.showAppErrorMessage
    },
  },
});
