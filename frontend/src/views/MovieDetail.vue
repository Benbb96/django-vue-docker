<template>
  <v-container>
    <div v-if="store.selectedMovie === null" class="text-center">
      <v-progress-circular indeterminate></v-progress-circular>
    </div>

    <div v-else>
      <h1 class="text-h2 text-center font-weight-bold mb-10">
        {{store.selectedMovie.title}}
      </h1>

      <v-row>
        <v-col cols="12" sm="4">
          <v-card>
            <v-card-title>Actors</v-card-title>
            <v-card-text>
              <v-list v-if="store.selectedMovie.actors.length">
                <v-list-item v-for="actorId in store.selectedMovie.actors" :key="actorId">
                  {{store.getActorDisplay(actorId)}}
                </v-list-item>
              </v-list>
              <p v-else>
                No actor in this movie...
              </p>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" sm="8">
          <p v-if="store.selectedMovie.description">
            Description : <span class="font-italic">{{store.selectedMovie.description}}</span>
          </p>
          <p v-else>No description.</p>

          <p v-if="store.selectedMovie.review_set.length">
            Average grade : <v-chip>{{store.averageGradeForSelectedMovie}} / 5</v-chip>
          </p>

          <AddReview :movie-id="route.params.id"></AddReview>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup>
import {useAppStore} from "@/store/app"
import {useRoute} from "vue-router"
import {onMounted} from "vue"
import AddReview from "@/components/AddReview.vue"

const store = useAppStore()
const route = useRoute()

onMounted(async () => {
  // Fetch movie if it's not in store
  if (!store.selectedMovie) {
    await store.fetchMovie(route.params.id)
  }
})
</script>

<style scoped>
p {
  margin-bottom: 1em;
}
</style>

