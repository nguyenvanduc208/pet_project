import { createRouter, createWebHistory } from "vue-router";
import Main from "@/views/Client/main.vue";
import HomePage from "@/views/Client/HomePage.vue";
import ShopList from "@/views/Client/Shop/ShopList.vue";
import DetailProduct from "@/views/Client/Shop/DetailProduct.vue";
import Cart from "@/views/Client/Cart.vue";
import Login from "@/views/Login.vue";
import AdminMainView from "@/views/Admin/Main.vue";
import Dashboard from "@/views/Admin/Dashboard.vue";
import CategoryList from "@/components/Admin/Category/List.vue";
import CategoryForm from "@/components/Admin/Category/Form.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Main,
      children: [
        {
          path: "/",
          component: HomePage,
        },
        {
          path: "/shop",
          component: ShopList,
        },
        {
          path: "/product/:id",
          component: DetailProduct,
        },
        {
          path: "/cart",
          component: Cart,
        },
      ],
    },

    {
      path: "/login",
      name: 'login',
      component: Login,
    },

    {
      path: "/admin",
      name: 'admin',
      component: AdminMainView,
      children: [
        {
          path: "",
          name: 'dashboard',
          component: Dashboard,
        },
        {
          path: "category",
          name: 'category',
          component: CategoryList,
        },
        {
          path: "category",
          name: 'category',
          component: CategoryForm,
        },
      ],
    },
  ],
});

export default router;
