

export default class APIService {
    static ActualizaCategoria(id, nombre){
        return fetch(`http://127.0.0.1:5000/categoria/update/${id}`,{
        'method':'PUT',
        headers: {'Content-Type': 'application/json',"Access-Control-Allow-Headers" : "Content-Type",
        "Access-Control-Allow-Origin": "https://www.example.com",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"},
        nombre: JSON.stringify(nombre)
    
        })
        .then(response => response.json())

    }
}

