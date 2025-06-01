import React from 'react'
import Hero from './Hero'
import Products from './Products'
import { useEffect, useState } from 'react';
import api from '../../api'

const HomePageLayout = () => {
    
    const [products, setProducts] = useState([]);

    useEffect(() => {
        
        api.get("products/allProducts")
        .then(res =>{
            console.log(res.data);
            setProducts(res.data)
        }).catch(err=>{
            console.log(err);
        });
    
    },[]);

    return (
        <div className='container-fluid px-5 bg-dark'>
            <Hero item={products}/>
            <Products products={products} />
        </div>

    )
}

export default HomePageLayout
