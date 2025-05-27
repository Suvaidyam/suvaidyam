<template>
  <div id="scroll_btn">
    <button
      v-show="showScrollToTop"
      @click="scrollToTop"
      class="w-10 cursor-pointer flex justify-center items-center text-white text-xl duration-500 h-10 z-50 bg-sky-600 rounded-full fixed right-5 bottom-10 hover:bg-sky-700 focus:outline-none focus:ring-2 bg-blue-600 focus:ring-green-600 focus:border-green-600"
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
        ></path>
      </svg>
    </button>
  </div>
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
    behavior: 'smooth',
  })
}

let carouselInterval 
onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onBeforeUnmount(() => {
  if (carouselInterval) {
    clearInterval(carouselInterval)
  }
  window.removeEventListener('scroll', handleScroll)
})
</script>
