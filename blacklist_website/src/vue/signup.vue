<script setup>
import { ref } from 'vue';
import axios from 'axios';
import router from '@/router';

const liste_institutions = ref([])

const recup_institutions = async() => {
    const response = await axios.get('http://127.0.0.1:5000/recup_institutions')
    console.log(response.data)
    response.data["institutions"].forEach(element => {
        console.log("\n-- ", element, "--\n")
        liste_institutions.value.push(element)
    });
    console.log ("tableau final des institutions : ", liste_institutions.value)
    // liste_institutions.value.forEach(element => {
    // console.log("y a qq ? ", element)
    // });
}
recup_institutions()

const liste_noms_institutions = ref([])

const lister_noms = () => {
    console.log("on passe pas par la ? ")
    liste_institutions.value.forEach(element => {
        liste_noms_institutions.value.push(element[1])
        console.log("element ", element[1], "ajouté")
    });
}

lister_noms()
// ca marche pas sa mere 


const email = ref("")
const password = ref("")
const job = ref("")

const error = ref(0)

const send_new_user = async() => {
    const user = {
        email:email.value,
        password:password.value,
        job:job.value,
    } // iportant envoyer au format json
    
    try {
        const response = await axios.post('http://127.0.0.1:5000/new_user', user)
        console.log("user sent to python")
        if (response.data === "-- KO status --"){
            console.log(response.data)
            error.value = 1
        }
        else {
            router.push("/login")
        }
    } catch (error) {
        console.error("error when trying to send user information to python : ", error)
    }
}

</script>

<template>
    yo t la pour te signup toi

    <form action="" method="post">
        <input type="email" placeholder="email" v-model="email">
        <input type="password" placeholder="password" v-model="password">
        <input type="text" placeholder="job" v-model="job">
        <input type="submit" @click.prevent="send_new_user()">
    </form>
    <p style="color: red;" v-if="error === 1"> erreur lors de l'enregistrement de l'utilisateur </p>

    <p> le v-model de email (test) : {{ email }} </p>

    liste des etablissements : 
    <p v-for="institution in liste_noms_institutions"> {{ institution }} </p>

</template>
