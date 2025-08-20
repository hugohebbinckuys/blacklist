<script setup>
import { useBlacklistStore } from '@/blacklist_store';
import router from '@/router';
import axios from 'axios';
import { ref } from 'vue';

const institution_password = ref("")
const blacklist_store = useBlacklistStore()

const send_request = async() => {
    try {
        const to_send = {password_entered:institution_password.value, institution_id:blacklist_store.getter_user_information[3]}
        const response = await axios.post("http://127.0.0.1:5000/institution_login", to_send)
        if (response.data["status"] === "OK"){
            console.log("mdp pour l'hotel validé")
            const user_info = response.data["user_info"]
            // blacklist_store.action_fill_user_information(user_info)
            console.log("la on doit changer le fait que authorisé a acc&éder à son etablissement c 1 maintenant ! parce que la on va pas povuoir accéder à connected/menu)")
            router.push("/connected/menu")
        }
    } catch (error) {
        console.error("erreur :", error)
    }
}

</script>

<template>
    <p> institution_auth </p>

    <form action="" method="POST">
        <input type="text" value="Hotel de Wimereux" disabled>
        <input type="text" value="Wimereux" disabled>
        <input type="password" v-model="institution_password" placeholder="hdfsuyh78/@kdsijd^">
        <input type="submit" @click.prevent="send_request()">
    </form>

</template>