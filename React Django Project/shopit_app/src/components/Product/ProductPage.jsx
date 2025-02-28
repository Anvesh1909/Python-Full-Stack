import React, { useEffect, useState } from 'react';
import RelatedProducts from './RelatedProducts';
import ProductPagePlaceHolder from './ProductPagePlaceHolder';
import { useParams } from 'react-router-dom';

import api from '../../api';

const ProductPage = () => {

    const {slug } = useParams()
    const {product, setProduct} = useState()
    const {similarProducts, setSimilarProducts} = useState([])
    const {loading, setLoading} = useState(false)

    useEffect(function(){
        setLoading(true)
        api.get(`product_detail/${slug}`)
        .then(res=>{
            console.log(res.data);
            setProduct(res.data)
            setSimilarProducts(res.data.similarProducts)
            setLoading(false)
        })
        .catch(err=>{
            console.log(err.message)
            setLoading(false)
        })
    },[])

  return (
    <div>
      <ProductPagePlaceHolder />
      <section className="py-3">
        <div className="container py-4 px-lg-5 my-5">
          <div className="row gx-4 gx-lg-5 align-items-center">
            <div className="col-md-6">
              <img className="card-img-top mb-5 mb-md-0" src="" alt="kvlnogf" />
            </div>
            <div className="col-md-6">
              <div className="small mb-1">SKU: BST-498</div>
              <h1 className="display-5 fw-bolder"></h1>
              <div className="fs-5 mb-5">
                <span className="text-decoration-line-through">$45.00</span>
                <span>$40.00</span>
              </div>
              <p className="lead">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta minus molestias id qui reprehenderit at
                quia deleniti cumque ipsam excepturi hic beatae, delectus magnam vitae, ex ratione eius.
                Necessitatibus, reiciendis.
              </p>
              <div className="d-flex">
                <input
                  className="form-control text-center me-3"
                  id="inputQuantity"
                  type="number"
                  value="1"
                  style={{ maxWidth: '3rem' }}
                />
                <button className="btn btn-outline-dark flex-shrink-0" type="button">
                  <i className="bi-cart-fill me-1"></i>
                  Add to cart
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
      <RelatedProducts />
    </div>
  );
};

export default ProductPage;
