import { defineStore } from "pinia";
import { ref } from "vue";
import httpClient from "../utils/interceptor";

export const useItem = defineStore("item", {
  state: () => ({
    item: ref({}),
    itemList: ref([]),
    loading: ref(false),
  }),

  getters: {
    getItem() {
      return this.item;
    },
    getItemList() {
      return this.itemList;
    },
    isLoading() {
      return this.loading;
    },
  },

  actions: {
    async getItemsAction(page = 1, searchText = "") {
      try {
        this.loading = true;
        const response = await httpClient.get(`items`, {
          params: {
            page: page,
            search: searchText,
          },
        });
        if (response) {
          this.itemList = response.data;
          this.loading = false;
        }
      } catch (error) {
        console.log(error);
      } finally {
        this.loading = false;
      }
    },

    async getItemDetailAction(id) {
      try {
        this.loading = true;
        const response = await httpClient.get(`items/${id}`);
        this.item = response.data;
      } catch (error) {
        console.log(error);
        return error;
      } finally {
        this.loading = false;
      }
    },

    resetItemData() {
      this.item = {};
      this.itemList = [];
    },
  },
});
