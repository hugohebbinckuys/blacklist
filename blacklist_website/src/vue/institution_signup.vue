<script setup>

import { ref } from 'vue'
// import mimemessage from 'mimemessage'
// import nodemailer from 'nodemailer'
import dotenv from 'dotenv'
import axios from 'axios'
import router from '@/router'

const institution_name = ref("")
const institution_location = ref("")
const institution_postalCode = ref("")
const institution_mailAdress = ref("")
const institution_director = ref("")
const institution_phone = ref("")
const person_talking = ref("")
const person_talking_role = ref("")
const comment = ref("")

const email_sent = ref(0)

const timeout_and_message = (message) => {
    if (message === "OK"){
        email_sent.value = 1
        setTimeout(function(){
            console.log("waiting 15 seconds")
            router.push("/")
        }, 15000)
    }
    else if (message === "KO"){
        email_sent.value = -1
    }
}

const send_email = () => {
    try {
        email_sent.value = 0 
        axios.post('http://localhost:3000/email_sender', {
            institution_name: institution_name.value,
            institution_location: institution_location.value,
            institution_postalCode: institution_postalCode.value,
            institution_mailAdress: institution_mailAdress.value,
            institution_director: institution_director.value,
            institution_phone: institution_phone.value,
            person_talking: person_talking.value,
            person_talking_role: person_talking_role.value,
            comment: comment.value,
        }).then(function(retour){
            // console.log(retour)
            if (retour.data["success"] === true){
                timeout_and_message("OK")
            }
        })
    } catch (error) {
        console.error("error : ", error)
    }
    timeout_and_message("KO")    
}

</script>

<template>
    <p>Hi you want to join us and register your institution ? Here it is </p>
    

    <form action="" method="POST" @submit.prevent="send_email()">
        <input type="text" placeholder="Hotel de Wimereux" v-model="institution_name" required> <br>
        <input type="text" placeholder="Wimereux" v-model="institution_location" required><br>
        <input type="text" placeholder="62930" v-model="institution_postalCode" required><br>
        <input type="text" placeholder="contact.hdw@gmail.com" v-model="institution_mailAdress" required><br>
        <input type="text" placeholder="Jean Marc Boulanger" v-model="institution_director" required><br>
        <input type="text" placeholder="0315423968" v-model="institution_phone" required><br>
        <input type="text" placeholder="Nicolas Hebbinckuys" v-model="person_talking" required><br>
        <input type="text" placeholder="Réceptionniste" v-model="person_talking_role" required><br>
        <textarea placeholder="any comment..." v-model="comment"> </textarea><br><br>
        <input type="submit" value="Envoyer à l'équipe de blacklist">
    </form><br>

    <p v-if="email_sent === 1">Your register 'll be investigated. You 'll have an answer under 48h. You can come back to the menu or 'll be automatically redirected in few seconds'</p>
    <p v-if="email_sent === -1" style="color: red;">An error occurs during sending the information. Please try again later or contact us to solve the problem. </p>
</template>