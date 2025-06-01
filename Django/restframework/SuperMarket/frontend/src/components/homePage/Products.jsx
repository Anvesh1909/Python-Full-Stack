import ProductCard from './ProductCard';


const Products = ({products}) => {


    const ListProducts = [
        {
            id: 1,
            name: "Milk Packet",
            description: "Milk Packet by PepsiCo in Snacks category.",
            brand: "PepsiCo",
            price: 181.43,
            stock: 17,
            is_available: true,
            image: null,
            created_at: "2025-04-12T12:09:08.148410Z",
            updated_at: "2025-04-12T12:09:08.148410Z",
            category: 2
        },
        {
            id: 2,
            name: "Cheese Slice",
            description: "Cheese Slice by Parle in Bakery category.",
            brand: "Parle",
            price: 143.49,
            stock: 42,
            is_available: true,
            image: null,
            created_at: "2025-04-12T12:09:08.160716Z",
            updated_at: "2025-04-12T12:09:08.160716Z",
            category: 4
        }
    ];


    


 

    return (
        <div className="container-fluid pt-3 bg-dark">
            <div className="row row-cols-md-4 row-cols-1 row-gap-2">
                {products.map(item => (
                    <ProductCard key={item.id} item={item} />
                ))}
            </div>
        </div>   
    );
};

export default Products;