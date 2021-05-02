<template>
  <button class="px-4 py-2 block item-center font-bold rounded-none focus:outline-none"
    :class="classObject"
    :disabled="this.disabled"
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: 'main'
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    classObject() {
      return {
        'text-white bg-gray-200 border border-white cursor-default': this.disabled,
        'text-white hover:underline bg-main-600 hover:bg-main-700': this.color == 'main' && !this.disabled,
        'text-main-400 hover:underline bg-main-100 hover:bg-main-200 border border-main-400': this.color == 'secondary' && !this.disabled
      }
    }
  }
}
</script>

<style>
.yellow {
  box-shadow: 0px 5px 20px 0px rgb(249 215 76 / 50%);
}
</style>