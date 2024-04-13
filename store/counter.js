import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', () => {
  return {
    count: 0,
    increment() {
      this.count++;
    },
  };
});