import React from 'react';
import { baseURL } from '../../api';

import {Link} from 'react-router-dom'


const Hero = ({ item }) => {
    console.log(item);

    return (
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <div id="carouselExampleDark" className="carousel carousel-dark slide" data-bs-ride="carousel">
                        <div className="carousel-indicators">
                            {[0, 1, 2].map(index => (
                                <button
                                    key={index}
                                    type="button"
                                    data-bs-target="#carouselExampleDark"
                                    data-bs-slide-to={index}
                                    className={index === 0 ? 'active' : ''}
                                    aria-current={index === 0 ? 'true' : undefined}
                                    aria-label={`Slide ${index + 1}`}
                                />
                            ))}
                        </div>

                        <div className="carousel-inner">
                            {item.slice(1, 4).map((prod, index) => (
                                <div
                                    className={`carousel-item ${index === 0 ? 'active' : ''}`}
                                    key={prod.id}
                                    data-bs-interval={5000}
                                >
                                    <div className="container py-5">
                                        <div className="row align-items-center">
                                            <div className="col-lg-6 mb-4 mb-lg-0 text-center">
                                                <img
                                                    src={`${baseURL}/${prod.image}`}
                                                    className="img-fluid rounded shadow"
                                                    alt={prod.name}
                                                    style={{ maxHeight: '400px', objectFit: 'cover' }}
                                                />
                                            </div>
                                            <div className="col-lg-6 text-white">
                                                <h1 className="display-6 fw-bold mb-3">{prod.name}</h1>
                                                <p className="lead">{prod.description || prod.discription || 'No description available.'}</p>
                                                <div className="d-flex gap-3">
                                                    <Link to={`product/${prod.id}`} className="btn btn-primary btn-lg">Shop Now</Link>
                                                    <button className="btn btn-outline-light btn-lg">Add to Wishlist</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>

                        <button
                            className="carousel-control-prev"
                            type="button"
                            data-bs-target="#carouselExampleDark"
                            data-bs-slide="prev"
                        >
                            <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span className="visually-hidden">Previous</span>
                        </button>
                        <button
                            className="carousel-control-next"
                            type="button"
                            data-bs-target="#carouselExampleDark"
                            data-bs-slide="next"
                        >
                            <span className="carousel-control-next-icon" aria-hidden="true"></span>
                            <span className="visually-hidden">Next</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Hero;
