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
    async getItemsAction(page = 1) {
      try {
        this.loading = true;
        const response = await httpClient.get(`items`, {
          params: {
            page: page,
          },
        });
        if (response) {
          this.itemList = response.data.results;
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
        const headers = {
          Authorization: `Bearer ${auth.authData.access}`,
        };
        const response = await httpClient.get("groups?page=" + page, {
          headers,
        });
        this.item = response.data;
      } catch (error) {
        console.log(error);
        return error;
      }
    },

    resetItemData() {
      this.item = {};
      this.itemList = [];
    },
  },
});
