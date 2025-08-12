import { createRouter, createWebHistory } from "vue-router";
import { useBlacklistStore } from "./blacklist_store";

import accueil from "./vue/accueil.vue";
import signup from "./vue/signup.vue";
import login from "./vue/login.vue";
import menu from "./vue/connected/menu.vue";

const routes = [
    { path:'/', name: accueil, component: accueil},
    { path:'/signup', name: signup, component: signup},
    { path:'/login', name: login, component: login},
    { path:'/menu', name: menu, component: menu, meta:{requiredAuth:true}},
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

    // return false // pour cancel la navigation
})

export default router; 