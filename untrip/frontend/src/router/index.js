import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Landing",
    component: () =>
      import("../views/Landing.vue")
  },
  {
    path: "/trayectos",
    name: "Trayectos",
    component: () =>
      import("../views/Trayectos.vue")
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import("../views/About.vue")
  },
  {
    path: "/admin",
    name: "Admin",
    component: () =>
      import("../views/Admin.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
