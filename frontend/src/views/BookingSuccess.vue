<template>
  <div class="container mx-auto mt-24 text-center">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 mx-auto text-main-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
    <div class="my-4">
      <p class="text-xl md:text-2xl"><span>{{$route.params.firstname}} {{$route.params.lastname}}</span>, You successfully created your booking!</p>
      <p class="text-lg md:text-xl">{{$route.params.date}}</p>
      <p>{{$route.params.info}}</p>
    </div>
    <Button class="mx-auto" @click="cancel">Cancel Booking</Button>
  </div>
</template>

<script>
import axios from 'axios'
import Button from '../components/Button'

export default {
  components: {
    Button
  },
  methods: {
    async cancel() {
      try {
        const res = await axios.post('/api/bookings/cancel', {id: this.$route.params.id})
        if (res.status === 200) {
          alert('Booking cancelled.')
          this.$router.push('/')
        }
      } 
      catch (err) {
        alert('Something went wrong!')
      }
    }
  },
  beforeRouteEnter (to, from, next) {
    if (from.path == '/booking') {
      next()
    }
    else {
      next({path: '/'})
    }
  },
}
</script>

<style>

</style>