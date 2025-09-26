import { createRouter, createWebHistory } from "vue-router";
import { useBlacklistStore } from "./blacklist_store";

import accueil from "./vue/accueil.vue";
import signup from "./vue/signup.vue";
import login from "./vue/login.vue";
import blacklist from "./vue/blacklist.vue";
import institution_auth from "./vue/institution_auth.vue";
import institution_signup from "./vue/institution_signup.vue";
import Insertion from "./vue/insertion.vue";

const routes = [
    { path:'/', name: accueil, component: accueil},
    { path:'/signup', name: signup, component: signup},
    { path:'/login', name: login, component: login},
    { path:'/blacklist', name: blacklist, component: blacklist}, 
    { path:'/institution_auth', name: institution_auth, component: institution_auth, meta:{requiredAuth:true}},
    { path:'/insertion', name: Insertion, component: Insertion, meta:{requiredAuth:true, requiredInstitution_Auth:true}},
    { path:'/institution_signup', name: institution_signup, component: institution_signup},
];

const router = createRouter({
    history : createWebHistory(), 
    routes,
});

router.beforeEach(async(to, from)=>{
    const blacklist_store = useBlacklistStore() // ici sinon le store est instancié avant qu'il existe 

    if (to.meta.requiredAuth && !blacklist_store.getter_is_authorized){
        console.log("you must be connected to access this page, redirect")
        return "/login"
    }
    if (to.meta.requiredInstitution_Auth && blacklist_store.getter_user_information[4]!==1){
        console.log("actual state of institution auth : ", blacklist_store.getter_user_information[4])
        console.log("you must have access to your institution, redirect")
        return "/institution_auth"
    }

    // return false // pour cancel la navigation
})

export default router; 