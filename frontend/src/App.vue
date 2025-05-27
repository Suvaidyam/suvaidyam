<template>
  <div>
    <Header />
	<ScrollToTopButton />
    <router-view />
  </div>
  <Footer />
</template>
<script setup>
import Footer from './pages/footer.vue';
import Header from './pages/header.vue';
import ScrollToTopButton from './pages/ScrollToTopButton.vue';
</script>
