<template>
  <div>
    <Header />
    <router-view />
    <scrollbutton />
  </div>
  <Footer />
</template>
<script setup>
import Footer from './pages/footer.vue';
import Header from './pages/header.vue';
import scrollbutton from './pages/scrollbutton.vue';

</script>
