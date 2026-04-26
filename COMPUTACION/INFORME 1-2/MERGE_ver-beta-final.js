let vector1 = []  // Declaramos los dos vectores globales para que puedan ser accedidos por ambas funciones
let vector2 = [] 

function create_vector(){
    const size1 = Number(document.getElementById('input_size1').value)
    const size2 = Number(document.getElementById('input_size2').value)

    if (!Number.isInteger(size1) || !Number.isInteger(size2) || size1 < 0 || size2 < 0){
        alert("INGRESE VALORES VALIDOS PARA LOS TAMAÑOS")
        return
    }
    let acumulador1 = 0 // Definimos un acumulador para cada vector, el cual se irá incrementando con números aleatorios para asegurar que los elementos del vector estén ordenados de forma creciente
    for (let i=0; i<size1; i++){
        let random = Math.floor(Math.random()*900 + 100)
        acumulador1 += random
        vector1[i] = acumulador1
    }

    let acumulador2 = 0
    for (let i=0; i<size2; i++){
        let random = Math.floor(Math.random()*900 + 100)
        acumulador2 += random
        vector2[i] = acumulador2
    }

    document.getElementById('output_vector1').innerHTML = `VECTOR 1: [${vector1}]`
    document.getElementById('output_vector2').innerHTML = `VECTOR 2: [${vector2}]`
}

function Merge_Trap(){
    let size1 = vector1.length
    let size2 = vector2.length
    vector1[size1] = vector2[size2 - 1] + 1 // Agregamos un centinela al final de cada vector, el valor del centinela es mayor que el último elemento del vector para asegurar que no interfiera con la comparación
    vector2[size2] = vector1[size1 - 1] + 1
    let size3 = size1 + size2
    let pos1 = 0
    let pos2 = 0
    let vector3 = new Array(size3)
    for (let i=0; i < size3; i++){
        vector3[i] = vector1[pos1] < vector2[pos2]?  // Comparamos los elementos de ambos vectores y agregamos el menor al vector3
        vector1[pos1++] : vector2[pos2++]; // OPERADOR TERNARIO: Si el elemento de vector1 es menor, lo agregamos a vector3 y avanzamos el puntero pos1, de lo contrario, agregamos el elemento de vector2 y avanzamos el puntero pos2
        
    }
    document.getElementById('output_merge_trap').innerHTML = `VECTOR MERGE #1: [${vector3}]`
}


function Merge(){
    let size1 = vector1.length - 1; // El tamaño real es uno menos porque el último elemento es el centinela, además la propiedad length tomo directamente el tamaño del arreglo, no el índice del último elemento 
    let size2 = vector2.length - 1;
    let vector3 = new Array(size1 + size2);

    let p1 = 0;
    let p2 = 0;
    let i = 0;

    // Mientras ambos tengan elementos, comparamos y agregamos el menor elemento de cualquiera de los vectores  al vector3
    while (p1 < size1 && p2 < size2){
        vector3[i++] = vector1[p1] < vector2[p2]?
        vector1[p1++] : vector2[p2++];
    }
    
    // COPIAMOS LOS ELEMENTOS RESTANTES DE CUALQUIERA DE LOS DOS VECTORES
    if (p1 < size1){
        for (let k = p1; k < size1; k++){
        vector3[i++] = vector1[k];
        }
    }

    if (p2 < size2){
        for (let r = p2; r < size2; r++){
            vector3[i++] = vector2[r];
        }
    }
    document.getElementById('output_merge').innerHTML =
        `VECTOR MERGE #2: [${vector3.join(', ')}]`;
}