import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api, { baseURL } from '../../api';

const ViewProduct = () => {
	const { id } = useParams();
	const [product, setProduct] = useState(null);

	useEffect(() => {
		api.get(`products/allProducts?id=${id}`)
			.then(res => {
				console.log(res.data);
				setProduct(res.data);
			})
			.catch(err => {
				console.log(err.message);
				setProduct(null);
			});
	}, [id]);

	return (
		<div className="container mt-5">
			{product ? (
				<div className="row featurette pt-5">
					<div className="col-md-5 order-md-1">
						<img src={`${baseURL}${product.image}`} alt={product.name} className="img-fluid" />
					</div>
					<div className="col-md-7 order-md-2">
						<h2 className="featurette-heading fw-normal lh-1">{product.name}</h2>
						<p className="lead">{product.description}</p>
					</div>
				</div>
			) : (
				<p>Loading...</p>
			)}
		</div>
	);
};

export default ViewProduct;
