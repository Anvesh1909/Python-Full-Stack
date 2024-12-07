import axios from 'axios';
import React, {useEffect , useState} from 'react'

function Student() {

    const { details, setDetails } = useState([]);
    const { formData, setFormData }  = useState({'id' : '', 'name' : '', 'age' : 0});


    const fetchDetails = async () => {
        try{
            const response = await axios.get("http://127.0.0.1:8000/api/all/");
            setDetails(response.data);
        }
        catch(error){
            console.log(error);
        }
    }
    
    
    useEffect(()=>{
        fetchDetails()
    },[]);


    return (
        <div>
            Student Form




            {
                details.map((detail) => {
                    <div>
                        name : {detail.name}
                        age : {detail.age}
                    </div>
                } )
            }
        </div>
    )
}

export default Student