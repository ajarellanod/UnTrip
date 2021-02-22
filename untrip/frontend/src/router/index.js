import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Landing",
    component: () => import("../views/Landing.vue")
  },
  {
    path: "/trayectos",
    name: "Trayectos",
    component: () => import("../views/Trayectos.vue")
  },
  {
    path: "/reserva/:rutaId",
    name: "Reserva",
    component: () => import("../views/Reserva.vue"),
    props: true
  },
  {
    path: "/admin/create",
    name: "AdminCreate",
    component: () => import("../views/AdminCreate.vue")
  },
  {
    path: "/admin/update",
    name: "AdminUpdate",
    component: () => import("../views/AdminUpdate.vue")
  },
  {
    path: "/admin/delete",
    name: "AdminDelete",
    component: () => import("../views/AdminDelete.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
