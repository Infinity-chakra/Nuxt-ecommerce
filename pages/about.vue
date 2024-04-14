<template>
  <div>
    <v-container fluid>
      <v-row class="item-container">
        <v-col cols="12" sm="6" md="6" lg="6">
          <h2>ABOUT</h2>
          
          <p>
            This is an Ecommerce website created using Nuxt JS. It uses an API built with Django Rest Framework.
            You can search for items, view items, and paginate through the items.
          </p>
        </v-col>
        <v-col cols="12" sm="6" md="6" lg="6">
          <img src="/static/images/eshop.png" alt="Image" />
        </v-col>
      </v-row>
    </v-container>
    
  </div>
</template>
<script setup>
// import { useCounterStore } from "~/store/counter"; // Assuming auto-imports
// import { ref, onMounted } from "vue";
// import httpClient from "~/utils/interceptor";

// const isOpen = ref(false);
// const data = ref(null);
// const isLoading = ref(false);
// const counterStore = useCounterStore();

// const getApiData = async () => {
//   try {
//     isLoading.value = true;
//     const response = await httpClient.get(`anime`);
//     if (response.status === 200) {
//       data.value = response.data.data;
//     }
//   } catch (error) {
//     console.error(error);
//   } finally {
//     isLoading.value = false;
//   }
// };

// onMounted(async () => {
//   console.log("Mounted ..");
//   await getApiData();
//   console.log("Counter Value:", counterStore.count);
// });
</script>
