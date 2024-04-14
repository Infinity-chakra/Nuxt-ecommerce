<template>
  <v-container class="footer" fluid>
      <v-row>
        <v-col cols="12" sm="6">
          <p>
            &copy; {{ new Date().getFullYear() }} <strong>Ecommerce Nuxt App</strong>
          </p>
        </v-col>
      </v-row>
    </v-container>
</template>

<script setup>
import { ref } from "vue";
</script>

<style scoped>
.footer {
  background-color: aquamarine;
  color: white;
  text-align: center;
  padding: 10px;
}
</style>