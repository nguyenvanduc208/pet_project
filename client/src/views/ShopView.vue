<template>
    <div class="breadcrumb-area pt-45 pb-45">
        <div class="container">
            <div class="row">
                <div class="col-xl-12">
                    <div class="breadcrumb-text text-center">
                        <h1>shop</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- breadcrumb-area-end -->
    <!-- shop-area-start -->
    <div class="shop-area pt-100 pb-100">
        <div class="container">
            <div class="row">
                <div class="col-xl-12">
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 mb-65">
                            <ul class="nav shop-tab" id="myTab" role="tablist">
                                <li class="nav-item">
                                    <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home"><i
                                            class="fas fa-th"></i></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile"><i
                                            class="fas fa-th-list"></i></a>
                                </li>
                            </ul>
                            <div class="showing-text d-none d-md-block">
                                <span>Showing 1–20 of 75 results </span>
                            </div>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 mb-65 d-none d-md-block">
                            <div class="selector-field  justify-content-end">
                                <form action="#">
                                    <select name="select">
                                        <option value="">Sort by : Default sorting</option>
                                        <option value="">Price: Lowest first</option>
                                        <option value="">Price: Highest first</option>
                                        <option value="">Product Name: A to Z</option>
                                        <option value="">Product Name: Z to A</option>
                                        <option value="">In stock</option>
                                        <option value="">Reference: Lowest first</option>
                                        <option value="">Reference: Highest first</option>
                                    </select>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="tab-content" id="myTabContent">
                        <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                            <div class="row">
                                <div class="col-xl-4 col-lg-4 col-md-6 mb-60">
                                    <div class="shop-wrapper">
                                        <div class="shop-img">
                                            <router-link to="/product/1"><img src="asset/img/shop/shop1.jpg" alt="" /></router-link>
                                        </div>
                                        <div class="shop-text">
                                            <h3><a href="#">Apple cider sauce and pork</a></h3>
                                            <span>$99.90</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-6 mb-60">
                                    <div class="shop-wrapper">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop2.jpg" alt="" /></a>
                                        </div>
                                        <div class="shop-text">
                                            <h3><a href="#">Chicken Ball </a></h3>
                                            <span>$99.90</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-6 mb-60">
                                    <div class="shop-wrapper">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop3.jpg" alt="" /></a>
                                        </div>
                                        <div class="shop-text">
                                            <h3><a href="#">Vegetable Pakura</a></h3>
                                            <span>$99.90</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-6 mb-60">
                                    <div class="shop-wrapper">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop4.jpg" alt="" /></a>
                                        </div>
                                        <div class="shop-text">
                                            <h3><a href="#">Special Wonthan</a></h3>
                                            <span>$99.90</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-6 mb-60">
                                    <div class="shop-wrapper">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop5.jpg" alt="" /></a>
                                        </div>
                                        <div class="shop-text">
                                            <h3><a href="#">Apple cider sauce and pork</a></h3>
                                            <span>$99.90</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-6 mb-60">
                                    <div class="shop-wrapper">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop6.jpg" alt="" /></a>
                                        </div>
                                        <div class="shop-text">
                                            <h3><a href="#">Cheese cake</a></h3>
                                            <span>$99.90</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                            <div class="row mb-20">
                                <div class="col-xl-4 col-lg-4 col-md-6">
                                    <div class="shop-wrapper mb-40">
                                        <div class="shop-img">
                                            <a href="#">
                                                <img src="asset/img/shop/shop2.jpg" alt="" />
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-8">
                                    <div class="shop-desc">
                                        <h2>
                                            <a href="#">Apple cider sauce and pork</a>
                                        </h2>
                                        <span>$99.90</span>
                                        <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis
                                            praesentium voluptatum deleniti atque corrupti
                                            quos dolores et quas molestias excepturi sint occaecati cupiditate non
                                            provident, similique sunt in culpa qui officia
                                            deserunt mollitia animi, id est laborum et dolorum fuga.</p>
                                        <div class="shop-details">
                                            <a class="btn" href="#">View More</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-20">
                                <div class="col-xl-4 col-lg-4 col-md-6">
                                    <div class="shop-wrapper mb-40">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop1.jpg" alt="" /></a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-8">
                                    <div class="shop-desc">
                                        <h2><a href="#">Chicken Ball</a></h2>
                                        <span>$99.90</span>
                                        <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis
                                            praesentium voluptatum deleniti atque corrupti
                                            quos dolores et quas molestias excepturi sint occaecati cupiditate non
                                            provident, similique sunt in culpa qui officia deserunt
                                            mollitia animi, id est laborum et dolorum fuga.</p>
                                        <div class="shop-details">
                                            <a class="btn" href="#">View More</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-20">
                                <div class="col-xl-4 col-lg-4 col-md-6">
                                    <div class="shop-wrapper mb-40">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop3.jpg" alt="" /></a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-8">
                                    <div class="shop-desc">
                                        <h2><a href="#">Special Wonthan</a></h2>
                                        <span>$99.90</span>
                                        <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis
                                            praesentium voluptatum deleniti atque corrupti
                                            quos dolores et quas molestias excepturi sint occaecati cupiditate non
                                            provident, similique sunt in culpa qui officia deserunt
                                            mollitia animi, id est laborum et dolorum fuga.</p>
                                        <div class="shop-details">
                                            <a class="btn" href="#">View More</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row mb-20">
                                <div class="col-xl-4 col-lg-4 col-md-6">
                                    <div class="shop-wrapper mb-40">
                                        <div class="shop-img">
                                            <a href="#"><img src="asset/img/shop/shop4.jpg" alt="" /></a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-8">
                                    <div class="shop-desc">
                                        <h2><a href="#">Vegetable Pakura</a></h2>
                                        <span>$99.90</span>
                                        <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis
                                            praesentium voluptatum deleniti atque corrupti
                                            quos dolores et quas molestias excepturi sint occaecati cupiditate non
                                            provident, similique sunt in culpa qui officia deserunt
                                            mollitia animi, id est laborum et dolorum fuga.</p>
                                        <div class="shop-details">
                                            <a class="btn" href="#">View More</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="pagination text-center">
                        <ul>
                            <li class="active">
                                <a href="#">
                                    <span>1</span>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <span>2</span>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <span>3</span>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="fas fa-angle-double-right"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    </div>


</template>

<script>
export default {
    name: 'ShopView'
}
</script>