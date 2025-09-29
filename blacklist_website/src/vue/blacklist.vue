<script setup>
import { ref } from 'vue';
import axios from 'axios';
import insertion from './insertion.vue';

const blacklist_all = ref([]) // this one 'll contain all the information about the blacklisted 
const blacklist = ref([]) // this one 'll only contain the information to display on the table 

const retrieve_blacklisted = async() => {
    const response = await axios.get("http://127.0.0.1:5000/retrieve_blacklisted")
    try {
        // console.log("blacklisted from query : ", response.data)
        blacklist_all.value = response.data.blacklisted
    } catch (error) {
        console.error("Error when trying to retrieve blacklisted :", error)
    }
    for (let i = 0; i < blacklist_all.value.length ; i++){
        // console.log("iteratyion : ", blacklist_all.value[i])
        blacklist.value[i] = [blacklist_all.value[i][1], blacklist_all.value[i][2], blacklist_all.value[i][3], blacklist_all.value[i][4], blacklist_all.value[i][5]]
    }
    // console.log("\n\nblacklist_all : ", blacklist_all.value)
    // console.log("\n\nblacklist : ", blacklist.value)
}

retrieve_blacklisted()

const redirect_insertion = () => {
    
}
</script>

<template>
    // Menu template //
    <br><br>
    next, soon -> add someone to the blacklist 
    <br><br>

    <router-link to="insertion"> Ajouter un nouveau blacklisté </router-link> 

    <table>
        <caption> Black-listed people </caption>
        <thead>
            <tr>
                <th>Nom</th>
                <th>Prenom</th>
                <th>numero</th>
                <th>email</th>
                <th>description</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="person in blacklist">
                <td v-for="elt in person">
                    <p> {{ elt }} </p>
                </td>
            </tr>
        </tbody>
    </table>

    <button @click="retrieve_blacklisted()" class="btn"> raffraichir </button> 

</template>

<style>
table{
    width: 100%;
    text-align: center;
}
</style>