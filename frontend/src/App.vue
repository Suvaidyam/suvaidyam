<template>
  <div>
    <Header />
    <router-view />
  </div>
  <Footer />
</template>
<script setup>
import Footer from './pages/footer.vue';
import Header from './pages/header.vue';

</script>
