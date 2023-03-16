<template>
  <div v-if="state.editing" class="mb-8">
    <v-textarea
      label="Description"
      v-model="state.newDescription"
      :error-messages="state.descriptionErrors"
      rows="2"
      auto-grow
    ></v-textarea>
    <div class="d-flex justify-space-evenly">
      <v-btn @click="state.editing = false" prepend-icon="mdi-close">
        Cancel
      </v-btn>
      <v-btn @click="saveDescription" color="primary" prepend-icon="mdi-content-save">
        Save
      </v-btn>
    </div>
  </div>
  <div v-else class="mb-8">
    <div v-if="store.selectedMovie.description">
      <h3>Description</h3>
      <span class="font-italic description">{{store.selectedMovie.description}}</span>
      <v-btn @click="state.editing = true" prepend-icon="mdi-pencil" size="small" class="ml-2">
        Edit
      </v-btn>
    </div>
    <div v-else>
      <v-btn @click="state.editing = true" prepend-icon="mdi-plus" size="small">
        Add a description
      </v-btn>
    </div>
  </div>
</template>

<script setup>
import {useAppStore} from "@/store/app"
import {reactive} from "vue"

const store = useAppStore()
const state = reactive({
  editing: false,
  newDescription: store.selectedMovie.description,
  descriptionErrors: [],
  loading: false
})

const props = defineProps({
  movieId: String
})

const saveDescription = async () => {
  state.descriptionErrors = []
  state.loading = true
  const res = await fetch(`http://localhost:8080/movies/${props.movieId}/`, {
    method: "PATCH",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      description: state.newDescription
    })
  })
  state.loading = false
  // Handle errors
  if (res.status === 400) {
    const errors = await res.json()
    state.descriptionErrors = errors.description
  } else {
    const movie = await res.json()
    store.selectedMovie.description = movie.description
    store.displaySnackbar('Description has been updated')
    state.editing = false
  }
}
</script>

<style scoped>
.description {
  white-space: pre-wrap;
}
</style>
