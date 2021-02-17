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
    path: "/admin/create",
    name: "AdminCreate",
    component: () =>
      import("../views/AdminCreate.vue")
  },
  {
    path: "/admin/update",
    name: "AdminUpdate",
    component: () =>
      import("../views/AdminUpdate.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
