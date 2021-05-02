<template>
  <div class="container mx-auto flex flex-col md:flex-row my-8 px-8 md:px-0 md:space-x-8">
    <div class="w-full md:w-1/2">
      <p class="text-3xl font-medium">Contact Us</p>

      <div class="my-2">
        <svg class="w-6 inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
        </svg>
        <span class="text-lg align-middle">info@barbershop.com</span>
      </div>

      <div class="my-2">
        <svg class="w-6 inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
        </svg>
        <span class="text-lg align-middle">+1-541-754-3010</span>
      </div>

      <div class="my-2">
        <svg class="w-6 inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span class="text-lg align-middle">12345 AA 12th St Street, ABCDEF, AB 12345</span>
      </div>
    </div>

    <form class="w-full md:w-1/2 max-w-xl" @submit.prevent="send">
      <div>
        <label class="block">Name:</label>
        <input v-model="fullname" type="text" placeholder="Full Name" class="w-full mt-2 py-2 px-3 appearance-none border border-gray-300 rounded-none outline-none">
      </div>
      <div class="mt-2">
        <label class="block">Email</label>
        <input v-model="email" type="email" placeholder="Email" class="w-full mt-2 py-2 px-3 appearance-none border border-gray-300 rounded-none outline-none">
      </div>
      <div class="mt-2">
        <label class="block">Phone</label>
        <input v-model="phone" type="tel" placeholder="Phone" class="w-full mt-2 py-2 px-3 appearance-none border border-gray-300 rounded-none outline-none">
      </div>
      <div class="mt-2">
        <label class="block">Message</label>
        <textarea v-model="message" name="" id="" cols="30" rows="10" class="w-full mt-2 py-2 px-3 appearance-none border border-gray-300 rounded-none outline-none resize-non"></textarea>
      </div>
      
      <Button class="mt-2">Send</Button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

import Button from '../components/Button.vue'

export default {
  components: {
    Button
  },
  data() {
    return {
      fullname: '',
      email: '',
      phone: '',
      message: ''
    }
  },
  methods: {
    async send() {
      try {
        const res = await axios.post('/api/contact', {
          fullname: this.fullname,
          email: this.email,
          phone: this.phone,
          message: this.message
        })
        if (res.status === 200) {
          this.fullname = ''
          this.email = ''
          this.phone = ''
          this.message = ''
        }
      }
      catch (error) {
        console.log(error.response)
      }
    }
  }
}
</script>