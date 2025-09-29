<script setup>
import { ref, computed, watch } from 'vue';
import { useBlacklistStore } from '@/blacklist_store';

const blacklist_store = useBlacklistStore()
console.log("\n ------- blacklist_store.getter_is_authorized : ", blacklist_store.getter_is_authorized)
const is_connected = computed(() => blacklist_store.getter_is_authorized) //computed pour que ce soit actualisé direct, sinon faudrait refresh pour que 'logout' apparaisse
// console.log(is_connected.value)
const user_email = ref("")

const logout_confirm = () => {
    if (confirm("Vous allez être déconnecté, êtes-vous sûr ?")){
        blacklist_store.action_logout()
    }
}

watch(is_connected, (new_value) => {
    if (new_value === true){
        console.log(blacklist_store.getter_user_information)
        user_email.value = blacklist_store.getter_user_information[0]
    }
}

)

</script>

<template>
    <a href="/" v-if="is_connected === true" @click="logout_confirm()">logout</a>
    <br>
    <router-link to="/"> accueil </router-link>
    <p v-if="is_connected === true"> connected under : {{ user_information }}</p>
    <p v-else> not connected </p>
</template>
