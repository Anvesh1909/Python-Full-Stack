import './App.css';

import { BrowserRouter,Routes,Route } from 'react-router-dom'

import MainLayout from './layout/MainLayout';
import HomePageLayout from './components/homePage/HomePageLayout';
import ViewProduct from './components/ProductPage/ViewProduct';
import Signup from './components/user/Signup';
import Login from './components/user/login';

function App() {
  

    return (
      <>

		<BrowserRouter>
			<Routes>
				<Route path='/' element={<MainLayout />}>
					<Route index element={<HomePageLayout />} />
					<Route path='product/:id' element={<ViewProduct />}/> 
					<Route path='login' element={<Login />}/>  
					<Route path='signup' element={<Signup />}/>  

				</Route>
			</Routes>
      	</BrowserRouter>

      </>
    )
}
      
export default App
