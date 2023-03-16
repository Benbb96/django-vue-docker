<template>
  <v-app>
    <default-bar />

    <default-view />

    <v-snackbar v-model="store.snackbar.display" :color="store.snackbar.color">
      {{ store.snackbar.text }}

      <template v-slot:actions>
        <v-btn variant="text" @click="store.snackbar.display = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script setup>
import {useAppStore} from "@/store/app"
import DefaultBar from './AppBar.vue'
import DefaultView from './View.vue'

const store = useAppStore()
</script>
