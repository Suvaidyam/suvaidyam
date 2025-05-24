<template>
  <header class="w-full h-20 fixed top-0 bg-white z-[3000] shadow">
    <div class="w-full h-full max-w-[1720px] mx-auto flex px-5 lg:px-20 justify-between items-center">
      <!-- Logo -->
      <router-link to="/" class="h-full flex items-center">
        <img
          class="w-32 md:w-40 lg:w-48"
          src="../assets/images/suvaidyam logo.png"
          alt="Suvaidyam Logo"
        />
      </router-link>

      <!-- Desktop Navigation: visible on lg and above -->
      <nav class="hidden lg:flex gap-8 items-center">
        <router-link
          class="font-semibold text-[15px] text-[#0C1D39] hover:text-gray-600"
          to="/about"
        >
          About Us
        </router-link>
        <router-link
          class="font-semibold text-[15px] text-[#0C1D39] hover:text-gray-600"
          to="/work"
        >
          Where We Work
        </router-link>
        <router-link
          class="font-semibold text-[15px] text-[#0C1D39] hover:text-gray-600"
          to="/contact"
        >
          Contact Us
        </router-link>
        <router-link to="/involved">
          <button
            class="w-48 h-10 text-[10px] font-bold border-[1.5px] border-[#0C1D39] text-[#0C1D39] hover:bg-[#0C1D39] hover:text-white tracking-widest duration-500"
          >
            GET INVOLVED
          </button>
        </router-link>
      </nav>

      <!-- Mobile Hamburger Button: visible below lg -->
      <button
        @click="toggleMobileMenu"
        class="lg:hidden focus:outline-none"
        aria-label="Toggle Menu"
      >
        <svg
          v-if="!mobileMenuOpen"
          class="w-8 h-8 text-[#0C1D39]"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          viewBox="0 0 24 24"
        >
          <path d="M3 12h18M3 6h18M3 18h18" />
        </svg>
        <svg
          v-else
          class="w-8 h-8 text-[#0C1D39]"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          viewBox="0 0 24 24"
        >
          <path d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <!-- Mobile Menu Dropdown -->
    <nav
      v-if="mobileMenuOpen"
      class="mobile-menu lg:hidden flex flex-col px-5 py-4 gap-4 text-[#0C1D39] bg-white shadow-md"
    >
      <router-link
        class="font-semibold text-lg hover:text-gray-600"
        to="/about"
        @click="closeMobileMenu"
      >
        About Us
      </router-link>
      <router-link
        class="font-semibold text-lg hover:text-gray-600"
        to="/work"
        @click="closeMobileMenu"
      >
        Where We Work
      </router-link>
      <router-link
        class="font-semibold text-lg hover:text-gray-600"
        to="/contact"
        @click="closeMobileMenu"
      >
        Contact Us
      </router-link>
      <router-link to="/involved" @click="closeMobileMenu">
        <button
          class="w-full h-10 text-[12px] font-bold border-[1.5px] border-[#0C1D39] text-[#0C1D39] hover:bg-[#0C1D39] hover:text-white tracking-widest duration-500"
        >
          GET INVOLVED
        </button>
      </router-link>
    </nav>
  </header>
</template>

<script setup>
import { ref } from "vue";

const mobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

const closeMobileMenu = () => {
  mobileMenuOpen.value = false;
};
</script>

<style scoped>
@media (max-width: 1023px) {
  .mobile-menu {
    position: fixed;
    top: 80px; /* height of header */
    left: 0;
    right: 0;
    background: white;
    z-index: 2000;
  }
}
</style>
