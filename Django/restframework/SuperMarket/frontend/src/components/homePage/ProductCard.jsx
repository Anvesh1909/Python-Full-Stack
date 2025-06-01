import React from 'react'

import { baseURL } from '../../api'

import {Link} from 'react-router-dom'

const ProductCard = ({item}) => {




  return ( 
    <div className="col">
        <div className="card">
			<img src={`${baseURL}/${item.image}`} className="card-img-top image-fluid" alt="..." />
			<div className="card-body">
				<h5 className="card-title">{item.name}</h5>
				<h5 className="card-subtitle">₹ {item.price}</h5>

				<p className="card-text">{item.description}</p>
				<p className="card-text">{item.brand}</p>
				<p className="card-text">Available : {item.stock}</p>

				<Link to={`product/${item.id}`} className="btn btn-primary w-100" >
				View Product
				</Link>
				
			</div> 
      	</div>
    </div>
  )
}

export default ProductCard
