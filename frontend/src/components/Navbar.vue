<template>
  <nav class="fixed top-0 z-30 inset-x-0 bg-white text-main-700 h-16">
    <div class="flex container h-full md:mx-auto px-4 lg:px-0 items-center justify-between">
      <div class="w-auto min-w-max">
        <a href="/" class="text-3xl font-semibold mr-8 cursor-pointer" @click.prevent="gotoHome">Barbershop</a>
      </div>
      
      <div class="z-50 md:space-x-8 space-y-8 md:space-y-0 bg-white text-5xl md:text-xl text-center" :class="{'absolute md:relative top-full md:top-0 left-0 w-full md:w-auto h-screen md:h-auto flex flex-col p-8 md:p-0 md:flex-row': open , 'hidden md:block': !open}">
        <a href="/" class="text-lg font-medium hover:underline" @click.prevent="gotoHome">Home</a>
        <router-link class="text-lg font-medium hover:underline" to="/services">Services</router-link>
        <router-link class="text-lg font-medium hover:underline" to="/about">About</router-link>
        <router-link class="text-lg font-medium hover:underline" to="/contact">Contact</router-link>
        <button @click="$router.push('/booking')" class="px-3 py-1 text-lg font-medium border border-main-700 focus:outline-none">Book Now</button>
      </div>

      <!-- Mobile -->
      <a @click="open=!open" class="md:hidden">
        <svg v-if="!open" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </a>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      showServices: false,
      open: false,
    }
  },
  methods: {
    gotoHome() {
      if (this.$route.path !== '/') {
        this.$router.push('/')
      }

      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
    },
  }
}
</script>