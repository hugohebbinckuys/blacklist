<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useBlacklistStore } from '@/blacklist_store';
import router from '@/router';

const blacklist_store = useBlacklistStore()
const institution_id = blacklist_store.getter_user_information[3]

const nom = ref("")
const prenom = ref("")
const numero = ref("")
const email = ref("")
const description = ref("")

const send_new_blacklisted = async() => {
    const new_blacklisted = {
        nom:nom.value, 
        prenom:prenom.value, 
        numero: numero.value, 
        email:email.value, 
        description:description.value,
        institution_id:institution_id
    }
    console.log("-- envoi des informations suivantes pour ajout d'un nouveau bblacklisté : --")
    console.log(new_blacklisted)
    const response = await axios.post("http://127.0.0.1:5000/new_blacklisted", new_blacklisted)
    // console.log(response)
    alert("Blacklisted added successfuly ! ")
    router.push("/blacklist")
}

</script>

<template>
    <br><br>
    // insertion nouveau blacklisté //
    <br><br>

    <form action="" method="post" @submit.prevent="send_new_blacklisted()">
        <input type="text" placeholder="nom" v-model="nom"><br>
        <input type="text" placeholder="prenom" v-model="prenom"><br>
        <input type="text" placeholder="06 .. .. .. .." v-model="numero"><br>
        <input type="text" placeholder="email@email.com" v-model="email"><br>
        <textarea placeholder="description des faits..." v-model="description"></textarea><br>
        <!-- <input type="submit" value="ajouter blacklisté" @click.prevent="send_new_blacklisted()">  -->
        <input type="submit" value="ajouter blacklisté"> 
    </form>
</template>