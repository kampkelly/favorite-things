import Vue from 'vue';
import Vuex from 'vuex';
import { LOGIN, LOGOUT, SET_APP_ERROR_MESSAGE } from './mutationTypes';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: '',
    token: localStorage.getItem('token') || '',
    appErrorMessage: '',
    showAppErrorMessage: false,
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
      state.appErrorMessage = payload.message;
      state.showAppErrorMessage = payload.show;
    },
  },
  actions: {
    LOGIN({ commit }, payload) {
      commit(LOGIN, payload);
      const message = { message: '', show: false };
      commit(SET_APP_ERROR_MESSAGE, message);
      localStorage.setItem('token', payload.token);
    },
    LOGOUT({ commit }) {
      commit(LOGOUT);
      const message = { message: '', show: false };
      commit(SET_APP_ERROR_MESSAGE, message);
      localStorage.removeItem('token');
    },
    SET_APP_ERROR_MESSAGE({ commit }, payload) {
      const message = { message: payload, show: true };
      commit(SET_APP_ERROR_MESSAGE, message);
    },
  },
  getters: {
    isAuthenticated: state => !!state.token,
    appErrorMessage: state => state.appErrorMessage,
    showAppErrorMessage: state => state.showAppErrorMessage,
  },
});
