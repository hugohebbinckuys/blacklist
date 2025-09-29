<script setup>
import { useBlacklistStore } from '@/blacklist_store';
import router from '@/router';
import axios from 'axios';
import { ref } from 'vue';

const institution_password = ref("")
const blacklist_store = useBlacklistStore()
const bad_password = ref(0)

const send_request = async() => {
    try {
        bad_password.value = 0 
        const to_send = {password_entered:institution_password.value, institution_id:blacklist_store.getter_user_information[3], user_email:blacklist_store.getter_user_information[0]}
        const response = await axios.post("http://127.0.0.1:5000/institution_login", to_send)
        if (response.data["status"] === "OK"){
            console.log("mdp pour l'hotel validé")
            
            const user_info = response.data["user_updated"]
            console.log("user updated : ", user_info)
            blacklist_store.action_fill_user_information(user_info)
        
            router.push("/blacklist")
        }
        else {
            bad_password.value = 1
        }
    } catch (error) {
        console.error("erreur institution login  :", error)
    }
}

</script>

<template>
    <p> institution_auth </p>

    <h3 style="color:red"> Vous n'êtes pas encore authentifiés auprès de votre établissement. <br>Authentifiez-vous avec le mot de passe de celui-ci pour pouvoir ajouter des blacklistés. </h3>

    <form action="" method="POST">
        /!\ changer hotel de wimereux ici et bien mettre le bon hotel linked to the connected person
        <input type="text" value="Hotel de Wimereux" disabled>
        <input type="text" value="Wimereux" disabled>
        <input type="password" v-model="institution_password" placeholder="hdfsuyh78/@kdsijd^">
        <input type="submit" @click.prevent="send_request()">
    </form>

    <p v-if="bad_password == 1" style="color: red;"> Le mot de passe saisi n'est pas bon</p>
</template>