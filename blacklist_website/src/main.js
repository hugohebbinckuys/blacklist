import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'

const app = createApp(App) // createApp est une fonction fournie par vue pour permettrte de créer une instance de App.vue. Sert a l'utiliser et la monter dans un DOM. 
app.use(createPinia())
app.use(router)


app.mount('#app') // et ca ca sert a monter l'application sur l'elt html ayant l'id app (dans index.html). Monter dans les frameworks ca signifie afficher l'app dans le navigateur en liant le code vue avec une balise html dans le index.html