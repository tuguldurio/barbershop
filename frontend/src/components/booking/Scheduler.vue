<template>
  <div class="w-11/12 md:w-168 h-168 md:h-96 mx-auto flex flex-col md:flex-row md:divide-x divide-black divide-opacity-10 select-none">
    <div class="w-full md:w-1/2 h-1/2 md:h-full pt-2 flex flex-col">
      <div class="flex items-center justify-center">
        <svg class="w-8 cursor-pointer transform scale-100" @click="prevMonth" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>

        <div class="w-44 text-lg text-center font-medium">{{year}} {{monthName}}</div>

        <svg class="w-8 cursor-pointer" @click="nextMonth" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
      </div>

      <div class="flex-grow grid grid-cols-7 grid-rows-7">
        <div class="w-full h-full flex items-center justify-center">Sun</div>
        <div class="w-full h-full flex items-center justify-center">Mon</div>
        <div class="w-full h-full flex items-center justify-center">Tue</div>
        <div class="w-full h-full flex items-center justify-center">Wed</div>
        <div class="w-full h-full flex items-center justify-center">Thu</div>
        <div class="w-full h-full flex items-center justify-center">Fri</div>
        <div class="w-full h-full flex items-center justify-center">Sat</div>
        <div class="w-full h-full flex items-center justify-center" :class="'col-start-'+dateStart()" ></div>
        <div class="w-full h-full flex items-center justify-center" v-for="day in daysInMonth" :key="day.format('YYYY:MM:DD')"
          :class="daysClass(day)"
          @click="toggleDay(day)"
        >
          {{day.date()}}
        </div>
      </div>
    </div>
    <div class="relative h-44 md:h-auto p-4 space-y-6">
      <p>Which hour would you like to choose?</p>

      <select v-model="selectedHour">
        <option value="null" disabled>Select hour</option>
        <template v-for="avail in available" :key="avail.format('YYYY:MM:DD')">
          <option v-if="selectedDay && avail.format('YYYY:MM:DD') == selectedDay.format('YYYY:MM:DD')">
            <span>{{avail.format('hh:mm A')}}</span>
          </option>
        </template>
      </select>

      <Button v-if="!firstStep" class="absolute bottom-8" @click="$emit('back')" color="secondary">Back</Button>
      <Button class="absolute bottom-8" :class="[firstStep ? '' : 'left-24']" @click="nextStep" :disabled="selectedHour==null || selectedDay==null">Continue</Button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import Button from '@/components/Button.vue'

export default {
  components: {
    Button
  },
  props: {
    firstStep: Boolean
  },
  data() {
    const date = moment()
    return {
      date: date,
      year: date.year(),
      month: date.month(),
      monthName: date.format('MMMM'),
      daysInMonth: [],
      available: [],
      selectedDay: null,
      selectedHour: null
    }
  },
  mounted() {
    this.date = moment()
    this.date.set({hour:0, minute:0, second:0, millisecond:0})
    this.fetchAvailableDates()
    this.daysInMonth = this.getDaysInMonth()
  },
  watch: {
    month() {
      this.monthName = this.date.format('MMMM')
      this.year = this.date.year()
      this.daysInMonth = this.getDaysInMonth()
    }
  },
  methods: {
    async fetchAvailableDates() {
      const res = await axios.get('/api/bookings/available')
      res.data.dates.forEach(e => {
        this.available.push(moment.utc(e.date, 'YYYY-MM-DD HH:mm').local())
      })
    },
    getDaysInMonth() {
      let count =  this.date.month(this.month).daysInMonth();
      let days = [];

      for (let i = 1; i < count+1; i++) {
        days.push(this.date.clone().month(this.month).date(i))
      }
      return days
    },
    /** Functions to change date */
    prevMonth() {
      if (this.date > moment()) {
        this.date.subtract(1, 'M')
        this.month = this.date.month()
      }
    },
    nextMonth() {
      this.date.add(1, 'M')
      this.month = this.date.month()
    },

    /** Utility functions for calendar */
    dateStart() {
      let first = this.date.startOf('month')
      return first.weekday()
    },
    checkAvailable(day) {
      for (let i = 0; i < this.available.length; i++) {
        if (day.format('YYYY:MM:DD') == this.available[i].format('YYYY:MM:DD')) {
          return true
        }
      }
      return false
    },
    daysClass(day) {
      return [
        this.checkAvailable(day) ? 'hover:underline font-extrabold cursor-pointer' : 'font-light text-gray-800',
        {' bg-main-500 text-white': this.checkAvailable(day) && (this.selectedDay && this.selectedDay.format('YYYY:MM:DD') == day.format('YYYY:MM:DD'))},
      ]
    },
    toggleDay(day) {
      if (this.checkAvailable(day)) {
        if (this.selectedDay == null) {
          this.selectedDay = day
        }
        else {
          if (day != this.selectedDay) {
            this.selectedDay = day
            this.selectedHour = null
          }
          else {
            this.selectedDay = null
            this.selectedHour = null
          }
        }
      }
    },
    nextStep() {
      const fake = moment(' 00-01-01 '+this.selectedHour, 'YY-MM-DD hh:mm A')
      this.selectedDay.hour(fake.hour())
      this.selectedDay.minute(fake.minute())
      this.selectedDay.second(0)
      this.$emit('next', this.selectedDay)
    }
  }
}
</script>