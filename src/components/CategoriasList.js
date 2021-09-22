import React from 'react'

function categoriasList(props) {


    const editCategoria = (categoria) => {

        props.editCategoria(categoria)
    }


    return (
        <div>
            <h1>Sergio Sanmiguel</h1>

            <div class="row justify-content-center">
                <h2>Clasificaciones</h2>
            </div>
            <div class="card-header">
                <a
                    class="btn btn-primary btn-sm"
                    href="127.0.0.1"
                    data-toggle="modal"
                    data-target=""
                >Nueva Clasificación</a>
                

            </div>



            <table class="table table-light">
                <thead>
                    <tr>
                    <td>#</td>
                    <td>Nombre</td>
                    <td>Acciones</td>
                    </tr>
                </thead>

                <tbody>

                    {props.categorias && props.categorias.map(categoria => {
                        return (

                            <tr>
                                <td>{categoria.id}</td>
                                <td>{categoria.nombre}</td>
                                <td>
                    
                                    <i class="far fa-edit"></i>
                                    |
                                    <i class="far fa-trash-alt" onClick={() => editCategoria(categoria)}></i>
                                </td>
                            </tr>
        
                        )
                    })}

                </tbody>
            </table>
        </div>
    )
}

export default categoriasList
