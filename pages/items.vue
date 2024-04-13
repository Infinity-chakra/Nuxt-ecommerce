<template>
  <div>
    <p>About Page</p>
    <p v-if="isLoading">Loading ...</p>
    <div v-else>
      <p v-for="item in items" :key="item.id">
        {{ item.title }}
      </p>
    </div>
  </div>
</template>
<script setup>
import { useItem } from "~/store/item"; // Assuming auto-imports
import { ref, onMounted, computed } from "vue";

const isOpen = ref(false);
const data = ref(null);
const itemStore = useItem();

const items = computed(() => itemStore.getItemList);
const isLoading = computed(() => itemStore.isLoading);

onMounted(async () => {
  await itemStore.getItemsAction();
});
</script>
