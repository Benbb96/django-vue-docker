<template>
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
</template>

<script setup>
import {reactive} from "vue"
import {useAppStore} from "@/store/app"

const store = useAppStore()

const props = defineProps({
  movieId: String
})

const newReview = reactive({
  value: null,
  errors: [],
  loading: false
})

const submitReview = async () => {
  newReview.errors = []
  newReview.loading = true
  const res = await fetch("http://localhost:8080/reviews/", {
    method: "post",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      movie: props.movieId,
      grade: newReview.value
    })
  })
  newReview.loading = false
  // Handle errors
  if (res.status === 400) {
    const errors = await res.json()
    newReview.errors = errors.grade
  } else {
    store.displaySnackbar('Review is being added to this movie')
    newReview.value = null
  }
}
</script>

<style scoped>

</style>
