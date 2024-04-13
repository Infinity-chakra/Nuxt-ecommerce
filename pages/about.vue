<template>
  <div>
    <p>About Page</p>
    <p v-if="isLoading">
      Loading ...
    </p>
    <v-container v-else>
      <v-row>
        <v-col>
          <v-card v-for="item in data" :key="item.id">
            <v-card-title>
              {{ item.title }}
            </v-card-title>
            <v-card-text>
              {{ item.description }}
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
import { useCounterStore } from "~/store/counter"; // Assuming auto-imports
import { ref, onMounted } from "vue";
import httpClient from "~/utils/interceptor";

const isOpen = ref(false);
const data = ref(null);
const isLoading = ref(false);
const counterStore = useCounterStore();

const getApiData = async () => {
  try {
    isLoading.value = true;
    const response = await httpClient.get(`anime`);
    if (response.status === 200) {
      data.value = response.data.data;
    }
  } catch (error) {
    console.error(error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(async () => {
  console.log("Mounted ..");
  await getApiData();
  console.log("Counter Value:", counterStore.count);
});
</script>
