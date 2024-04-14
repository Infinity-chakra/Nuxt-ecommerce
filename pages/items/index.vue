<template>
  <div>
    <v-container fluid>
      <v-row class="item-container">
        <v-col cols="12" sm="6" md="6" lg="6">
          <h2>ITEMS</h2>
          <div class="paginator">
            <v-btn
              color="primary"
              @click="goToPage('previous')"
              class="ma-1"
              :disabled="correctedPageNumber === 1"
              >Previous Page</v-btn
            >
            <v-btn color="primary" @click="goToPage('next')" class="ma-1"
              >Next Page</v-btn
            >
            <span>Total Pages {{ Math.ceil(items.count / 10) }}</span>
            <v-text-field
              class="page-input"
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
    <Loader v-if="isLoading" />
    <v-container v-else fluid>
      <v-row>
        <v-col
          v-for="item in items.results"
          :key="item.id"
          cols="12"
          sm="4"
          md="4"
          lg="4"
        >
          <v-card class="card-margin bg-green.darken1">
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
              <v-btn color="secondary" @click="goToDetail(item.id)">
                View Details
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
import { useRouter } from "nuxt/app";

const searchText = ref("");
const currentPage = ref(1);
const itemStore = useItem();
const router = useRouter();

const items = computed(() => itemStore.getItemList);
const isLoading = computed(() => itemStore.isLoading);

// Page number validation
const correctedPageNumber = computed(() => {
  return Math.max(currentPage.value, 1);
});

useHead({
  title: "Items",
  meta: [
    {
      hid: "description",
      name: "description",
      content:
        "This is an Ecommerce website created using Nuxt JS. It uses an API built with Django Rest Framework. You can search for items, view items, and paginate through the items.",
    },
  ],
});

const openLink = (url) => {
  window.open(url, "_blank");
};

const goToDetail = async (itemId) => {
  // Navigate to items route with params
  console.log("Item ID", itemId);
  await navigateTo(`/items/${itemId}`);
};

const onSearch = async () => {
  await itemStore.getItemsAction(1, searchText.value);
};

const goToPage = async (type) => {
  currentPage.value = parseInt(currentPage.value);
  if (type === "next") {
    currentPage.value += 1;
  } else {
    if (currentPage.value > 0) {
      currentPage.value -= 1;
    }
  }
  await itemStore.getItemsAction(correctedPageNumber.value, searchText.value);
};

const goToPageNumber = async () => {
  await itemStore.getItemsAction(correctedPageNumber.value, searchText.value);
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

.page-input {
  width: 300px;
  margin-top: 0.75rem;
}
</style>
