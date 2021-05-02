export default {
  state: {
    error404: false
  },
  getters: {
  },
  mutations: {
    error404(state) {
      state.error404 = true
    },
    resetError404(state) {
      state.error404 = false
    }
  },
  actions: {
    error404({commit}) {
      commit('error404')
    },
    resetError404({commit}) {
      commit('resetError404')
    }
  }
};