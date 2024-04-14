<template>
  <div>
    <Loader v-if="isLoading" />
    <v-container v-else fluid>
      <h2>ITEM - {{ item.title }}</h2>
      <v-row>
        <v-col cols="12" sm="6" md="4" lg="6">
          <v-card class="card-margin">
            <v-card-title>
              {{ item.brand }}
            </v-card-title>
            <v-card-text>
              <p>
                <span class="data">Price: {{ item.price }}</span>
              </p>
              <p>
                <span class="data">Discount: {{ item.discount }}</span>
              </p>
              <p>
                <span class="data">Rating: {{ item.rating }}</span>
              </p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="openLink(item.link)">
                Buy Now
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
import { useItem } from "~/store/item"; // Assuming auto-imports
import { onMounted, computed } from "vue";

const itemStore = useItem();
const route = useRoute()

const item = computed(() => itemStore.getItem);
const isLoading = computed(() => itemStore.isLoading);

useHead({
  title: "Item Detail",
  meta: [
    {
      hid: "description",
      name: "description",
      content:
        "Get the details of a specific Item",
    },
  ],
});

const openLink = (link) => {
  window.open(link, "_blank");
};

onMounted(async () => {
  await itemStore.getItemDetailAction(route.params._id);
});
</script>

<style scoped>
.card-margin {
  margin: 1rem;
}

p {
  margin: 0.75rem auto;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  padding: 0.5rem 1.5rem;
  justify-content: space-between;
}

.data {
  font-weight: bold;
  margin: 0.25rem;
  padding: 0.5rem;
  background-color: bisque;
}
</style>
