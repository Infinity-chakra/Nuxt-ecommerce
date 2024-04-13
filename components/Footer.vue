<template>
  <v-footer color="primary" app>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6">
          <v-card-title class="white--text"> Footer Content </v-card-title>
          <v-card-text class="white--text">
            This is a Vuetify footer example.
          </v-card-text>
        </v-col>
        <v-col cols="12" sm="6">
          <v-card-title class="white--text"> Links </v-card-title>
          <v-card-text class="white--text">
            <v-list>
              <v-list-item
                v-for="(link, index) in links"
                :key="index"
                link
                class="white--text"
              >
                {{ link }}
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script setup>
import { ref } from "vue";

const links = ref(["Home", "About", "Contact"]);
</script>
