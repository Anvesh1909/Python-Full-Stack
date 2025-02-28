import React from 'react';
import {Link} from 'react-router-dom';

import {FaCartShopping} from 'react-icons/fa6';
import styles from "./NavBar.module.css"
import NavBarLink from './NavLink';

const NavBar = () => {
  return (
    <nav className={`navbar navbar-expand-lg navbar-light bg-white shadow-sm py-3 ${styles.stickyNavbar}`}>
        <div className="container">
            <Link className='navbar-brand fw-bold text-uppercase' to="/">SHOPIT</Link>
            <button
                className='navbar-toggle'
                type='button'
                data-bs-toggle='collapse' 
                data-bs-target='#navbarContent'
                aria-expanded='false'
                aria-label='Toggle navigation'
            >
                <span className='navbar-toggle-icon'></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarContent">
                <NavBarLink />
                <Link to='/cart' className={`btn btn-dark ms-3 rounded-pill position-relative ${styles.responsiveCart}`}>
                    <FaCartShopping/>
                    <span 
                        className='position-absolute top-o start-100 translate-middle badge rounded-pill'
                        style={{ fontSize:'0.85rem', padding:'0.5em 0.65em', backgroundColor:'#6050DC'}}
                    >
                        12
                    </span>
                </Link>
            </div>
        </div>
    </nav>
  )
}

export default NavBar
