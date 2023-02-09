<template>
    <div>
        <div class="container-fluid pt-4">
            <div class="col-sm-12 col-xl-12">
                <div class="bg-light rounded h-100 p-4">
                    <div class="d-flex justify-content-between mb-4">
                        <h6 class="d-flex align-items-center">Category List</h6>
                        <router-link :to="{ name: 'category-add' }" class="btn btn-primary">add new</router-link>
                    </div>
                    <table class="table" >
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Name</th>
                                <th scope="col">Image</th>
                                <th scope="col">Status</th>
                                <th scope="col" width="250">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(category, index) in categories" :key="category.id" >
                                <th scope="row">{{ index + 1}}</th>
                                <td>{{ category.name }}</td>
                                <td><img :src="category.image_path" width="80" height="80" alt=""></td>
                                <td>{{ category.status == 1 ? 'Active' : 'Deactivate' }}</td>
                                <td class="d-flex justify-content-between">
                                    <router-link :to="{ name: 'category-update', params: { id: category.id } }"
                                        class="btn btn-success">Update</router-link>
                                    <button type="button" class="btn btn-danger" @click="handleRemove(category.id)">Remove</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <nav aria-label="Page navigation example">
                        <ul class="pagination">
                            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                            <li @click="handleSwitchPage(numberPage)" v-for="numberPage in totalPage" :key="numberPage"
                                class="page-item" :class="{ active: page == numberPage }">
                                <a class="page-link" href="#">{{ numberPage }}</a>
                            </li>
                            <li class="page-item"><a class="page-link" href="#">Next</a></li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import apiService from '@/apiService.js'
export default {
    name: 'ListCategory',
    data() {
        return {
            categories: [],
            page: 1,
            totalPage: 0
        }
    },

    mounted() {
        this.getCategories()
    },

    watch: {
        page: function (newPage, oldPage) {
            this.getCategories()
        }
    },

    methods: {
        handleSwitchPage(numberPage) {
            this.page = numberPage
        },

        getCategories() {
            apiService.getCategories(this.page).then(response => {
                this.categories = response.result
                this.totalPage = response.info.total_page
            })
        },

        async handleRemove(id) {
            if (confirm('Are you sure you want to delete ?')) {
                const res = await apiService.deleteCategory(id)

                if (res) {
                    alert('Delete the directory successfully')
                    this.getCategories()
                }
                else {
                    alert('Unsuccessful directory deletion')
                }
            }
        }
    }
}

</script>