<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100 px-4">
        <!-- Registration Form - Show when not registered -->
        <div v-if="!isRegistrationSuccessful" class="max-w-md w-full bg-white p-8 rounded-xl shadow-lg">
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
                    <label class="block text-gray-700 font-medium mb-1">Address</label>
                    <input
                        type="text"
                        placeholder="Enter your Address"
                        v-model="Address"
                        required
                        class="w-full  px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
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

        <!-- Success Message - Show when registration is successful -->
        <div v-if="isRegistrationSuccessful" class="max-w-md w-full bg-blue-400 p-8 rounded-xl shadow-lg animate-fade-in">
            <h2 class="text-[50px] font-bold text-center text-gray-800 mb-6">THANK YOU</h2>
            <p class="text-[20px] text-center text-blue-900 mb-4">Your registration is successful</p>
            <p class="text-[20px] text-center text-blue-900 mb-4">Suvaidyam team will reach you soon</p>
            <div class="flex justify-center">
                <img class="w-32 md:w-40 lg:w-48" src="../assets/images/suvaidyam_logo-removebg-preview.png" alt="Suvaidyam Logo"/>
            </div>
        </div>
    </div>
</template>
 
<script setup>
import { useRouter } from 'vue-router'
import { inject, ref } from 'vue'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

const call = inject('call')
const StudentName = ref('')
const email = ref('')
const Address = ref('')
const mobile = ref('')
const password = ref('')
const confirmPassword = ref('')
const isRegistrationSuccessful = ref(false)
const router = useRouter()

const register = async () => {
    if (password.value !== confirmPassword.value) {
        alert('Passwords do not match.');
        return;
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
                address: Address.value,
            }
        );

        if (response.message) {
            isRegistrationSuccessful.value = true;
            console.log("Registering student...", response.message);
            toast.success('Registration successful!', { autoClose: 4000 });

            setTimeout(() => {
                router.push('/');
            }, 5000);
        } else {
            toast.error(response.error, { autoClose: 4000 });
        }

    } catch (error) {
        toast.error(error.message || 'An error occurred during registration.', { autoClose: 4000 });
    }
};

</script>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.5s ease-in-out;
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
</style>