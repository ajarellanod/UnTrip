import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'


createApp(App)
  .use(store)
  .use(router)
  .use(Buefy)
  .mount("#app");
