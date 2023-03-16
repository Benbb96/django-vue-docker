<template>
  <v-app-bar flat>
    <v-app-bar-title>
      <v-icon icon="mdi-movie" />
      Movie Review
    </v-app-bar-title>
    <v-btn :to="{name: 'Home'}" prepend-icon="mdi-view-list">Movie list</v-btn>
  </v-app-bar>
</template>

<script setup>
  //
</script>
