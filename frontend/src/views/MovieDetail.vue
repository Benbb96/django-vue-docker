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

          <h2>Add a review</h2>
          <v-form @submit.prevent="submitReview">
            <v-slider
              label="Grade"
              v-model="newReview.value"
              :min="1"
              :max="5"
              :step="1"
              thumb-label
              :error-messages="newReview.errors"
            >
              <template #append>
                <v-btn type="submit" :loading="newReview.loading">
                  Send
                </v-btn>
              </template>
            </v-slider>
          </v-form>
        </v-col>
      </v-row>
    </div>
    <v-snackbar v-model="snackbar.display">
      {{ snackbar.text }}

      <template v-slot:actions>
        <v-btn color="pink" variant="text" @click="snackbar.display = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script setup>
import {useAppStore} from "@/store/app"
import {useRoute} from "vue-router"
import {onMounted, reactive} from "vue"

const store = useAppStore()
const route = useRoute()

onMounted(async () => {
  // Fetch movie if it's not in store
  if (!store.selectedMovie) {
    await store.fetchMovie(route.params.id)
  }
})

const newReview = reactive({
  value: null,
  errors: [],
  loading: false
})

let snackbar = reactive({
  text: '',
  display: false
})

const submitReview = async() => {
  newReview.errors = []
  newReview.loading = true
  const res = await fetch("http://localhost:8080/reviews/", {
    method: "post",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      movie: route.params.id,
      grade: newReview.value
    })
  })
  newReview.loading = false
  // Handle errors
  if (res.status === 400) {
    const errors = await res.json()
    newReview.errors = errors.grade
  } else {
    snackbar.display = true
    snackbar.text = 'Review is being added to this movie'
    newReview.value = null
  }
}
</script>

<style scoped>
p {
  margin-bottom: 1em;
}
</style>

