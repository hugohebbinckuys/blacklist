<script setup>
import { ref, computed } from 'vue';
import { useBlacklistStore } from '@/blacklist_store';

const blacklist_store = useBlacklistStore()
const is_connected = computed(() => blacklist_store.getter_is_authorized) //computed pour que ce soit actualisé direct, sinon faudrait refresh pour que 'logout' apparaisse

</script>

<template>
    <a href="/" v-if="is_connected" @click="blacklist_store.action_logout">logout</a>
    <br>
    <router-link to="/"> retour accueil </router-link>
</template>