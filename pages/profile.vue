<template>
  <NuxtLayout name="error">
    <v-container fluid>
      <v-row class="item-container">
        <v-col cols="12" sm="6" md="6" lg="6">
          <h2>PROFILE</h2>

          <p>
            This is an Ecommerce website created using Nuxt JS. It uses an API
            built with Django Rest Framework. You can search for items, view
            items, and paginate through the items.
          </p>
        </v-col>
        <v-col cols="12" sm="6" md="6" lg="6">
          <img src="/static/images/eshop.png" alt="Image" />
        </v-col>
      </v-row>
    </v-container>
  </NuxtLayout>
</template>
<script setup>
definePageMeta({
  middleware: ["auth"],
});
</script>
