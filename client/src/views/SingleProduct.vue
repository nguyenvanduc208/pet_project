<template>
    <div class="breadcrumb-area pt-45 pb-45">
        <div class="container">
            <div class="row">
                <div class="col-xl-12">
                    <div class="breadcrumb-text text-center">
                        <h1>Single Shop</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- breadcrumb-area-end -->
    <!-- shop-area-start -->
    <div class="shop-area pt-100 pb-90">
        <div class="container">
            <div class="row mb-50">
                <div class="col-xl-6 col-lg-5">
                    <div class="product-zoom-img mb-50">
                        <ul class="nav product-tab" id="myTab" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab"
                                    aria-controls="home" aria-selected="true"><img
                                        src="http://localhost:5173/asset/img/shop/shop-details/2.jpg" alt=""></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab"
                                    aria-controls="profile" aria-selected="false"><img
                                        src="http://localhost:5173/asset/img/shop/shop-details/3.jpg" alt=""></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab"
                                    aria-controls="contact" aria-selected="false"><img
                                        src="http://localhost:5173/asset/img/shop/shop-details/4.jpg" alt=""></a>
                            </li>
                        </ul>
                        <div class="tab-content" id="myTabContent">
                            <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                                <img :src="getPhoto()" alt="aaaa"></div>
                            <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab"><img
                                    src="http://localhost:5173/asset/img/shop/shop-details/1.jpg" alt=""></div>
                            <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab"><img
                                    src="http://localhost:5173/asset/img/shop/shop-details/1.jpg" alt=""></div>
                        </div>
                    </div>
                </div>
                <div class="col-xl-6 col-lg-7">
                    <div class="product-desc mb-50">
                        <h2>Apple cider sauce and pork</h2>
                        <div class="rating">
                            <a href="#"><i class="fas fa-star"></i></a>
                            <a href="#"><i class="fas fa-star"></i></a>
                            <a href="#"><i class="fas fa-star"></i></a>
                            <a href="#"><i class="fas fa-star"></i></a>
                            <a href="#"><i class="far fa-star"></i></a>
                            <span>(2)</span>
                        </div>
                        <span>$99.90</span>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
                            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
                            laboris nisi ut aliquip ex ea co- mmodo consequat.</p>
                        <div class="pro-details-action">
                            <a href="#" class="brand-btn"> <i class="fas fa-shopping-cart">
                                </i>ADD TO CART</a>
                            <select name="select" id="number">
                                <option value="">01</option>
                                <option value="">02</option>
                                <option value="">03</option>
                                <option value="">04</option>
                                <option value="">04</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-xl-12">
                    <div class="product-review">
                        <ul class="nav review-tab" id="myTab1" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" id="home-tab1" data-toggle="tab" href="#home1" role="tab"
                                    aria-controls="home" aria-selected="true">Description </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="profile-tab1" data-toggle="tab" href="#profile1" role="tab"
                                    aria-controls="profile" aria-selected="false">Reviews (2)</a>
                            </li>
                        </ul>
                        <div class="tab-content" id="myTabContent2">
                            <div class="tab-pane fade show active" id="home1" role="tabpanel"
                                aria-labelledby="home-tab1">
                                <div class="review-text mt-30">
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
                                        incididunt ut labore et dolore magna
                                        aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
                                        ut aliquip ex ea commodo consequat.</p>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
                                        incididunt ut labore et dolore magna
                                        aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
                                        ut aliquip ex ea commodo consequat.</p>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="profile1" role="tabpanel" aria-labelledby="profile-tab1">
                                <div class="review-text mt-30">
                                    <div class="product-commnets">
                                        <div class="product-commnets-list">
                                            <div class="pro-comments-img">
                                                <img src="http://localhost:5173/asset/img/shop/shop-details/1.png" alt="">
                                            </div>
                                            <div class="pro-commnets-text">
                                                <h4>Roger West -
                                                    <span>June 5, 2017</span>
                                                </h4>
                                                <div class="rating">
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="far fa-star"></i>
                                                    </a>
                                                </div>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                                                    eiusmod tempor incididunt ut labore et dolore magna aliqua.
                                                    Ut enim ad minim veniam, quis nostrud exercitation.</p>
                                            </div>
                                        </div>
                                        <div class="product-commnets-list mt-30">
                                            <div class="pro-comments-img">
                                                <img src="http://localhost:5173/asset/img/shop/shop-details/2.png" alt="">
                                            </div>
                                            <div class="pro-commnets-text">
                                                <h4>Roger West -
                                                    <span>June 5, 2017</span>
                                                </h4>
                                                <div class="rating">
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="fas fa-star"></i>
                                                    </a>
                                                    <a href="#">
                                                        <i class="far fa-star"></i>
                                                    </a>
                                                </div>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
                                                    eiusmod.</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row mt-60">
                <div class="col-xl-7">
                    <div class="review-box">
                        <h4>Add a Review</h4>
                        <div class="your-rating mb-40">
                            <span>Your Rating:</span>
                            <div class="rating-list">
                                <a href="#">
                                    <i class="far fa-star"></i>
                                </a>
                                <a href="#">
                                    <i class="far fa-star"></i>
                                </a>
                                <a href="#">
                                    <i class="far fa-star"></i>
                                </a>
                                <a href="#">
                                    <i class="far fa-star"></i>
                                </a>
                                <a href="#">
                                    <i class="far fa-star"></i>
                                </a>
                            </div>
                        </div>
                        <form class="review-form" action="#">
                            <div class="row">
                                <div class="col-xl-12">
                                    <label for="message">YOUR REVIEW</label>
                                    <textarea name="message" id="message" cols="30" rows="10"></textarea>
                                </div>
                                <div class="col-xl-6">
                                    <label for="r-name">Name</label>
                                    <input type="text" id="r-name">
                                </div>
                                <div class="col-xl-6">
                                    <label for="r-email">Email</label>
                                    <input type="email" id="r-email">
                                </div>
                                <div class="col-xl-12">
                                    <button class="brand-btn">Add your Review</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- shop-area-end -->
    <!-- product-area-start -->
    <div class="product-area pb-90">
        <div class="container">
            <div class="row">
                <div class="col-xl-12">
                    <div class="product-title">
                        <h1>Related products</h1>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="product-active owl-carousel">
                    <div class="col-xl-12">
                        <div class="shop-wrapper">
                            <div class="shop-img">
                                <a href="#"><img src="http://localhost:5173/asset/img/shop/shop1.jpg" alt="" /></a>
                            </div>
                            <div class="shop-text">
                                <h3><a href="#">Apple cider sauce and pork</a></h3>
                                <span>$99.90</span>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-12">
                        <div class="shop-wrapper">
                            <div class="shop-img">
                                <a href="#"><img src="http://localhost:5173/asset/img/shop/shop2.jpg" alt="" /></a>
                            </div>
                            <div class="shop-text">
                                <h3><a href="#">Chicken Ball </a></h3>
                                <span>$99.90</span>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-12">
                        <div class="shop-wrapper">
                            <div class="shop-img">
                                <a href="#"><img src="http://localhost:5173/asset/img/shop/shop3.jpg" alt="" /></a>
                            </div>
                            <div class="shop-text">
                                <h3><a href="#">Vegetable Pakura</a></h3>
                                <span>$99.90</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: 'SingleProduct',
    methods: {
        getPhoto() {
            return 'http://localhost:5173/asset/img/shop/shop-details/1.jpg';
      }
    }
}


</script>