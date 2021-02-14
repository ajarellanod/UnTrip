<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <h1>We Are Testing VueJS</h1>
    <Navbar />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar
  }
};
</script>
