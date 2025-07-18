import React from 'react'

const login = () => {
    return (
        <div className="container mt-5 p-5">
			<div class="row align-items-center g-lg-5 py-5">
				<div class="col-lg-7 text-center text-lg-start">
					<h1 class="display-4 fw-bold lh-1 text-body-emphasis mb-3">GroceryGo</h1>
					<p class="col-lg-10 fs-4">Login form</p>
				</div>
				<div class="col-md-10 mx-auto col-lg-5">
					<form class="p-4 p-md-5 border rounded-3 bg-body-tertiary">
						<div class="form-floating mb-3">
							<input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" />
							<label for="floatingInput">Email address</label>
						</div>
						<div class="form-floating mb-3">
							<input type="password" class="form-control" id="floatingPassword" placeholder="Password" />
							<label for="floatingPassword">Password</label>
						</div>
						<div class="checkbox mb-3">
							<label>
								<input type="checkbox" value="remember-me" /> Remember me
							</label>
						</div>
						<button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
						<hr class="my-4" />
						<small class="text-body-secondary">Login Here</small>
					</form>
				</div>
			</div>
        </div>
    )
}

export default login
