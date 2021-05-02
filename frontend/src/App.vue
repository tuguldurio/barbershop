<template>
  <Navbar @openCart="showCart=true"/>
  
  <main class="pt-16 flex-1">
    <Error404 v-if="error404"/>
    <router-view v-else/>
  </main>

  <Footer/>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import Error404 from '@/views/error/404.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
    Error404
  },
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn
    },
    error404() {
      return this.$store.state.error.error404
    }
  }
}
</script>

<style lang="scss">
html, body {
  height: 100%;
}

body {
  position: relative;
}

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
</style>