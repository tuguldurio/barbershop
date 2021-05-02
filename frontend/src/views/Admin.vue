<template>
  <div class="container mx-auto">
    <div class="flex flex-col md:flex-row ">
      <div class="w-full md:w-1/2 p-4 flex flex-col space-y-4">
        <div>
          <a @click="fetchBookings" class="cursor-pointer">Refresh</a>
          <a @click="logout" class="cursor-pointer">Logout</a>
        </div>
        <div v-for="(booking, index) in bookings" :key="index" class="p-4 border border-main-600">
          <div>
            <p class="text-lg font-medium">{{booking.date}}</p>
            <p class="text-lg">Type: {{booking.booking.type}}</p>
          </div>
          <div>
            <p>
              {{booking.booking.info.firstname}}
              {{booking.booking.info.lastname}}
            </p>
            <p>{{booking.booking.info.email}}</p>
            <p>{{booking.booking.info.phone}}</p>
            <p>{{booking.booking.info.notes}}</p>
          </div>
        </div>
      </div>
      <div class="w-full md:w-1/2 p-4">
        <DateAdder/>
      </div>
    </div>
  </div>
</template>

<script>
import axios  from 'axios'
import moment from 'moment'
import DateAdder from '../components/admin/AvailableAdder.vue'

export default {
  components: {
    DateAdder
  },
  data() {
    return {
      bookings: []
    }
  },
  created() {
    this.fetchBookings()
  },
  methods: {
    async fetchBookings() {
      const res = await axios.get('/api/bookings/admin/bookings')
      this.bookings = []
      res.data.bookings.forEach(e => {
        this.bookings.push({
          date: moment.utc(e.date).local().format('YYYY-MM-DD hh:mm A'),
          booking: e.booking
        })
      })
    },
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>

</style>