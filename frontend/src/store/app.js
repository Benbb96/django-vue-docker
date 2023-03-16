import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoading: true,
    actors: [],
    page: 1,
    movies: [],
    next: null,
    previous: null,
    count: 0,
    selectedMovie: null,
    snackbar: {
      display: false,
      text: '',
      color: null
    }
  }),
  getters: {
    averageGradeForSelectedMovie: (state) => {
      if (!state.selectedMovie || state.selectedMovie.review_set.length === 0) {
        return 0
      }
      const average = state.selectedMovie.review_set.reduce((a, b) => a + b) / state.selectedMovie.review_set.length
      return average.toFixed(2)
    }
  },
  actions: {
    async fetchActors() {
      this.isLoading = true
      const res = await fetch("http://localhost:8080/actors/")
        .then(response => response.json())
      this.isLoading = false
      this.actors = res
    },
    async fetchMovies() {
      this.isLoading = true
      const res = await fetch(`http://localhost:8080/movies/?page=${this.page}`)
        .then(response => response.json())
      this.isLoading = false
      this.count = res.count
      this.next = res.next
      this.previous = res.previous
      this.movies = res.results
    },
    async fetchMovie(id) {
      this.isLoading = true
      const res = await fetch(`http://localhost:8080/movies/${id}`)
        .then(response => response.json())
      this.isLoading = false
      this.selectedMovie = res
    },
    getActorDisplay(id) {
      const actor = this.actors.find(a => a.id === id)
      return actor.first_name + ' ' + actor.last_name
    },
    displaySnackbar(text, color='success') {
      this.snackbar.display = true
      this.snackbar.text = text
      this.snackbar.color = color
    }
  }
})
