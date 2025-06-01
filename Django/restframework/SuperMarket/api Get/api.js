import axios from "axios";

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/products/',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});


api.get("allProducts")
.then(res =>{
    console.log(res.data);
}).catch(err=>{
    console.log(err.message);
});


