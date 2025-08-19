<script setup>
import { ref } from 'vue';
import axios from 'axios';
import router from '@/router';
import { useBlacklistStore } from '@/blacklist_store';

const blacklist_store = useBlacklistStore()
const liste_institutions = ref([])

const recup_institutions = async() => {
    const response = await axios.get('http://127.0.0.1:5000/recup_institutions')
    console.log(response.data)
    response.data["institutions"].forEach(element => {
        console.log("\n-- ", element, "--\n")
        liste_institutions.value.push(element)
    });
    console.log ("tableau final des institutions : ", liste_institutions.value)
    return true
    // liste_institutions.value.forEach(element => {
    // console.log("y a qq ? ", element)
    // });
}

recup_institutions()

const email = ref("")
const password = ref("")
const job = ref("")
const institution_selected = ref("")

const error = ref(0)

const send_new_user = async() => {
    const user = {
        email:email.value,
        password:password.value,
        job:job.value,
        institution:institution_selected.value
    } // iportant envoyer au format json
    
    try {
        console.log("Attempt to send these informations to python : ", user)
        const response = await axios.post('http://127.0.0.1:5000/new_user', user)
        console.log("user informations sent to python : ")
        if (response.data["status"] === "KO"){
            console.log(response.data)
            error.value = 1
        }
        else {
            if (response.data["status"] === "OK"){
                blacklist_store.action_fill_user_information(response.data["user_info"])
                blacklist_store.action_authorized()
                if (response.data["redirect"] === "connected"){
                    router.push("/connected")
                }
                else if (response.data["redirect"] === "institution_auth"){
                    router.push("/institution_auth")
                }
            }
        }
    } catch (error) {
        console.error("error when trying to send user information to python : ", error)
    }
}

</script>

<template>
    <p>yo t la pour te signup toi</p>

    <br>

    <form action="" method="post">
        <input type="email" placeholder="email" v-model="email">
        <input type="password" placeholder="password" v-model="password">
        <input type="text" placeholder="job" v-model="job">
        <select name="institutions_name" v-model="institution_selected" >
            <option v-for="institution in liste_institutions" :value="institution[0]"> {{ institution[1] }} </option>
        </select>

        <input type="submit" @click.prevent="send_new_user()">
    </form>
    <p style="color: red;" v-if="error === 1"> erreur lors de l'enregistrement de l'utilisateur </p>

</template>
