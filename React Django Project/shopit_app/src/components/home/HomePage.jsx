import React, { useEffect, useState } from 'react'
import Header from './Header'
import CardContainer from './CardContainer'

import api from '../../api'
import PlaceHolderContainer from '../ui/placeHolderContainer'

import ErrorComp from '../ui/ErrorComp'

const HomePage = () => {

	const [products, setProducts] = useState([]);
	const [loading, setLoading] = useState(false);
	const [error,setError] = useState("")

	useEffect(() => {
		setLoading(true)
		api.get("products")
		.then(res => {
			console.log(res.data); 
			setProducts(res.data);
			setLoading(false)
			setError("")
		}).catch(err => {
		  	console.log(err.message);
			setLoading(false)
			setError(err.message)
		});
	}, []);
	  



	return (
		<>
			<Header />
			{/* { loading &&  <PlaceHolderContainer /> }
			<CardContainer products={products} /> */}
			{/* { loading ? <PlaceHolderContainer /> : <CardContainer products={products} /> } */}

			{ error && <ErrorComp error={error} /> } 
			{loading && <PlaceHolderContainer />}
			{ loading || error!="" || <CardContainer products={products} /> }
 
		</>
	)	
}

export default HomePage
