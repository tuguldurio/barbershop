<template>
  <div class="container mx-auto">
    <div class="w-11/12 sm:max-w-3xl mx-auto my-8 p-8 shadow">
      <Type v-if="step===0" @next="nextToScheduler" />
      <Scheduler v-if="step===1" @back="backToType" @next="nextToInfo" :firstStep="this.$route.query.type ? true : false" />
      <Info v-if="step===2" @back="backToScheduler" @submitInfo="submit" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import Type from '@/components/booking/Type.vue'
import Scheduler from '@/components/booking/Scheduler.vue'
import Info from '@/components/booking/Info.vue'

export default {
  components: {
    Type,
    Scheduler,
    Info,
  },
  data() {
    return {
      step: 0,
      date: null,
      booking: {
        type: null,
        info: null
      }
    }
  },
  created() {

  },
  methods: {
    back() {
      this.step -= 1
    },
    backToScheduler() {
      this.booking.info = null
      this.date = null
      this.back()
    },
    backToType() {
      this.date = null
      this.booking.type = null
      this.back()
    },

    next() {
      this.step += 1
    },
    nextToScheduler(type) {
      this.booking.type = type
      this.next()
    },
    nextToInfo(date) {
      this.date = date
      this.next()
    },
    submit(info) {
      this.booking.info = info
      this.submitDatas()
    },
    async submitDatas() {
      try {
        const res = await axios.post('/api/bookings/make', {
          date: this.date.toDate(),
          booking: this.booking
        })

        if (res.status === 201) {
          this.$router.push({name: 'BookingSuccess', params: {
            id: res.data.id,
            date: this.date.format('dddd, MMMM Do, YYYY h:mm at A'),
            type: this.booking.type,
            ...this.booking.info
          }})
        }
        else alert('Something went wrong!')
      }
      catch (error) {
        console.log(error.response)
      }
    }
  }
}
</script>