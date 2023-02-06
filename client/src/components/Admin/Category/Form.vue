<template>
    <div class="col-sm-12 col-xl-12 mt-4 bg-light">
        <div class="bg-light rounded h-100 p-4">
            <h6 class="mb-4">Add new category</h6>
            <form @submit.prevent="handleSubmit">
                <div class="mb-3">
                    <label for="name" class="form-label">Name</label>
                    <input ref="name" @blur="validateName" v-model="name" type="text" class="form-control" id="name">
                    <div v-if="validate.name.status" id="emailHelp" class="form-text text-danger">{{ validate.name.message }}
                    </div>
                </div>
                <div class="mb-3">
                    <label for="formFile" class="form-label">Image</label>
                    <input ref="fileInput" @change="getFile" class="form-control" type="file" id="formFile">
                    <div v-if="validate.image.status" id="emailHelp" class="form-text text-danger">{{ validate.image.message }}
                    </div>
                </div>
                <div class="mb-3 form-check">
                    <label for="exampleInputPassword1" class="form-label">Status</label>
                    <div class="form-check">
                        <input class="form-check-input" v-model="status" type="radio" name="gridRadios" value="1" checked>
                        <label class="form-check-label" for="gridRadios1">
                            Active
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" v-model="status" type="radio" name="gridRadios" value="0">
                        <label class="form-check-label" for="gridRadios2">
                            Deactive
                        </label>
                    </div>
                </div>
                <button type="submit" class="btn btn-primary">Add new</button>
                <i v-if="loading" class="fas fa-spinner fa-spin"></i>
            </form>
        </div>
    </div>
</template>

<script>
import { fb, convertToSlug } from "@/common.js"
import apiService from '@/apiService.js'


export default {
    name: 'FormCategory',
    data() {
        return {
            name: '',
            image: [],
            status: '1',
            validate: {
                name: {
                    status: false,
                    message: ''
                },
                image: {
                    status: false,
                    message: ''
                }
            },
            loading: false
        }
    },
    methods: {
        getFile() {
            const input = this.$refs.fileInput
            this.image = input.files
            this.validateImage()
        },

        async uploadFile(file) {
            const firebase = fb
            const storageRef = firebase.storage().ref()
            const fileRef = storageRef.child(`images/${file.name}`)
            await fileRef.put(file)
            const url = await fileRef.getDownloadURL()
            return url
        },
        validateName() {
            if(this.name === ''){
                this.validate.name.status = true
                this.validate.name.message = 'Please enter category name'
            }else{
                this.validate.name.status = false
            }
        },
        validateImage(){
            if (this.image.length === 0){
                this.validate.image.status = true
                this.validate.image.message = 'Please choose a photo'
            }else{
                this.validate.image.status = false
            }
        },
        clearData() {
            this.$refs.fileInput.value = ''
            this.name = ''
        },

        async handleSubmit() {
            console.log(this.status);
            this.loading = true
            this.validateImage()
            this.validateName()
            if (!this.validate.name.status && !this.validate.image.status){
                const file = this.image[0]
                const url = await this.uploadFile(file)
                const slug = convertToSlug(this.name)
                const imageData = await apiService.addImage({
                    path: url,
                    title: slug
                })

                const categoryData = {
                    name: this.name,
                    status: this.status,
                    image: imageData.id
                }
                
                const categoryRes = await apiService.addCategory(categoryData)
                
                if (categoryRes) { 
                    this.clearData()
                    alert("Add data successfully")
                }

                this.loading = false
                
            }
            

        }
    }
}
</script>