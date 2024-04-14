<template>
  <div class="has-background-light">
    <HeaderComponent />
    <slot />
    <FooterCompoenent />
  </div>
</template>

<script setup>
import HeaderComponent from "@/components/Header.vue";
import FooterCompoenent from "@/components/Footer.vue";
</script>

<style></style>
