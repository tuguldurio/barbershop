import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/tailwind.css'
import axios from 'axios'

axios.defaults.baseURL = 'http://192.168.0.235:8000'

axios.interceptors.request.use(
  function (config) {
    const token = store.state.user.accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(
  response => {
    return response;
  },
  async error => {
    if (error.response.status === 404) {
      store.dispatch('error404')
    }
    else if (error.response.status === 401 && error.config.url !== '/api/auth/token') {
      store.dispatch('logout')
    }
    throw error
  }
)

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.getters.loggedIn) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})

router.afterEach((to, from) => {
  store.dispatch('resetError404')
})

createApp(App).use(store).use(router).mount('#app')