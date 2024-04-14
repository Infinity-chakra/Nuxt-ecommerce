<template>
  <header>
    <nav>
      <div>
        <h3>
          NUXT ECommerce 
        </h3>
      </div>
      <div>
        <NuxtLink to="/items" class="link">Item</NuxtLink>
        <NuxtLink to="/" class="link">Home</NuxtLink>
        <NuxtLink to="/about" class="link">About</NuxtLink>
        <NuxtLink to="/profile" class="link">Profile</NuxtLink>
      </div>
    </nav>
  </header>
</template>
<script setup>

import { ref } from 'vue'
const drawer = ref(false)
const menu = ref([
  { title: 'Home', icon: 'mdi-home' },
  { title: 'About', icon: 'mdi-information' },
  { title: 'Contact', icon: 'mdi-email' },
])

const toggleMenu = () => {
  console.log('Toggle')
  drawer.value = !drawer.value
}

</script>

<style>
nav {
  background-color: aquamarine;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.link {
  padding: 0.50rem 0.75rem;
  border-radius: 2%;
  box-shadow: 0 0 5px white;
  margin: auto 0.5rem;
  background-color: blue;
  color: white;
  text-decoration: none;
  min-width: 100px;
  text-align: center;
  font-size: 1rem;
  transition: all 0.3s ease-in-out;
}

.link:hover {
  color: black;
  background-color: white;
  transition: all 0.3s ease-in-out;
}
</style>