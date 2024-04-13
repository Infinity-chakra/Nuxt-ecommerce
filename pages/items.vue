<template>
  <div>
    <p>Items</p>
    <p v-if="isLoading">Loading ...</p>
    <v-container v-else fluid>
      <v-row>
        <v-col cols="12" sm="4" md="4" lg="4" v-for="n in 3" :key="n">
          <v-card v-for="item in items" :key="item.id" class="card-margin">
            <v-card-title>
              {{ item.title }}
            </v-card-title>
            <v-card-text>
              <p>
                By <v-chip color="primary">{{ item.brand }}</v-chip>
              </p>
              <p>
                Original Price <v-chip color="primary">{{ item.mrp }}</v-chip>
              </p>
              <p>
                Discount <span class="data">{{ item.discount }} %</span
                >
              </p>
              <p>
                Discounted Price
                <v-chip color="primary">{{ item.price}}</v-chip>
              </p>
              <p>
                Average Rating <span class="data">{{ item.rating }}</span>
              </p>
              <p>
                Total Ratings <span class="data">{{ item.totalRating }}</span>
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
import { ref, onMounted, computed } from "vue";

const isOpen = ref(false);
const data = ref(null);
const itemStore = useItem();

const items = computed(() => itemStore.getItemList);
const isLoading = computed(() => itemStore.isLoading);

const openLink = (url) => {
  window.open(url, "_blank");
};

onMounted(async () => {
  await itemStore.getItemsAction();
});
</script>

<style>
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
  padding: 0.50rem;
  background-color: bisque;
}
</style>
