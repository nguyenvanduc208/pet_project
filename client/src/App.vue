<script>
import Header from './components/layouts/Header.vue'
import Footer from './components/layouts/Footer.vue'
import AdminMainView from './views/Admin/Main.vue'
import LoginPage from '@/views/Login.vue'

const test = JSON.parse(sessionStorage.getItem('token'))
console.log(test)

export default {
  components: {
    Header,
    Footer,
    AdminMainView,
    LoginPage
  },

  computed: {
    isAdminRoute() {
      return this.$route.path.startsWith('/admin');
    },

    isLoginRoute(){
      return this.$route.path.startsWith('/login');
    }
  }
}
</script>

<template>
  <!-- client page -->
  <div v-if="isAdminRoute">
    <AdminMainView>
       <template v-slot:content-view >
        <RouterView />
       </template>
    </AdminMainView>
  </div>

  <div v-else-if="isLoginRoute">
    <LoginPage />
  </div>

  <div v-else>
    <Header></Header>

      <RouterView />

    <Footer></Footer>
  </div>

</template>


