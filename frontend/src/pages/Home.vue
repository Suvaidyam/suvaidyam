<template>
  <div id="app" class="min-h-screen flex flex-col">
    <!-- Header -->
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
          <div class="block lg:hidden">
            <button @click="toggleMobileMenu" class="text-4xl cursor-pointer">
              <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" class="w-6 h-6">
                <path fill-rule="evenodd" d="M3 6.75A.75.75 0 013.75 6h16.5a.75.75 0 010 1.5H3.75A.75.75 0 013 6.75zM3 12a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75A.75.75 0 013 12zm0 5.25a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75a.75.75 0 01-.75-.75z" clip-rule="evenodd"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </header>

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
              class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-black bg-opacity-50 text-white p-2 rounded-full hover:bg-opacity-75"
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
            <p class="font-bold text-blue-900 pb-8 text-lg tracking-widest">
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
      <section class="md:h-[480px] w-full py-10 justify-center flex items-center px-6 text-center bg-blue-900 text-white">
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
     
        

    <!-- Footer -->
    <footer class="w-full mt-auto">
  <!-- Main footer content -->
          <div class="w-full max-w-[1720px] mx-auto h-auto py-7 px-6 md:px-12 lg:px-24 xl:px-30">
            <div class="flex flex-col gap-3 ">
              <h3 class="text-[40px] md:text-[46px] font-serif">SUPPORT US</h3>
              <div class="relative w-[268px] flex justify-end items-center">
                <span class="h-[1px] bg-blue-700 w-[40px] absolute left-0"></span>
                <span class="text-right h-6 z-50 font-light text-[16px]">Your support means saved lives</span>
              </div>
              <button class="bg-blue-900 text-white text-[10px] tracking-widest border-[1.5px] border-blue-900 w-28 h-9 font-extrabold hover:bg-white hover:text-blue-900 duration-500">
                DONATE
              </button>
        </div>
            <div class="w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-10 lg:gap-24 items-start">
              <!-- Support Us -->
              <div class="flex flex-col gap-6">
              
                <div class="flex flex-col gap-2 mt-4">
                  <p class="font-semibold text-lg">Registered Office</p>
                  <p class="font-serif text-sm font-medium">VILLINTEL SUVAIDYAM PRIVATE LIMITED</p>
                  <p class="font-light text-sm text-gray-600">
                    CIN - U62099DL2024PTC436726<br> 
                    PAN - AAKCV4369C<br> 
                    TAN - DELV29114B
                  </p>
                </div>
              </div>

              <!-- Address -->
              <div>
                <p class="font-semibold text-lg mb-4">Address</p>
                <div class="flex flex-col gap-3 text-sm text-gray-600">
                  <p>
                    F-374/C GF BLOCK -F, AYA NAGAR EXTN PH-6,<br>
                    South Delhi - 110047
                  </p>
                  <p>+91-8308623995</p>
                  <a href="mailto:tech@suvaidyam.com" class="text-gray-600">
                    tech@suvaidyam.com
                  </a>
                </div>
              </div>

              <!-- Get Involved -->
              <div>
                <p class="font-semibold text-lg mb-4">GET INVOLVED</p>
                <p class="text-sm text-gray-600">
                  Let's combine forces to make a<br>difference together
                </p>
              </div>

              <!-- Join Us -->
              <div>
                <p class="font-semibold text-lg mb-4">JOIN US</p>
                
                <div class="flex flex-col gap-4">
                  <div class="flex gap-3">
                    <a href="https://www.instagram.com/suvaidyam/" target="_blank" rel="noopener noreferrer">
                      <div class="w-8 h-8 rounded-full bg-pink-500 flex items-center justify-center text-white">
                        <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" class="w-4 h-4">
                          <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"></path>
                        </svg>
                      </div>
                    </a>
                    <a href="https://whatsapp.com/channel/0029VaAg20iG3R3rCSYYjL30" target="_blank" rel="noopener noreferrer">
                      <div class="w-8 h-8 rounded-full bg-green-500 flex items-center justify-center">
                        <svg stroke="currentColor" fill="white" stroke-width="0" viewBox="0 0 448 512" class="w-5 h-5">
                          <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"></path>
                        </svg>
                      </div>
                    </a>
                    <a href="https://www.youtube.com/@suvaidyam/featured" target="_blank" rel="noopener noreferrer">
                      <div class="w-8 h-8 rounded-full bg-red-500 flex items-center justify-center">
                        <svg stroke="currentColor" fill="white" stroke-width="0" viewBox="0 0 576 512" class="w-5 h-5">
                          <path d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"></path>
                        </svg>
                      </div>
                    </a>
                    <a href="https://www.linkedin.com/company/suvaidyam/?originalSubdomain=in" target="_blank" rel="noopener noreferrer">
                      <div class="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white">
                        <svg stroke="currentColor" fill="currentColor" stroke-width="0" version="1.1" viewBox="0 0 16 16" class="w-4 h-4">
                          <path d="M6 6h2.767v1.418h0.040c0.385-0.691 1.327-1.418 2.732-1.418 2.921 0 3.461 1.818 3.461 4.183v4.817h-2.885v-4.27c0-1.018-0.021-2.329-1.5-2.329-1.502 0-1.732 1.109-1.732 2.255v4.344h-2.883v-9z"></path>
                          <path d="M1 6h3v9h-3v-9z"></path>
                          <path d="M4 3.5c0 0.828-0.672 1.5-1.5 1.5s-1.5-0.672-1.5-1.5c0-0.828 0.672-1.5 1.5-1.5s1.5 0.672 1.5 1.5z"></path>
                        </svg>
                      </div>
                    </a>
                  </div>
                  
                  <!-- Newsletter Signup -->
                  <div class="flex gap-2">
                    <input 
                      v-model="email"
                      name="email" 
                      type="email" 
                      placeholder="Enter email address" 
                      class="border-2 flex-1 px-3 py-2 border-blue-900 placeholder:text-sm placeholder:font-light outline-none text-sm font-light"
                      required
                    >
                    <button 
                      type="submit" 
                      class="px-4 py-2 border-2 border-blue-900 hover:bg-blue-900 hover:text-white duration-500 text-xs font-extrabold tracking-widest"
                    >
                      JOIN
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Copyright -->
          <div class="w-full bg-blue-400 h-16">
            <div class="w-full max-w-[1250px] h-full lg:px-[185px] flex items-center lg:justify-start">
              <p class="text-white font-light text-sm px-6">
                © 2023 by Suvaidyam, Saran, Bihar
              </p>
            </div>
          </div>
    </footer>

    <!-- Scroll to Top Button -->
    <button 
      v-show="showScrollToTop"
      @click="scrollToTop"
      class="w-10 cursor-pointer flex justify-center items-center text-white text-xl duration-500 h-10 z-50 bg-sky-600 rounded-full fixed right-5 bottom-10 hover:bg-sky-700"
    >
      <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" class="w-4 h-4">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M13.854 7l-5-5h-.707l-5 5 .707.707L8 3.561V14h1V3.56l4.146 4.147.708-.707z"></path>
      </svg>
    </button>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onBeforeUnmount } from 'vue'
import image1 from '../assets/images/image1.jpg'
import image2 from '../assets/images/image2.jpg'

// Component name (not required in <script setup>, only useful in options API or defineOptions)
const currentSlide = ref(0)
const showScrollToTop = ref(false)
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

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const handleScroll = () => {
  showScrollToTop.value = window.pageYOffset > 300
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const submitNewsletter = () => {
  if (email.value) {
    console.log('Newsletter subscription:', email.value)
    alert('Thank you for subscribing to our newsletter!')
    email.value = ''
  }
}

onMounted(() => {
  startCarousel()
  window.addEventListener('scroll', handleScroll)
})

onBeforeUnmount(() => {
  if (carouselInterval) {
    clearInterval(carouselInterval)
  }
  window.removeEventListener('scroll', handleScroll)
})
</script>


<style scoped>
/* Custom styles for better visual appearance */
.carousel-container {
  position: relative;
  overflow: hidden;
}

/* Mobile menu styles if needed */
@media (max-width: 1023px) {
  .mobile-menu {
    position: fixed;
    top: 80px;
    left: 0;
    right: 0;
    background: white;
    z-index: 2000;
    padding: 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  }
}

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
a:focus,
input:focus {
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