import React from 'react'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import HomePage from "./components/home/HomePage"
import MainLayout from "./layout/MainLayout"
import NotFoundPage from './components/ui/NotFoundPage'
import ProductPage from './components/Product/ProductPage'

const App = () => {
  return (
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<MainLayout />}>
            <Route index element={<HomePage />} />
            <Route path='products/:slug' element={<ProductPage />}/>  
            <Route path='*' element={<NotFoundPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
  )
}

export default App
