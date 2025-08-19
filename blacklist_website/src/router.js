import { createRouter, createWebHistory } from "vue-router";
import { useBlacklistStore } from "./blacklist_store";

import accueil from "./vue/accueil.vue";
import signup from "./vue/signup.vue";
import login from "./vue/login.vue";
import menu from "./vue/connected/connected_menu.vue";
import connected_menu from "./vue/connected/connected_menu.vue";
import institution_auth from "./vue/institution_auth.vue";

const routes = [
    { path:'/', name: accueil, component: accueil},
    { path:'/signup', name: signup, component: signup},
    { path:'/login', name: login, component: login},
    { path:'/menu', name: menu, component: menu, meta:{requiredAuth:true}},
    { path:'/institution_auth', name: institution_auth, component: institution_auth, meta:{requiredAuth:true}},
    { path:'/connected/menu', name: connected_menu, component: connected_menu, meta:{requiredAuth:true, requiredInstitution_Auth:true}},
];

const router = createRouter({
    history : createWebHistory(), 
    routes,
});

router.beforeEach(async(to, from)=>{
    const blacklist_store = useBlacklistStore() // ici sinon le store est instancié avant qu'il existe 

    if (to.meta.requiredAuth && !blacklist_store.getter_is_authorized){
        console.log("you must be connected to access this page, redirect")
        return from
    }
    if (to.meta.requiredInstitution_Auth && blacklist_store.getter_user_information[4]!==1){
        console.log("actual state of institution auth : ", blacklist_store.getter_user_information[4])
        console.log("you must have access to your institution, redirect")
        return "/institution_auth"
    }

    // return false // pour cancel la navigation
})

export default router; 