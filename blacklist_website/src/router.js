import { createRouter, createWebHistory } from "vue-router";

import accueil from "./vue/accueil.vue";
import signup from "./vue/signup.vue";
import login from "./vue/login.vue";

const routes = [
    { path:'/', name: accueil, component: accueil},
    { path:'/signup', name: signup, component: signup},
    { path:'/login', name: login, component: login},
];

const router = createRouter({
    history : createWebHistory(), 
    routes,
});


export default router; 