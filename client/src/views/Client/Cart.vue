<template>
    <div class="breadcrumb-area pt-45 pb-45">
			<div class="container">
				<div class="row">
					<div class="col-xl-12">
						<div class="breadcrumb-text text-center">
							<h1>cart</h1>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- breadcrumb-area-end -->
		<!-- cart-area start -->
		<div class="cart-area pt-100 pb-100">
			<div class="container">
				<div class="row">
					<div class="col-xl-12">
						<div class="cart-table table-responsive">
							<table class="table table-bordered">
								<thead>
									<tr>
										<th scope="col">Product Image</th>
										<th scope="col">Product NAME</th>
										<th scope="col">PRICE</th>
										<th scope="col">QUANTITY</th>
										<th scope="col">TOTAL</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td><div class="cart-img"><img src="img/cart/1.jpg" alt=""></div></td>
										<td><div class="cart-name"><h4><a href="#">Daisy Coffee Table</a></h4></div></td>
										<td><div class="cart-price"><span>$350.00</span></div></td>
										<td><div class="cart-select">
											<select name="select" id="select">
												<option value="">01</option>
												<option value="">02</option>
												<option value="">03</option>
												<option value="">04</option>
											</select>
										</div></td>
										<td><div class="cart-del"><a href="#">X</a></div></td>
									</tr>
									<tr>
										<td><div class="cart-img"><img src="img/cart/1.jpg" alt=""></div></td>
										<td><div class="cart-name"><h4><a href="#">Daisy Coffee Table</a></h4></div></td>
										<td><div class="cart-price"><span>$350.00</span></div></td>
										<td><div class="cart-select">
											<select name="select" id="select2">
												<option value="">01</option>
												<option value="">02</option>
												<option value="">03</option>
												<option value="">04</option>
											</select>
										</div></td>
										<td><div class="cart-del"><a href="#">X</a></div></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
				<div class="row mt-20">
					<div class="col-xl-6 col-lg-6">
						<div class="coupon-left">
							<form action="#">
								<input type="text" placeholder="Coupon code">
								<button>Apply coupon</button>
							</form>
						</div>
					</div>
					<div class="col-xl-6 col-lg-6">
						<div class="update-cart text-left text-lg-right">
							<a href="#">CLEAR SHOPPING CART</a>
							<a href="#">UPDATE SHOPPING CART</a>
						</div>
					</div>
				</div>
				<div class="row pt-80">
					<div class="col-xl-5 offset-xl-7 col-lg-8  offset-lg-4 pl-0">
						<div class="section-title mb-20">
							<h2>CART TOTALS</h2>
						</div>
						<div class="cart-total-price">
							<ul>
								<li>Subtotal <span>$70</span></li>
								<li>Total <span>$70</span></li>
							</ul>
							<div class="text-right"><a class="btn brand-btn" href="#">CONTINUS SHOPPING</a></div>
						</div>
					</div>
				</div>
			</div>
		</div>

</template>

<script>
    export default {
        name: 'cart'
    }
</script>