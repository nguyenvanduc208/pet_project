<template>
  <header>
    <div id="sticky-header" class="header-top-area header-2 pr-60 pl-60">
      <div class="container-fluid">
        <div class="row">
          <div class="col-xl-3 col-lg-2">
            <div class="logo">
              <a href="index.html"><img src="/asset/img/logo/logo.png" alt="" /></a>
            </div>
          </div>
          <div class="col-xl-6 col-lg-8">
            <div class="main-menu text-center">
              <nav id="mobile-menu">
                <ul>
                  <li v-bind:class="{ active: $route.path === '/' }">
                    <router-link to="/">home </router-link>
                  </li>
                  <li><a href="about-us.html">about</a></li>
                  <li v-bind:class="{ active: $route.path === '/shop' }">
                    <router-link to="/shop">Shop</router-link>
                    <ul class="sub-menu text-left">
                      <li><a href="about-us.html">about</a></li>
                      <li><a href="error.html">error</a></li>
                      <li>
                        <a href="contact-classic.html">contact classic</a>
                      </li>
                      <li>
                        <a href="contact-simple.html">contact simple</a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a href="#">pages</a>
                    <ul class="sub-menu text-left">
                      <li><a href="about-us.html">about</a></li>
                      <li><a href="error.html">error</a></li>
                      <li>
                        <a href="contact-classic.html">contact classic</a>
                      </li>
                      <li>
                        <a href="contact-simple.html">contact simple</a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a href="blog-standard.html">blog</a>
                    <ul class="sub-menu text-left">
                      <li>
                        <a href="blog-standard.html">blog standard</a>
                      </li>
                      <li><a href="blog-list.html">blog list</a></li>
                      <li><a href="blog-details.html">blog details</a></li>
                    </ul>
                  </li>
                  <li><a href="contact-classic.html">contact</a></li>
                </ul>
              </nav>
            </div>
            <div class="mobile-menu"></div>
          </div>
          <div class="col-xl-3 col-lg-2">
            <div class="header-right f-right d-none d-md-none d-lg-block">
              <div class="header-button">
                <a href="#">get a quote</a>
              </div>
              <ul>
                <li>
                  <a href="#" data-toggle="modal" data-target="#search-modal"><span class="ti-search"></span></a>
                </li>
                <li>
                  <router-link to="/cart"><span class="ti-shopping-cart"></span></router-link>
                </li>
                <li class="info-bar">
                  <a href="javascript:void(0)"><span class="ti-align-right"></span></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="extra-info">
      <div class="close-icon">
        <button>
          <i class="far fa-window-close"></i>
        </button>
      </div>
      <div class="logo-side mb-30">
        <a href="index.html">
          <img src="/asset/img/logo/logo.png" alt="" />
        </a>
      </div>
      <div class="side-menu mb-30">
        <ul>
          <li>
            <a href="#">Home</a>
          </li>
          <li>
            <a href="#">About</a>
          </li>
          <li>
            <a href="#">Shop</a>
          </li>
          <li>
            <a href="#">Blog</a>
          </li>
          <li>
            <a href="#">Blog Details</a>
          </li>
          <li>
            <a href="#">Contact</a>
          </li>
        </ul>
      </div>
      <div class="instagram">
        <a href="#">
          <img src="/asset/img/instagram/1.jpg" alt="" />
        </a>
        <a href="#">
          <img src="/asset/img/instagram/2.jpg" alt="" />
        </a>
        <a href="#">
          <img src="/asset/img/instagram/3.jpg" alt="" />
        </a>
        <a href="#">
          <img src="/asset/img/instagram/4.jpg" alt="" />
        </a>
        <a href="#">
          <img src="/asset/img/instagram/5.jpg" alt="" />
        </a>
        <a href="#">
          <img src="/asset/img/instagram/6.jpg" alt="" />
        </a>
      </div>
      <div class="social-icon-right mt-20">
        <a href="#">
          <i class="fab fa-facebook-f"></i>
        </a>
        <a href="#">
          <i class="fab fa-twitter"></i>
        </a>
        <a href="#">
          <i class="fab fa-google-plus-g"></i>
        </a>
        <a href="#">
          <i class="fab fa-instagram"></i>
        </a>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>