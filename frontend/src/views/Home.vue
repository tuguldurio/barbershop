<template>
  <div> 
    <div id="hero1" class="relative overflow-hidden h-screen bg-cover bg-center-left bg-no-repeat">
      <div class="relative h-full w-full bg-main-900 bg-opacity-50">
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <h1 class="text-white uppercase text-4xl lg:text-6xl text-center font-fira font-bold">Great Haircut<br> Great Service</h1>
          <button class="block item-center font-bold rounded-none focus:outline-none mx-auto w-auto mt-6 px-5 py-3 lg:px-10 lg:py-6 text-md lg:text-xl text-main-700 bg-white hover:bg-main-100" @click="$router.push({path: '/booking'})" color="secondary">Book Now</button>
        </div>
      </div>
    </div>

    <div class="container mx-auto flex flex-col md:flex-row md:space-x-10 p-16">
      <div class="text-center">
        <div class="uppercase font-quicksand">
          <p class="relative text-2xl md:text-4xl font-bold text-main-500">Gentleman</p>
          <p class="relative text-5xl md:text-6xl">Services</p>
        </div>

        <div class="my-4">Barbershop is a full service grooming parlour for the discerning gentleman. We offer a wide variety of services that will certainly make you the talk of the town. Click below to see what we have to offer.</div>
      </div>
      <img class="w-full md:w-1/2 object-cover mx-auto" src="@/assets/carlos-magno-7tllY5pwe4s-unsplash.jpg" alt="">
    </div>

    <div id="hero2" class="relative overflow-hidden h-168 bg-cover bg-top-1 bg-no-repeat">
      <div class="relative h-full w-full bg-main-900 bg-opacity-30">
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <h1 class="text-white uppercase text-3xl lg:text-6xl text-center font-fira font-bold">Look Good<p class="md:inline mx-4">✦</p>Feel Good</h1>
          <button class="block item-center font-bold rounded-none focus:outline-none mx-auto w-auto mt-6 px-5 py-3 lg:px-10 lg:py-2 text-md lg:text-xl text-main-700 bg-white hover:bg-main-100" @click="$router.push({path: '/services'})" color="secondary">Services</button>
        </div>
      </div>
    </div>

    <div class="container mx-auto flex flex-col md:flex-row md:space-x-10 p-16">
      <div class="w-full md:w-1/3 text-center">
        <p class="text-xl font-semibold uppercase mb-2">Follow</p>
        <div class="flex justify-center space-x-2">
          <img class="w-8 cursor-pointer" src="@/assets/icons/logo-facebook.svg"/>
          <img class="w-8 cursor-pointer" src="@/assets/icons/logo-instagram.svg"/>
          <img class="w-8 cursor-pointer" src="@/assets/icons/logo-twitter.svg"/>
        </div>
      </div>
      <div class="w-full md:w-1/3 text-center">
        <p class="text-xl font-semibold uppercase mb-2">Address</p>
        <p>12345 AA 12th St Street, ABCDEF, AB 12345</p>
        <p>info@barbershop.com</p>
        <p>+1-541-754-3010</p>
      </div>
      <div class="w-full md:w-1/3 text-center">
        <p class="text-xl font-semibold uppercase mb-2">Opening Hours</p>
        <p>Mon - Fri: 9am - 8pm</p>
        <p>Saturday: 9am - 7pm</p>
        <p>Sunday: 10am - 6pm</p>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style lang="scss">
#hero1 {
  background-image: url('~@/assets/nathon-oski-EW_rqoSdDes-unsplash.jpg');
}
#hero2 {
  background-image: url('~@/assets/carlos-magno-B-J7He9XaBE-unsplash.jpg');
}
</style>