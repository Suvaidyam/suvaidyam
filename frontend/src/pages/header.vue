<template>
     <header class="w-full h-20 fixed top-0 bg-white z-[3000] shadow">
      <div class="w-full h-full max-w-[1720px] mx-auto flex px-5 lg:px-20 justify-between">
        <div class="h-full flex items-center">
          <router-link to="/">
            <img 
              class="w-1/2 md:w-1/3 lg:w-1/4" 
              src="../assets/images/suvaidyam logo.png" 
              alt="Suvaidyam Logo"
            >
          </router-link>
        </div>
        
        <div class="h-full flex items-center justify-center">
          <!-- Desktop Navigation -->
          <div class="hidden lg:block">
            <div class="flex gap-8 items-center">
              <div class="flex gap-6">
                <router-link 
                  class="font-semibold text-[15px] hover:text-slate-500 text-blue-900" 
                  to="/about"
                >
                  About Us
                </router-link>
                <router-link 
                  class="font-semibold text-[15px] hover:text-slate-500 text-blue-900" 
                  to="/work"
                >
                  Where We Work
                </router-link>
                <router-link 
                  class="font-semibold text-[15px] hover:text-slate-500 text-blue-900" 
                  to="/contact"
                >
                  Contact Us
                </router-link>
              </div>
              <router-link to="/involved">
                <button class="w-48 h-10 text-[10px] font-bold border-[1.5px] border-blue-900 hover:bg-blue-900 hover:text-white tracking-widest duration-500">
                  GET INVOLVED
                </button>
              </router-link>
            </div>
          </div>
          
          <!-- Mobile Menu Button -->
        
        </div>
      </div>
    </header>

</template>
<script setup></script>