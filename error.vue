<script setup lang="ts">
import type { NuxtError } from "#app";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

const props = defineProps({
  error: Object as () => NuxtError,
});

const handleError = () => clearError({ redirect: "/" });
</script>

<template>
  <div>
    <Header />
    <h2>{{ error.statusCode }}</h2>
    <p>The page you requested could not be found.</p>
    <button @click="handleError">Clear errors</button>
    <Footer />
  </div>
</template>

<style scoped>
.error-page {
  text-align: center;
  margin-top: 20px;
}
</style>
