import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ShopView from '../views/ShopView.vue'
import SingleProduct from '../views/SingleProduct.vue'
import Cart from '../views/Cart.vue'
import AdminProduct from '@/views/Admin/Product.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/shop',
      name: 'shop',
      component: ShopView

    },
    {
      path: '/product/:id',
      name: 'detail-product',
      component: SingleProduct
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    },

    {
      path: '/admin',
      name: 'admin',
      component: AdminProduct
    }


  ]
})

export default router
