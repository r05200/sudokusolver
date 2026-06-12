import React from 'react'
import '../styling/index.css'
function Grid({side_l}) {
  
  return (
    <div className="flex">
        <table className="flex-1">
          <tbody>
            {
              Array.from({length: side_l},(_,index) => <tr key={index}>
                {
                Array.from({length: side_l},(_,idx) => 
                <td key={idx} className="border-2"> 
                  {index}
                </td>)
                }
            </tr>)
            }
            
          </tbody>
        </table>
    </div>
  )
}

export default Grid