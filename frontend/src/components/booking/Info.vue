<template>
  <div class="w-11/12 md:w-144 mx-auto">
    <form @submit.prevent="submit">
      <div>
        <label class="block">Name:</label>
        <div class="flex">
          <input v-model="info.firstname" type="text" placeholder="First Name" class="w-1/2 mt-2 mr-2 py-2 px-3 appearance-none bg-white border border-gray-300 rounded-none outline-none">
          <input v-model="info.lastname" type="text" placeholder="Last Name" class="w-1/2 mt-2 ml-2 py-2 px-3 appearance-none bg-white border border-gray-300 rounded-none outline-none">
        </div>
      </div>
      <div class="mt-2">
        <label class="block">Email</label>
        <input v-model="info.email" type="email" placeholder="Email" class="w-full mt-2 py-2 px-3 appearance-none bg-white border border-gray-300 rounded-none outline-none">
      </div>
      <div class="mt-2">
        <label class="block">Phone</label>
        <input v-model="info.phone" type="tel" placeholder="Phone" class="w-full mt-2 py-2 px-3 appearance-none bg-white border border-gray-300 rounded-none outline-none">
      </div>
      <div class="mt-2">
        <label class="block">Any message for us?</label>
        <textarea v-model="info.notes" name="" id="" cols="30" rows="10" class="w-full mt-2 py-2 px-3 appearance-none bg-white border border-gray-300 rounded-none outline-none resize-none"></textarea>
      </div>
      
      <div class="flex mt-2">
        <Button @click="$emit('back')" color="secondary" class="mr-4">Back</Button>
        <Button>Complete</Button>
      </div>
    </form>    
  </div>
</template>

<script>
import Button from '../Button.vue'

export default {
  components: {
    Button
  },
  data() {
    return {
      info: {
        firstname: '',
        lastname: '',
        email: '',
        phone: '',
        notes: ''
      }
    }
  },
  methods: {
    submit() {
      this.$emit('submitInfo', this.info)
    }
  }
}
</script>