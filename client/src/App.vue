<script>
import Header from './components/layouts/Header.vue'
import Footer from './components/layouts/Footer.vue'
import AdminMainView from './views/Admin/Main.vue'

export default {
  components: {
    Header,
    Footer,
    AdminMainView
  },

  computed: {
    isAdminRoute() {
      return this.$route.path.startsWith('/admin');
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
  <div v-else>
    <Header></Header>

      <RouterView />

    <Footer></Footer>
  </div>

</template>


