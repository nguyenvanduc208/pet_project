<template>
    <div class="container-xxl position-relative bg-white d-flex p-0 ">
        <AdminSidebar />


        <!-- Content Start -->
        <div class="content">
                <AdminHeader />
                <div class="px-4">
                    <RouterView />
                </div>
                

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
import Cookies from 'js-cookie'

export default {
    name: 'AdminMainView',
    components: {
        AdminFooter,
        AdminHeader,
        AdminSidebar
    },
    beforeRouteEnter(to, from, next) {
        const token = Cookies.get('token')
        if (token) {
            next();
        } else {
            next({ name: 'login' });
        }
    },
}
</script>