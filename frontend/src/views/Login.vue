<template>
  <div v-if="loaded" class="container mx-auto">
    <div class="w-128 mx-auto">
      <FormFields 
        title="Login"
        :fieldsConfig="{
          email: 'email',
          password: 'password'
        }"
        action="login"
        @success="loginSuccess"
      />
    </div>
  </div>
</template>

<script>
import FormFields from '@/components/FormFields.vue'

export default {
  components: {
    FormFields
  },
  data() {
    return {
      loaded: false
    }
  },
  created() {
    if (this.$store.getters.loggedIn) {
      this.$router.push(this.$route.query.redirect || '/')
    }
    else {
      this.loaded = true
    }
  },
  methods: {
    loginSuccess() {
      this.$router.push(this.$route.query.redirect)
    },
  },
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn
    }
  },
  watch: {
    loggedIn(newValue) {
      if (newValue) {
        this.$router.push(this.$route.query.redirect || '/')
      }
    }
  }
}
</script>

<style>

</style>