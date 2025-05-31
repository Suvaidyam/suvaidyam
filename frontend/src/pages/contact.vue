<template>
  <div class="flex flex-col lg:flex-row gap-20 max-w-[1720px] mx-auto mt-32 px-4">
    <!-- Contact Form Section -->
    <div class="h-full w-full lg:w-3/5 bg-[#FAFAFA]">
      <div class="lg:pb-20 px-6">
        <!-- Header Section -->
        <div class="md:pt-32 pt-5 items-center md:text-center">
          <p class="md:text-4xl text-3xl text-[#2c3e50] font-bold md:tracking-widest">
            HAVE QUESTIONS?
          </p>
          <div class="flex justify-start md:justify-center">
            <p class="border-[#0C1D39] w-10 border-t-[3px] mt-2"></p>
          </div>
          <p class="pt-5 tracking-[2px] md:text-[14px] text-[17px] md:px-20 lg:px-40">
            We have answers. Feel free to leave a message, and we will get back to you as soon as possible.
          </p>
        </div>

        <!-- Contact Form -->
        <div class="lg:px-30 md:px-10 mt-20">
          <form @submit.prevent="handleSubmit">
            <!-- Name Field -->
            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="form.fullName"
                name="full_name"
                type="text"
                autocomplete="off"
                id="full_name"
                class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-#0C1D39 peer"
                placeholder=" "
                :class="{ 'border-red-500': errors.fullName }"
              />
              <p v-if="errors.fullName" class="text-red-500 text-sm mt-1">
                Please enter your name
              </p>
              <label
                for="full_name"
                class="peer-focus:font-medium absolute text-gray-600 tracking-widest font-normal text-[15px] duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-[#0C1D39] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
              >
                NAME
              </label>
            </div>

            <!-- Email Field -->
            <div class="relative z-0 w-full mb-6 group">
              <input
                v-model="form.email"
                name="email"
                type="email"
                autocomplete="off"
                id="email"
                class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-[#0C1D39] peer"
                placeholder=" "
                :class="{ 'border-red-500': errors.email }"
              />
              <p v-if="errors.email" class="text-red-500 text-sm mt-1">
                Please enter a valid email address
              </p>
              <label
                for="email"
                class="peer-focus:font-medium absolute text-gray-600 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-[#0C1D39] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
              >
                EMAIL
              </label>
            </div>

            <!-- Message Field -->
              <div class="relative z-0 w-full mb-6 group">
              <textarea
                v-model="form.message"
                name="message"
                id="message"
                cols="30"
                rows="4"
                placeholder=" "
                class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-[#0C1D39] peer "
                :class="{ 'border-red-500': errors.message }"
              ></textarea>
              <p v-if="errors.message" class="text-red-500 text-sm mt-1">
                Please enter your message
              </p>
              <label
                for="message"
                class="peer-focus:font-medium absolute text-gray-600 tracking-widest font-normal text-[15px] duration-500 transform -translate-y-6 scale-75 bottom-1 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-[#0C1D39] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6 peer-focus:top-3"
              >
                MESSAGE
              </label>
            </div>

            <!-- Submit Button -->
            <div class="text-center">
              <button
                type="submit"
                :disabled="isSubmitting"
                class="w-full md:h-10 h-12 md:text-[11px] text-[20px] md:mt-16 font-bold md:font-extrabold border-[2px] border-[#0C1D39] bg-[#0C1D39] hover:bg-white duration-700 text-white hover:text-#0C1D39 tracking-[2px] disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {{ isSubmitting ? 'SENDING...' : 'SEND' }}
              </button>
            </div>

            <!-- Success Message -->
            <div v-if="showSuccess" class="text-center mt-4">
              <p class="text-green-600 font-semibold">
                Message sent successfully! We'll get back to you soon.
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Google Maps Section -->
    <div class="w-full lg:w-2/5">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3591.026368601712!2d84.86815507600447!3d25.835676405543246!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3992b3006a6ec4b3%3A0x998d01f7712e7ad9!2sSuvaidyam!5e0!3m2!1sen!2sin!4v1721372561111!5m2!1sen!2sin"
        class="w-full h-full min-h-[400px] lg:min-h-[600px] border-0"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="Google Maps Embed"
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'
import { inject } from 'vue'


const emit = defineEmits(['form-submitted'])
const call = inject('call')


const form = reactive({
  fullName: '',
  email: '',
  message: ''
})

const errors = reactive({
  fullName: false,
  email: false,
  message: false
})

const isSubmitting = ref(false)
const showSuccess = ref(false)

const validateForm = () => {
  errors.fullName = !form.fullName.trim()
  errors.email = !form.email.trim() || !isValidEmail(form.email)
  errors.message = !form.message.trim()
  
  return !Object.values(errors).some(error => error)
}

const isValidEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
}

const handleSubmit = async () => {
  if (!validateForm()) {
    return
  }
  
  isSubmitting.value = true
  
  try {
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // Store form data before reset for emit
    const formData = await call('suvaidyam_portal.contact.submit_question', {
      fullName: form.fullName,
      email: form.email,
      message: form.message
    }
    );
    console.log('Form submitted:', formData);
    
    
    // Reset form and show success message
    Object.assign(form, {
      fullName: '',
      email: '',
      message: ''
    })
    showSuccess.value = true
    
    // Hide success message after 3 seconds
    setTimeout(() => {
      showSuccess.value = false
    }, 3000)
    
    // Emit event to parent component
    emit('form-submitted', formData)
    
  } catch (error) {
    console.error('Error submitting form:', error)
  } finally {
    isSubmitting.value = false
  }
}

// Clear errors when user starts typing
watch(() => form.fullName, () => {
  if (errors.fullName) {
    errors.fullName = false
  }
})

watch(() => form.email, () => {
  if (errors.email) {
    errors.email = false
  }
})

watch(() => form.message, () => {
  if (errors.message) {
    errors.message = false
  }
})
</script>

<style scoped>
/* Custom styles for the floating labels */
.peer:focus ~ label,
.peer:not(:placeholder-shown) ~ label {
  @apply transform scale-75 -translate-y-6;
}

/* Smooth transitions for form elements */
input, textarea {
  transition: border-color 0.3s ease;
}

input:focus, textarea:focus {
  border-color:#0C1D39;
}

/* Custom scrollbar for textarea */
textarea::-webkit-scrollbar {
  width: 4px;
}

textarea::-webkit-scrollbar-track {
  background: #f1f1f1;
}

textarea::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 2px;
}

textarea::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>