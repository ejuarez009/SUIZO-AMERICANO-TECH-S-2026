
let  vector_global = []
function crear_vector(){
    let tamaño = Number(document.getElementById('input_tamaño').value)
    let vector = new Array(tamaño)
    for(let i=0; i<tamaño;i++ ){
        vector[i] = Math.trunc(Math.random()*10)
    }
    vector_global = vector
}

function call_quick(){
    let ordenado = quicksorrt(vector_global)
    document.getElementById('vector_ordenado').innerHTML = "El vector ordenado es:" + ordenado 
}

function quicksorrt(vector){
    if (vector.length<=1){
        return vector
    }
    else{
        let pos_pivote = Math.trunc((vector.length)/2)
        let pivote = vector[pos_pivote]
        let mayores = []
        let menores = []
        for (let i=0; i<pos_pivote;i++){
            if (vector[i] < pivote){
                menores.append(vector[i])
            }
            else{
                mayores.append(vector[i])
            }
        }
        for (let i=pos_pivote+1; i<vector.length;i++){
            if (vector[i] < pivote){
                menores.append(vector[i])
            }
            else{
                mayores.append(vector[i])
            }
        }
        return quicksorrt(menores) + [pivote] + quicksorrt(mayores)
    }

}