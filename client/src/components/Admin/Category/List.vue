<template>
    <div>
        <div class="container-fluid pt-4">
            <div class="col-sm-12 col-xl-12">
                <div class="bg-light rounded h-100 p-4">
                    <h6 class="mb-4">Basic Table</h6>
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Name</th>
                                <th scope="col">Image</th>
                                <th scope="col">Status</th>
                                <th scope="col"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="category in categories" :key="category.id">
                                <th scope="row">1</th>
                                <td>{{ category.name }}</td>
                                <td><img :src="category.image_path" width="80" height="80" alt=""></td>
                                <td>{{ category.status == 1 ? 'Active' : 'Deactive' }}</td>
                            </tr>
                        </tbody>
                    </table>
                    <nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
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
            page: 3
        }
    },
    mounted() {
        apiService.getCategory(this.page).then(categories => {
            this.categories = categories
        })
    }
}

</script>