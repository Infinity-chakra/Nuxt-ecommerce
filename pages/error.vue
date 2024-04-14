<template>
    <div class="error-page">
      <h1>404 - Not Found</h1>
      <p>The page you requested could not be found.</p>
      <NuxtLink to="/">Go back to home</NuxtLink>
    </div>
  </template>
  
  <script setup>
  // Add any data, methods, or computed properties you need for your error page
  </script>
  
  <style scoped>
    .error-page {
        text-align: center;
        margin-top: 20px;
    }
  </style>