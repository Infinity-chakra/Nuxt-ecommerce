<template>
  <div>
    <p>About Page</p>
  </div>
</template>
<script setup>
const isOpen = ref(false);
import { useCounterStore } from "~/store/counter"; // Assuming auto-imports

const counterStore = useCounterStore();

onMounted(() => {
  console.log("Mounted ..");
  console.log("Counter Value:", counterStore.count);
});
</script>
