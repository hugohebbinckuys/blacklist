<script setup>
import { ref } from 'vue';
import axios from 'axios';
import router from '@/router';

const email = ref("")
const password = ref("")
const job = ref("")

const send_new_user = async() => {
    const user = {
        email:email.value,
        password:password.value,
        job:job.value,
    } // iportant envoyer au format json
    
    try {
        const response = await axios.post('http://127.0.0.1:5000/new_user', user)
        console.log("user sent to python")
        router.push("/login")
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

    <p> le v-model de email (test) : {{ email }} </p>

</template>
