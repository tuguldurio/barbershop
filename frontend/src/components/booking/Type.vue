<template>
  <div class="w-full mx-auto space-y-4">
    <p>Please select service to book:</p>
    
    <RadioGroup v-model="selected">
      <RadioGroupLabel class="sr-only">Server size</RadioGroupLabel>
        <div class="space-y-2">
          <RadioGroupOption
            as="template"
            v-for="service in services"
            :key="service.name"
            :value="service"
            v-slot="{ active, checked }"
          >
            <div
              :class="[
                active
                  ? 'ring-2 ring-offset-2 ring-offset-light-blue-300 ring-white ring-opacity-60'
                  : '',
                checked
                  ? 'bg-main-400 bg-opacity-75 text-black '
                  : 'bg-white',
              ]"
              class="relative flex px-5 py-4 rounded-lg shadow-md cursor-pointer focus:outline-none"
              @click="next(service.name)"
            >
              <div class="flex items-center space-x-4 w-full">
                <div class="flex-shrink-0 text-white w-6 h-6" :class="[checked ? 'visible' : 'visible']">
                  <svg class="w-full h-full" viewBox="0 0 24 24" fill="none">
                    <circle
                      cx="12"
                      cy="12"
                      r="12"
                      fill="#333"
                      fill-opacity="0.2"
                    />
                    <path
                      v-show="checked"
                      d="M7 13l3 3 7-7"
                      stroke="#fff"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </div>

                <div class="flex items-center">
                  <div class="text-sm">
                    <RadioGroupLabel
                      as="p"
                      :class="checked ? 'text-white' : 'text-gray-900'"
                      class="text-base font-medium"
                    >
                      {{ service.name }}
                    </RadioGroupLabel>
                    <RadioGroupDescription
                      as="span"
                      :class="checked ? 'text-white' : 'text-gray-500'"
                      class="inline"
                    >
                      <span>{{ service.price }}</span>
                    </RadioGroupDescription>
                  </div>
                </div>
                
              </div>
            </div>
          </RadioGroupOption>
        </div>
      </RadioGroup>
  </div>
</template>

<script>
import {
  RadioGroup,
  RadioGroupLabel,
  RadioGroupOption,
} from "@headlessui/vue"

const services = [
  {
    name: "Haircut",
    price: '50$',
  },
  {
    name: "Beard Trim",
    price: '$45'
  },
  {
    name: "Kid's cur",
    price: '30$'
  },
]

export default {
  components: { RadioGroup, RadioGroupLabel, RadioGroupOption },
  data() {
    return {
      selected: null,
      services
    }
  },
  methods: {
    next(type) {
      this.$emit('next', type)
    }
  }
}
</script>