<template>
  <div class="w-11/12 md:w-168 h-168 md:h-96 mx-auto space-y-4">
    <p>Choose your desired type:</p>
  
    <div class="flex items-center h-20 p-4 hover:bg-main-100 border border-gray-300" @click="next('Haircut')">
      <label class="font-medium">Haircut</label>
    </div>
    <div class="flex items-center h-20 p-4 hover:bg-main-100 border border-gray-300" @click="next('Haircut & Shave')">
      <label class="font-medium">Haircut & Shave</label>
    </div>
    <div class="flex items-center h-20 p-4 hover:bg-main-100 border border-gray-300" @click="next('Beard Trim')">
      <label class="font-medium">Beard Trim</label>
    </div>
  </div>
</template>

<script>

export default {
  methods: {
    next(type) {
      this.$emit('next', type)
    }
  }
}
</script>