<template>
  <v-card>
    <v-card-title>Actors</v-card-title>
    <v-card-text v-if="state.editing">
      <v-autocomplete
        label="Select the actors"
        v-model="state.newActors"
        :items="store.actors"
        multiple
        clearable
        closable-chips
        :error-messages="state.actorsErrors"
      >
      </v-autocomplete>
    </v-card-text>
    <v-card-text v-else>
      <v-list v-if="store.selectedMovie.actors?.length">
        <v-list-item v-for="actorId in store.selectedMovie.actors" :key="actorId">
          {{store.actors.find(a => a.value === actorId).title}}
        </v-list-item>
      </v-list>
      <p v-else>
        No actor in this movie...
      </p>
    </v-card-text>

    <v-card-actions v-if="state.editing" class="d-flex justify-space-around">
      <v-btn @click="state.editing = false" variant="outlined" prepend-icon="mdi-close">
        Cancel
      </v-btn>
      <v-btn color="primary" @click="saveActors" variant="outlined" prepend-icon="mdi-content-save">
        Save
      </v-btn>
    </v-card-actions>
    <v-card-actions v-else class="d-flex justify-end">
      <v-btn @click="state.editing = true" variant="outlined" prepend-icon="mdi-pencil">
        Edit
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import {useAppStore} from "@/store/app"
import {reactive} from "vue"

const store = useAppStore()

const state = reactive({
  editing: false,
  newActors: [...store.selectedMovie.actors],
  actorsErrors: [],
  loading: false
})

const props = defineProps({
  movieId: String
})

const saveActors = async () => {
  state.actorsErrors = []
  state.loading = true
  const res = await fetch(`http://localhost:8080/movies/${props.movieId}/`, {
    method: "PATCH",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      actors: state.newActors
    })
  })
  state.loading = false
  // Handle errors
  if (res.status === 400) {
    const errors = await res.json()
    state.actorsErrors = errors.actors
  } else {
    const movie = await res.json()
    store.selectedMovie.actors = movie.actors
    store.displaySnackbar('Actors has been updated')
    state.editing = false
  }
}
</script>

<style scoped>

</style>
