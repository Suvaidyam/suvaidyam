<template>
  <div class="w-full h-full mt-20 md:mt-28 lg:mt-44 md:px-0 px-5">
    <!-- Main Content Section -->
    <div class="md:flex lg:gap-12 md:gap-5">
      <div class="md:w-[55%]">
        <img 
          src="../assets/images/involved.webp" 
          alt="" 
          class="float-right"
        >
      </div>
      <div class="md:w-[45%]">
        <p class="md:text-[83px] text-[60px] font-playfire w-40 lg:mt-36">
          Get involved.
        </p>
        <p class="md:text-[15px] text-[18px] w-[305px] lg:w-[410px] text-[#737D84] font-fontNunito mt-3">
          Your contribution, no matter how much, helps us to continue empowering rural India through tech.
        </p>
        <p class="md:text-[15px] text-[18px] w-[287px] lg:w-[400px] text-[#737D84] font-nunito md:mt-6 mt-2">
          Discover ways in which you can give and make a meaningful contribution towards our work.
        </p>
      </div>
    </div>

    <!-- Donate Section -->
    <div class="flex justify-start md:ml-64 mt-20">
      <div class="md:mx-20">
        <div>
          <h1 class="text-[28px] md:-ml-5">DONATE</h1>
          <img 
            src="../assets/images/donate.webp" 
            alt="" 
            class="w-56"
          >
        </div>
      </div>
    </div>

    <!-- Gratitude Section -->
    <div class="w-full bg-[#0C1D39] text-white mt-20 flex justify-center">
      <div>
        <p class="text-[35px] mt-20 font-fontgetDown tracking-[0.5px] px-5 text-center md:max-w-[850px]">
          We wish to express our heartfelt gratitude for your support of our efforts.
        </p>
        <p class="border-[1.5px] md:mx-[47.5%] mx-[43%] mt-4 mb-20"></p>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name: 'GetInvolved',
  data() {
    return {}
  }
}
</script>

<style scoped>
/* Custom CSS classes that might be needed */
.font-playfire {
  /* Add your custom font family */
  font-family: 'Playfair Display', serif;
}

.font-fontNunito {
  font-family: 'Nunito Sans', sans-serif;
}

.font-fontgetDown {
  /* Add your custom font family */
  font-family: 'Jost', sans-serif;
}

.bg-bgblue {
  /* Define your custom blue color */
  background-color: #1e40af; /* Example blue color */
}

.text-bgblue {
  color: #1e40af; /* Example blue color */
}

.border-bgblue {
  border-color: #1e40af; /* Example blue color */
}

.bg-bgfooter {
  background-color: #374151; /* Example footer color */
}

.text-fsm {
  font-size: 0.875rem; /* 14px */
}

/* Hover effects */
</style>