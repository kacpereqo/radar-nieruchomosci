<template>
  <NavBar />
  <router-view />
  <Footer />
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    NavBar,
    Footer,
  },
};
</script>

<style>
.wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  flex: 1;
}

* {
  position: relative;
  z-index: 10;
}

#app {
  display: flex;
  flex-direction: column;
}

body {
  font-family: 'Roboto', sans-serif;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
</style>
