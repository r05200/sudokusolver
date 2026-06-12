import { useState } from 'react'
import Navbar from './Navbar'
import Grid from './Grid'


function App() {
  

  return (
    <>
      <div>
        <div>
          <Navbar />
        </div>
        <Grid side_l={4} />
      </div>
    </>
  )
}

export default App
