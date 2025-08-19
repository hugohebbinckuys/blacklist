<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useBlacklistStore } from '@/blacklist_store'
import router from '@/router'

const email = ref("")
const password = ref("")
const blacklist_store = useBlacklistStore()

const test_email_format = (email) => {
    const regex = new RegExp("[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,8}$")
    if (regex.test(email)) {
        // console.log("email : ", email, " valide")
        return true
    }
    else {
        // console.log("email : ", email, " NON valide")
        return false
    }
}



const login = async() => {
    if (test_email_format(email.value)){
        console.log("ok - login en cours")
        const login_info = {email:email.value, password: password.value}
        const response = await axios.post("http://127.0.0.1:5000/login", login_info)
        console.log(response.data)
        if (response.data.authorized == true){
            console.log("- autorisé, stockage dans le store -")
            blacklist_store.action_authorized()
            router.push("/menu")
            // mettre ici le code pour sauavgerader dans store etat de connexion 
        }
        else {
            console.log("non_autorisé")
            // pas autorisé a se connecter 
        }
    }
    else console.log("NOT ok - saisir email")
}

</script>

<template>
    yo t la pour te login toi 
    <br><br>

    <form action="" method="post">
        <!-- <input type="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,8}$" placeholder="adresse@email.com" v-model="email" required> -->
        <input type="email" placeholder="adresse@email.com" v-model="email" required>
        <input type="password" placeholder="dsfuhdè79ù%é47hu9" v-model="password" required>
        <input type="submit" value="login" @click.prevent="login()">
    </form>
</template>