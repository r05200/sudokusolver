import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'

import App from './components/App.jsx'

const router = createBrowserRouter([{
  path: '/',
  element: <App />
},
{
  path: '/generate',
  element: <></>
}])
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router}/>
  </StrictMode>,
)
