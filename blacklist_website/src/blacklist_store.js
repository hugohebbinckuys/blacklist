import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useBlacklistStore = defineStore('blacklist', () =>{
    //state
    const state = ref({
        authorized : sessionStorage.getItem("authorized_access") === "true",
        user_information : JSON.parse(sessionStorage.getItem("user_information"))
    }) //ici je pense que on fait ca pour que ce soit reactif sinon on metterait const authorized ... mais pas reactif je pense 


    //getter 

    const getter_is_authorized = computed(() => state.value.authorized)
    const getter_user_information = computed(()=> state.value.user_information)


    //action
    const action_authorized = () => {
        state.value.authorized = true // on met à trou comme ça le navigateur sait directement que c true (si que l'etape d'après on serait obligé de recharger la page donc perd la reactivité)
        sessionStorage.setItem("authorized_access", true) // ici on le stocke bien dans le sessionStorage (et le true est pas booléen mais str)
        console.log("- store action - authorized now")
    }
    
    const action_logout = () => {
        state.value.authorized = false
        sessionStorage.setItem("authorized_access", false)
        console.log("- store action - unauthorized now")
    }

    const action_fill_user_information = (user_info) => {
        state.value.user_information = user_info
        sessionStorage.setItem("user_information", JSON.stringify(user_info))
        console.log("- user :", user_info, "connecté")
    }

    const action_test_email_format = (email) => {
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

    return {
        state, 
        getter_is_authorized,
        getter_user_information, 
        action_authorized, 
        action_logout, 
        action_fill_user_information, 
        action_test_email_format
    };
});