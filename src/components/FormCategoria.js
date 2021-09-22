import React from 'react';
import {useState} from 'react';
import APIService from '../components/APIService';


function FormCategoria(props) {

    const[id, setId] = useState(props.categoria.id)
    const[nombre, setNombre] = useState(props.categoria.nombre)

    const actualizaCategoria = () => {
        APIService.ActualizaCategoria(props.categoria.id, {nombre})
        .then(response => console.log(response)) 
        .catch(err => console.error(err))

    }

    return (
        <div>
            {props.categoria ? (

                <div className="mb-3">
                    <label htmlFor = "title" className= "form-label"> Id</label>
                    <input type="text" value={id} className="form-control"  />

                    <label htmlFor = "title" className= "form-label"> Nombre</label>
                    <input type="text" className="form-control"  value={nombre} onChange = {(e) => setNombre(e.target.value)} placeholder="Ingrese Nombre"/>

                    <button type="submit" className="btn btn-success mt-3" onClick={actualizaCategoria} >Actualizar</button>
                </div>
            ):null}






            
        </div>
    )
}

export default FormCategoria
