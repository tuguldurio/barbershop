import { createStore } from 'vuex'
import user from './modules/user'
import error from './modules/error'

const store = createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user,
    error
  }
})

export default store