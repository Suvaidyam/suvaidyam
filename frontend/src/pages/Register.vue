<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100 px-4">
        <div class="max-w-md w-full bg-white p-8 rounded-xl shadow-lg">
            <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Student Registration</h2>
            <form @submit.prevent="register">
                <div class="mb-4">
                    <label class="block text-gray-700 font-medium mb-1">Student Name</label>
                    <input
                        type="text"
                        placeholder="Enter your name"
                        v-model="StudentName"
                        required
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-medium mb-1">Email</label>
                    <input
                        type="email"
                        placeholder="Enter your email"
                        v-model="email"
                        required
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-medium mb-1">Aadhar No.</label>
                    <input
                        type="text"
                        placeholder="Enter your Aadhar number"
                        v-model="AadharNo"
                        required
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-medium mb-1">Mobile</label>
                    <input
                        type="tel"
                        placeholder="Enter your mobile number"
                        v-model="mobile"
                        required
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-medium mb-1">Password</label>
                    <input
                        type="password"
                        placeholder="Enter your password"
                        v-model="password"
                        required
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 font-medium mb-1">Confirm Password</label>
                    <input
                        type="password"
                        placeholder="Confirm your password"
                        v-model="confirmPassword"
                        required
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                </div>
                <button
                    type="submit"
                    class="w-full bg-[#001f3f] text-white py-2 rounded-lg hover:bg-[#0f375f]"
                >
                    Register
                </button>
            </form>
        </div>
    </div>
</template>
 
<script setup>
import { useRouter } from 'vue-router'
import { inject, ref } from 'vue'
const call =inject('call')
const StudentName = ref('')
const email = ref('')
const AadharNo = ref('')
const mobile = ref('')
const password = ref('')
const confirmPassword = ref('')
const router = useRouter()
const register = async () => {
    if (password.value !== confirmPassword.value) {
        alert('Passwords do not match.')
        return
    }
 
    try {
        const response = await call(
            'suvaidyam_portal.register.register_student',
            {
                student_name: StudentName.value,
                email: email.value,
                mobile: mobile.value,
                password: password.value,
                confirm_password: confirmPassword.value,
                aadhar_no: AadharNo.value,
            },
        )
        console.log("Registering student...",response.message)
    } catch (error) {
        alert(`Error: ${error.message}`)
    }
    router.push('/')
}
</script>

 