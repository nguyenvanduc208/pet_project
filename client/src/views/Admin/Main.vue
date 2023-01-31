<template>
    <div class="container-xxl position-relative bg-white d-flex p-0">
        <AdminSidebar />


        <!-- Content Start -->
        <div class="content">

            <AdminHeader />

            <slot name="content-view"></slot>

            <AdminFooter />

        </div>
        <!-- Content End -->

        <!-- Back to Top -->
        <a href="#" class="btn btn-lg btn-primary btn-lg-square back-to-top"><i class="bi bi-arrow-up"></i></a>
    </div>
</template>

<script>
import AdminHeader from '@/components/Admin/Layouts/Header.vue'
import AdminFooter from '@/components/Admin/Layouts/Footer.vue'
import AdminSidebar from '@/components/Admin/Layouts/Sidebar.vue'
import router from '@/router'
export default {
    name: 'AdminMainView',
    components: {
        AdminFooter,
        AdminHeader,
        AdminSidebar
    },

    created() {
        if (this.$route.path.startsWith('/admin') && sessionStorage.getItem('token') == undefined) {
            router.push('/login')
        }
    },
}
</script>