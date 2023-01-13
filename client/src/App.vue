<script>
  import Header from './components/layouts/Header.vue'
  import Footer from './components/layouts/Footer.vue'

  export default {
    components: {
      Header,
      Footer
    }
  }
</script>

<template>
  <Header></Header>

  <RouterView />

  <Footer></Footer>
</template>


