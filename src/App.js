import './App.css';
import {useState, useEffect} from 'react';
import CategoriasList from './components/CategoriasList'
import FormCategoria from './components/FormCategoria'





function App() {

  const [categorias, setCategorias] = useState([])
  const [editedCategoria, setEditedCategoria] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:5000/categoria/',{
      'method':'GET',
      headers: {'Content-Type': 'application/json'}
  
    })
    .then(response => response.json())
    .then(response => setCategorias(response))
    .catch(err => console.error(err))
  },[])


  // EDITAR CATEGORIA
  const editCategoria = (categoria) => {
    //console.log("Hello World Editar Categoria");
    setEditedCategoria(categoria)
    
  }
 

  return (
    <div className="App">
      <CategoriasList categorias = {categorias} editCategoria = {editCategoria}/>

      {editedCategoria ? <FormCategoria categoria = {editedCategoria}/> : null}
      
    </div>
  );
}

export default App;
