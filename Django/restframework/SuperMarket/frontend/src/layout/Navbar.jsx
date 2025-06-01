import React from 'react';

import img from '../assets/GroceryGo1.png';
import {NavLink} from 'react-router-dom'


const navbar = () => {
    
    return (
        <header>
			<nav className="navbar navbar-expand-lg bg-dark navbar-dark">
				<div className="container">
					<NavLink className="navbar-brand" to=''><img src={img} alt="logo" height={60} /></NavLink>
					<button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
						<span className="navbar-toggler-icon"></span>
					</button>
					<div className="collapse navbar-collapse" id="navbarSupportedContent">
						<button className="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
							<i className="fas fa-times"></i>
						</button>
						<ul className="navbar-nav ms-auto me-lg-3">
						

							<li className="nav-item">
								<NavLink className="nav-link" aria-current="page" to=''>Home</NavLink>
							</li>
						
						</ul>
						<div className="d-lg-flex col-lg-3 justify-content-lg-end">
                            <div className="text-end">
                        
                                    <NavLink  to='login' className="btn btn-outline-light me-2">Login</NavLink>
                                    <NavLink  to='signup' className="btn btn-warning">Sign-up</NavLink>

                            </div>
                        </div>
					</div>
				</div>
			</nav>
		</header>
    )
}

export default navbar
