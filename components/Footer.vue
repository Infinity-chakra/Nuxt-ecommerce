<template>
  <v-footer color="secondary" app>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6">
          <p>
            &copy; {{ new Date().getFullYear() }} <strong>Ecommerce Nuxt App</strong>
          </p>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script setup>
import { ref } from "vue";
</script>
