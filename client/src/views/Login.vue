<template>
    <div class="container-fluid">
        <div class="row h-100 align-items-center justify-content-center" style="min-height: 100vh;">
            <div class="col-12 col-sm-8 col-md-6 col-lg-5 col-xl-4">
                <div class="bg-light rounded p-4 p-sm-5 my-4 mx-3">
                    <div class="d-flex align-items-center justify-content-between mb-3">
                        <router-link to="/">
                            <h3 class="text-primary"><i class="fa fa-hashtag me-2"></i>MATLUX SHOP</h3>
                        </router-link>
                        <h3>Sign In</h3>
                    </div>
                    <form @submit.prevent="handleSubmit">
                    <div v-if="message" class="alert alert-danger" role="alert">
                        {{ message }}
                    </div>
                        <div class="form-floating mb-3">
                            <input v-model="username" type="text" class="form-control" id="floatingInput"
                                placeholder="name@example.com">
                            <label for="floatingInput">Username</label>
                        </div>
                        <div class="form-floating mb-4">
                            <input v-model="password" type="password" class="form-control" id="floatingPassword"
                                placeholder="Password">
                            <label for="floatingPassword">Password</label>
                        </div>
                        <button @click="handleSubmit" type="submit" class="btn btn-primary py-3 w-100 mb-4">Sign In</button>
                    </form>
                    <p class="text-center mb-0">Don't have an Account? <a href="">Sign Up</a></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import apiSevice from '../apiService.js'
import router from '@/router'

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
            message: ''
        }
    },
    methods: {
        async handleSubmit() {
            const data = {
                'username': this.username,
                'password': this.password
            }

            const res = await apiSevice.login(data)

            if (!res) {
                this.message = 'Incorrect username or password'
            } else {
                router.push('/admin')
            }


        }
    },

    beforeRouteEnter(to, from, next) {
        const token = sessionStorage.getItem('token');
        if (!token) {
            next();
        } else {
            next({ name: 'admin' });
        }
    },
}
</script>