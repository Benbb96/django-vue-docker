<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex text-center fill-height">
      <h1 class="text-h2 font-weight-bold mb-12">Movie Review</h1>

      <v-row v-if="store.isLoading">
        <v-col>
          <v-progress-circular indeterminate></v-progress-circular>
        </v-col>
      </v-row>
      <v-row v-else class="d-flex justify-center">
        <v-col v-for="movie in store.movies" :key="movie.id" cols="12" sm="6" md="4">
          <v-card :to="{name: 'MovieDetail', params: {id: movie.id}}" @click="store.selectedMovie = movie">
            <v-card-title>{{movie.title}}</v-card-title>
            <v-card-text>
              <p v-if="movie.description">
                Description : {{movie.description}}
              </p>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-center mt-10">
        <v-col>
          <v-btn v-if="store.previous" @click="store.page--" prepend-icon="mdi-arrow-left">
            Previous
          </v-btn>
        </v-col>
        <v-col>
          {{store.count}} film{{store.count > 1 ? 's' : ''}} au total
        </v-col>
        <v-col>
          <v-btn v-if="store.next" @click="store.page++" prepend-icon="mdi-arrow-right">
            Next
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup>
import {onMounted, watch} from "vue"
import {useAppStore} from "@/store/app"

const store = useAppStore()

onMounted(async () => {
  await store.fetchMovies()
})

watch(() => store.page, () => store.fetchMovies())
</script>

