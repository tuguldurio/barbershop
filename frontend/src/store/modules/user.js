import axios from "axios";

export default {
  state: {
    accessToken: null,
    userLoaded: false
  },
  getters: {
    loggedIn(state) {
      return state.accessToken == null ? false : true
    }
  },
  mutations: {
    updateToken(state, token) {
      state.accessToken = token
      state.userLoaded = true
    },
    deleteToken(state) {
      state.accessToken = null
      state.userLoaded = true
      location.reload()
    }
  },
  actions: {
    login: ({ commit }, payload) => {
      return new Promise((resolve, reject) => {
        axios.post('/api/auth/token', payload)
        .then(({ data, status }) => {
          if (status === 200) {
            commit('updateToken', data.access_token)
            resolve(data.access);
          }
        })
        .catch(error => {
          reject(error)
        });
      });
    },
    logout: ({ commit }) => {
      commit('deleteToken')
    },
  }
};