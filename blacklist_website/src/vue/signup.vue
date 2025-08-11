<script setup>
import { ref } from 'vue';
import axios from 'axios';

const email = ref("")
const password = ref("")
const job = ref("")

const send_new_user = async() => {
    user = (email.value, password.value, job.value)
    try {
        response = await axios.post('url_script_python', user)
        console.log("user sent to python")
    } catch (error) {
        console.error("error when trying to send user information to python : ", error)
    }
}

</script>

<template>
    yo t la pour te signup toi

    <form action="">
        <input type="text" placeholder="email" v-model="email">
        <input type="password" placeholder="password" v-model="password">
        <input type="text" placeholder="job" v-model="job">
        <input type="submit">
    </form>

    <p> le v-model de email (test) : {{ email }} </p>

</template>
