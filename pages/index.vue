<template>
  <div>
    <p>Home Page</p>
    <p v-if="isLoading">
      Loading ...
    </p>
    <v-container v-else>
      <v-row>
        <v-col>
          <v-card  v-for="item in items" :key="item.id"> 
            <v-card-title>
              {{ item.id }}
            </v-card-title>
            <v-card-text>
              {{ item.title }}
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
// calls on server
// const { data } = await useFetch('https://jsonplaceholder.typicode.com/todos')

// console.log(data)

const items = ref([]);
const isLoading = ref(false);

const apiCall = async () => {
  try {
    const response = await axios.get("https://jsonplaceholder.typicode.com/todos"); 
    console.log('response', response.data)
    items.value = response.data;
  } catch (error) {
    console.error(error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(async () => {
  isLoading.value = true;
  await apiCall();
});
</script>
