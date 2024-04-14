<template>
  <div>
    <v-container fluid>
      <v-row class="item-container">
        <v-col cols="12" sm="6" md="6" lg="6">
          <h2>ITEMS</h2>
          <div class="paginator">
            <v-btn color="primary" @click="goToPage('next')" class="ma-1"
              >Next Page</v-btn
            >
            <v-btn color="primary" @click="goToPage('previous')" class="ma-1" :disabled="currentPage === 1"
              >Previous Page</v-btn
            >
            <span>Total Pages {{ Math.ceil(items.count/10) }}</span>
            <v-text-field
                v-model="currentPage"
                @keyup.enter="goToPageNumber"
                label="Go to Page Number"
                type="number"
                placeholder="Enter page number"
                outlined
                dense
            ></v-text-field>
          </div>
        </v-col>
        <v-col cols="12" sm="6" md="6" lg="6">
          <v-row>
            <v-col cols="12" sm="8" md="8" lg="8">
              <v-text-field
                v-model="searchText"
                @keyup.enter="onSearch"
                label="Search"
                outlined
                dense
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="4" md="4" lg="4">
              <v-btn color="primary" @click="onSearch" append-icon="mdi-magnify"
                >Search</v-btn
              >
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <p v-if="isLoading">Loading ...</p>
    <v-container v-else fluid>
      <v-row>
        <v-col cols="12" sm="4" md="4" lg="4" v-for="n in 3" :key="n">
          <v-card
            v-for="item in items.results"
            :key="item.id"
            class="card-margin"
          >
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
                Discount <span class="data">{{ item.discount }} %</span>
              </p>
              <p>
                Discounted Price
                <v-chip color="primary">{{ item.price }}</v-chip>
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

const searchText = ref("");
const data = ref(null);
const currentPage = ref(1);
const itemStore = useItem();

const items = computed(() => itemStore.getItemList);
const isLoading = computed(() => itemStore.isLoading);

const openLink = (url) => {
  window.open(url, "_blank");
};

const onSearch = async () => {
  await itemStore.getItemsAction(1, searchText.value);
};

const goToPage = async (type) => {
  if (type === "next") {
    currentPage.value += 1;
  } else {
    if (currentPage.value > 0) {
      currentPage.value -= 1;
    }
  }
  await itemStore.getItemsAction(currentPage.value, searchText.value);
};

const goToPageNumber = async () => {
  await itemStore.getItemsAction(currentPage.value, searchText.value);
};

onMounted(async () => {
  await itemStore.getItemsAction();
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

.item-container {
  align-items: center;
  background-color: azure;
}
</style>
