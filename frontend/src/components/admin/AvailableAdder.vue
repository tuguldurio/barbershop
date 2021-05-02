<template>
  <div class="mx-auto flex flex-col divide-black divide-opacity-10 select-none">
    <!-- Calendar -->
    <div class="w-full sm:w-96 h-96 pt-2 flex flex-col">
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
    <!-- Extra -->
    <div class="relative h-44 md:h-auto p-4 space-y-6">
      <div v-if="selectedDay">
        <p class="mb-2 font-medium">Add available hour</p>

        <div class="max-w-min flex">
          <div class="flex p-2 border border-main-600">
            <select v-model="addingHour.hour" class="px-2 appearance-none outline-none cursor-pointer">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
              <option value="7">7</option>
              <option value="8">8</option>
              <option value="9">9</option>
              <option value="10">10</option>
              <option value="11">11</option>
              <option value="12">12</option>
            </select>
            <span class="mx-1">:</span>
            <select v-model="addingHour.min" class="px-2 appearance-none outline-none cursor-pointer">
              <option value="0">00</option>
              <option value="30">30</option>
            </select>
            <select v-model="addingHour.ampm" class="px-2 appearance-none outline-none cursor-pointer">
              <option value="AM">AM</option>
              <option value="PM">PM</option>
            </select>
          </div>
          <div>
            <Button class="w-full h-full p-2" @click="addHour">Add</Button>
          </div>
        </div>

        <div v-if="addingError" class="text-red-600">
          {{addingError}}
        </div>

        <div class="mt-4">
          <p class="mb-2 font-medium">Added hours</p>
          <div v-for="hour in addedHours" :key="hour">
            <p class="text-lg">{{hour.date}} <span v-if="hour.booked"> - Booked</span></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import Button from '@/components/Button'

const date = moment()
date.set({hour:0, minute:0, second:0, millisecond:0})

export default {
  components: {
    Button
  },
  data() {
    return {
      year: date.year(),
      month: date.month(),
      monthName: date.format('MMMM'),
      daysInMonth: [],
      selectedDay: null,
      selectedHour: null,
      addedHours: [],
      addingHour: {
        hour: 1,
        min: 0, 
        ampm: 'AM'
      },
      addingError: null
    }
  },
  created() {
    this.daysInMonth = this.getDaysInMonth()
  },
  watch: {
    month() {
      this.monthName = date.format('MMMM')
      this.year = date.year()
      this.daysInMonth = this.getDaysInMonth()
    },
    selectedDay(newValue) {
      if (newValue) {
        this.fetchAddedHours()
      }
      this.addingError = null
    }
  },
  methods: {
    async fetchAddedHours() {
      const res = await axios.get('/api/bookings/admin/added', {params: {day: this.selectedDay.toDate()}})
      this.addedHours = []
      res.data.dates.forEach(e => {
        this.addedHours.push({
          date: moment.utc(e.date).local().format('hh:mm A'),
          booked: e.booked
        })
      })
    },
    getDaysInMonth() {
      let count =  date.month(this.month).daysInMonth();
      let days = [];

      for (let i = 1; i < count+1; i++) {
        days.push(date.clone().month(this.month).date(i))
      }
      return days
    },
    /** Functions to change date */
    prevMonth() {
      if (date > moment()) {
        date.subtract(1, 'M')
        this.month = date.month()
      }
    },
    nextMonth() {
      date.add(1, 'M')
      this.month = date.month()
    },
    /** Utility functions for calendar */
    dateStart() {
      let first = date.startOf('month')
      return first.weekday()
    },
    checkAvailable(day) {
      return day > moment()
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
          }
          else {
            this.selectedDay = null
          }
        }
      }
    },
    async addHour() {
      const payload = moment(`${this.selectedDay.format('YYYY-MM-DD')} ${this.addingHour.hour}:${this.addingHour.min} ${this.addingHour.ampm}`, 'YYYY-MM-DD hh:mm A')
      try {
        await axios.post('/api/bookings/admin/add', {date: payload.toDate()})
        this.addingError = null
        this.fetchAddedHours()
      }
      catch (err) {
        if (err.response.status === 409) {
          this.addingError = err.response.data.message
        }
      }
    }
  }
}
</script>