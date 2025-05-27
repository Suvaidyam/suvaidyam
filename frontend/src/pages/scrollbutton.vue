<template>
  <button 
    v-show="showScrollToTop" 
    @click="scrollToTop" 
    class="fixed right-5 bottom-10 z-50 w-10 h-10  text-white bg-blue-700 rounded-full flex items-center justify-center cursor-pointer duration-500 focus:outline-none "
  >
    <svg 
      stroke="currentColor" 
      fill="currentColor" 
      stroke-width="0" 
      viewBox="0 0 16 16" 
      class="w-4 h-4"
    >
      <path 
        fill-rule="evenodd" 
        clip-rule="evenodd" 
        d="M13.854 7l-5-5h-.707l-5 5 .707.707L8 3.561V14h1V3.56l4.146 4.147.708-.707z"
      />
    </svg>
  </button>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const showScrollToTop = ref(false)

const handleScroll = () => {
  showScrollToTop.value = window.pageYOffset > 300
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>