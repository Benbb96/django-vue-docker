<template>
  <router-view />
</template>

<script setup>
import {onMounted} from "vue"
import {useAppStore} from "@/store/app"

const store = useAppStore()
onMounted(() => store.fetchActors())
</script>
