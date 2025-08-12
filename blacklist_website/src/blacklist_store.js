import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useBlacklistStore = defineStore('blacklist', () =>{
    //state
    const state = ref({
        authorized : sessionStorage.getItem("authorized_access") === "true"
    }) //ici je pense que on fait ca pour que ce soit reactif sinon on metterait const authorized ... mais pas reactif je pense 


    //getter 

    const getter_is_authorized = computed(() => state.value.authorized)


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

    return {
        state, 
        getter_is_authorized,
        action_authorized, 
        action_logout
    };
});