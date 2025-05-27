<template>
  <div id="app" class="min-h-screen flex flex-col">
    <!-- Header -->
      <!-- <Navbar/> -->
    <!-- Main Content -->
    <main class="w-full h-full max-w-[1800px] mx-auto">
      <!-- Hero Carousel -->
      <section class="w-full mt-20">
        <div class="carousel-container relative">
          <div class="relative w-full overflow-hidden">
            <div
              class="flex transition-transform duration-1000 ease-in-out"
              :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
            >
              <div
                v-for="(slide, index) in slides"
                :key="index"
                class="w-full flex-shrink-0"
              >
                <img
                  :src="slide.image"
                  :alt="slide.alt"
                  class="w-full h-[200px] md:h-[460px] lg:h-[600px] object-cover"
                >
              </div>
            </div>

            <!-- Carousel Controls -->
            <button
              @click="prevSlide"
              class="absolute left-4 top-1/2  transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2 rounded-full hover:bg-opacity-75"
            >
              &#8249;
            </button>
            <button
              @click="nextSlide"
              class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2 rounded-full hover:bg-opacity-75"
            >
              &#8250;
            </button>

            <!-- Carousel Dots -->
            <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
              <button
                v-for="(slide, index) in slides"
                :key="index"
                @click="goToSlide(index)"
                :class="[
                  'w-3 h-3 rounded-full transition-colors',
                  currentSlide === index ? 'bg-white' : 'bg-white bg-opacity-50'
                ]"
              ></button>
            </div>
          </div>
        </div>
      </section>

      <!-- Title Section -->
      <section class="pl-6 md:text-center">
        <h1 class="text-blue-900 pt-7 font-serif md:text-[85px] text-[40px] font-bold">
          SUVAIDYAM
        </h1>
        <p class="text-sm md:text-xl text-blue-900 md:-mt-5"></p>
      </section>

      <!-- About Section -->
      <section class="block md:flex w-full pb-4 pt-10 px-6 md:pb-16 md:px-5 md:gap-10 lg:gap-24">
        <div class="md:w-1/2 md:flex justify-end">
          <div class="lg:w-[365px]">
            <div class="md:flex items-center md:gap-5">
              <div>
                <div class="border-t w-20 border-red-500 hidden md:block"></div>
              </div>
              <div>
                <p class="font-thin md:text-xs text-[16px] tracking-widest">
                  Bridging the technology gap
                </p>
              </div>
            </div>
            <div class="md:pt-6 pt-2 font-serif text-[27px] lg:text-[35px] md:text-3xl w-full text-blue-900">
              <p>Every individual deserves to reach their full potential and we want to make sure that happens</p>
            </div>
          </div>
        </div>

        <div class="md:w-1/2 flex">
          <div class="lg:w-[410px] md:text-[17.5px] text-[20px] font-serif text-black tracking-wide">
            <p>Indian villages have the potential to serve as centres of advanced technology and innovation. Our primary objective is to empower rural India by revolutionising the way we teach and upskill its youth.</p>
            <p class="pt-6">We are working towards removing the barriers that keep rural India out of the tech ecosystem. We want its youth to be able to dream big and chase opportunities in tech.</p>
            <p class="pt-6">Our goal therefore is to provide easy access to technical infrastructure, education and opportunities to rural India and empower individuals, families, and in turn rural communities to thrive and grow.</p>
            <router-link to="/about" class="underline md:text-xs text-[17px] md:text-[14.2px] md:mt-7 mt-2 tracking-widest inline-block">
              MORE ABOUT US
            </router-link>
          </div>
        </div>
      </section>

      <!-- Image and Why Section -->
      <section class="w-full block lg:flex md:gap-10 lg:gap-6">
        <div class="lg:w-[50%]">
          <img
            src="../assets/images/members.jpeg"
            class="md:h-[580px] w-full object-cover"
            alt="Group of people"
          >
        </div>
        <div class="lg:w-[50%] md:text-start text-center px-6">
          <div class="lg:pl-16 md:text-center lg:text-start">
            <h2 class="font-extrabold md:text-[55px] text-[45px] tracking-[12px] text-blue-900 pt-8">
              WHY
            </h2>
            <p class="font-bold text-[#0C1D39] pb-8 text-lg tracking-widest">
              JOIN HANDS
            </p>
            <div class="md:text-[18px] lg:w-[365px] md:px-32 lg:px-0 text-[18px] font-serif text-blue-900 tracking-wide">
              <p>Barriers such as lack of guidance, exposure, infrastructure and resources prevent the youth of rural India to dream of a career in the technology space. Together we can break down those barriers that are holding them back.</p>
              <p class="pt-5">Help us in bridging the gap that is keeping rural India out of the life-changing tech industry.</p>
            </div>
            <router-link to="/involved">
              <button class="md:w-40 w-48 lg:text-[12px] md:text-[11px] text-[15px] md:h-12 h-12 md:mt-16 mt-7 font-bold md:border-[2px] border-[3px] border-blue-900 hover:bg-blue-900 duration-700 text-blue-900 hover:text-white md:tracking-widest tracking-[3px]">
                GET INVOLVED
              </button>
            </router-link>
          </div>
        </div>
      </section>

      <!-- Partners Section -->
      <section class="flex justify-center">
        <div class="w-full md:flex justify-between px-6 max-w-[1230px] lg:px-24 xl:px-48 items-center mt-20">
          <div>
            <h2 class="font-serif text-blue-900 text-[29px] lg:text-5xl md:text-[36px]">
              Partner Organizations
            </h2>
          </div>
          <div class="flex md:justify-center md:gap-4">
            <div class="md:w-16 w-9 mt-4 border-gray-500 md:border-t border-t-2"></div>
            <div class="font-thin text-[18px] hidden md:block tracking-wider">
              LEADING IN THE INDUSTRY
            </div>
          </div>
        </div>
      </section>

      <!-- Partner Logos -->
      <section class="w-full h-auto md:h-40 px-6 lg:px-24 xl:px-48 mt-6 md:mt-2 mb-10 flex justify-center">
        <div class="w-full h-full flex gap-8 md:gap-10 max-w-[850px] flex-wrap items-center justify-center">
          <div class="logo">
            <a href="https://dhwaniris.com" target="_blank" rel="noopener noreferrer">
              <img
                src="../assets/images/dhwanilogo.png"
                class="w-full h-full"
                alt="Dhwani RIS"
              >
            </a>
          </div>
          <div class="logo">
            <a href="https://www.capitalaircom.com" target="_blank" rel="noopener noreferrer">
              <img
                src="../assets/images/capital.jpeg"
                class="capital w-full h-full"
                alt="Capital Air"
              >
            </a>
          </div>
        </div>
      </section>

      <!-- Quote Section -->
      <section class="md:h-[480px] w-full py-10 justify-center flex items-center px-6 text-center bg-[#0C1D39] text-white">
        <div>
          <p class="md:text-[38px] text-[29px] font-thin tracking-wider">
            A little guidance goes a long way...
          </p>
          <div class="border-t-4 mt-5 md:mx-[46.5%] mx-[43%]"></div>
          <div class="mt-5 font-sans text-[17.5px]">
            <p>We are empowering the youth of rural India to choose careers in the tech domain</p>
            <p>by providing them mentorship every step of the way.</p>
          </div>
          <div class="pt-5 font-sans text-[17.5px]">
            <p>We are bringing technical infrastructure to our villages in order to make them self-</p>
            <p>sustained technology hubs so that our youth is not forced to migrate to cities to</p>
            <p>pursue rewarding careers.</p>
            <p class="mt-12 font-bold tracking-widest">- Amresh Kumar, Founder</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onBeforeUnmount } from 'vue'
import image1 from '../assets/images/image1.jpg'
import image2 from '../assets/images/image2.jpg'


// Component name (not required in <script setup>, only useful in options API or defineOptions)
const currentSlide = ref(0)
const email = ref('')
const mobileMenuOpen = ref(false)
let carouselInterval = null

const slides = [
  {
    image: image1,
    alt: 'Suvaidyam Hero Image 1'
  },
  {
    image: image2,
    alt: 'Suvaidyam Hero Image 2',
    height: '460px'
  }
]

const startCarousel = () => {
  carouselInterval = setInterval(() => {
    nextSlide()
  }, 5000)
}

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.length
}

const prevSlide = () => {
  currentSlide.value = currentSlide.value === 0 ? slides.length - 1 : currentSlide.value - 1
}

const goToSlide = (index) => {
  currentSlide.value = index
}

onMounted(() => {
  startCarousel()
})

onBeforeUnmount(() => {
  if (carouselInterval) {
    clearInterval(carouselInterval)
  }
})
</script>


<style scoped>
/* Custom styles for better visual appearance */
.carousel-container {
  position: relative;
  overflow: hidden;
}

/* Mobile menu styles if needed */


/* Smooth transitions */
.transition-all {
  transition: all 0.3s ease;
}

/* Custom scrollbar for better UX */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

/* Ensure proper image aspect ratios */
img {
  max-width: 100%;
  /* height: auto; */
}

.capital{
  height: 90px;
}

/* Button hover effects */
button {
  transition: all 0.3s ease;
}

/* Link hover effects */
a {
  transition: color 0.3s ease;
}

/* Hero section typography */
h1 {
  line-height: 1.1;
}

/* Responsive typography adjustments */
@media (max-width: 768px) {
  .text-responsive {
    font-size: clamp(1rem, 4vw, 1.5rem);
  }
}

/* Focus states for accessibility */
button:focus,
a:focus{
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

/* Loading states */
.loading {
  opacity: 0.7;
  pointer-events: none;
}

/* Animation classes */
.fade-in {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.slide-in-right {
  animation: slideInRight 0.5s ease-out;
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Grid layout improvements */
.grid-auto-fit {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* Form styling improvements */
input[type="email"] {
  transition: border-color 0.3s ease;
}

input[type="email"]:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* Social media icon hover effects */
.social-icon {
  transition: transform 0.3s ease;
}

.social-icon:hover {
  transform: translateY(-2px);
}

/* Carousel dot styling */
.carousel-dots button {
  transition: all 0.3s ease;
}

.carousel-dots button:hover {
  transform: scale(1.2);
}

/* Card hover effects for future use */
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

/* Text selection styling */
::selection {
  background-color: #3b82f6;
  color: white;
}

/* Improved accessibility for screen readers */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Loading spinner */
.spinner {
  border: 2px solid #f3f3f3;
  border-top: 2px solid #3b82f6;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
