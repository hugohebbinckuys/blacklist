<script setup>
import navbar from './component/navbar.vue';
</script>

<template>
  <navbar/>
  <div class="container card">
    <router-view/>
  </div>
</template>