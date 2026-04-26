// <!--#=========================================================DCOUMENTACION INTERNA=======================================================================================================================================================
// # -- Objetivo: Implementar los algoritmos de Factorial y Fibonacci en recursion e iteracion.
// # -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
// # -- Descipcion: Los algoritmos de Factorial y Fibonacci son métodos para calcular el factorial de un número y la secuencia de Fibonacci, respectivamente. Se implementan tanto de manera recursiva como iterativa para comparar su eficiencia y funcionamiento.
// # -- Lenguaje: JavaScript y HTML para la interfaz gráfica.
// # -- Recursos: Navegador Web
// # -- Procesos: 
// #    1. Implementar la función factorial de manera recursiva.
// #    2. Implementar la función factorial de manera iterativa.
// #    3. Implementar la función Fibonacci de manera recursiva.
// #    4. Implementar la función Fibonacci de manera iterativa.
// # -- Historia: Fecha de creacion 14/03/2026 Fecha de modificacion: 16/03/2026
// # -- Ajustes pendientes: Ninguno 
// # ======================================================================================================================================================================================================================================-->



// ===========================================FUNCIONES RECURSIVAS========================================

function call_rfact(){
    let num = Number(document.getElementById('input_num').value)
    document.getElementById('span_rfact').innerHTML = `El factorial de ${num} es: ${recu_fact(num)}`
}

function recu_fact(num){
    if (num<=1){
        return num 
    }
    if (num<0){
        alert("No se puede calcular el factorial de un negativo")
    }
    else{
        return num * recu_fact(num-1)
    }

}

function call_rfibo(){
    let num = Number(document.getElementById('input_num').value)
    document.getElementById('span_rfib').innerHTML = `El término ${num} de la sucesión de Fibonacci es: ${recu_fibo(num)}`
}

function recu_fibo(num){
    if (num <= 0){
        alert("No existe ningun termino en la sucesion con ese índice")
    }
    if (num <= 2){
        return num-1
    }
    else{
        return recu_fibo(num-1) + recu_fibo(num-2)
    }
}

//==================================================FUNCIONES ITERATIVAS===================================================
function ite_fact(){
    let num = Number(document.getElementById('input_num').value)
    let acu = 1
    for (let i=1; i<=num; i++){
        acu *= i 
    }
    document.getElementById('span_fact_ite').innerHTML = `El factorial de ${num} es: ${acu}`
}

function ite_fibo(){
    let num = Number(document.getElementById('input_num').value)
    if (num <= 0){
        alert("No existe el elemento de indice 0 o menor en la sucuesion de fibonnaci")
    }
    if (num <= 2){
        return num - 1
    }
    else{
        let anterior = 0
        let posterior = 1
        let siguiente = 0
        for (let i=1; i<num;i++){
            siguiente = anterior + posterior
            anterior = posterior
            posterior = siguiente
        }
        document.getElementById('span_fibo_ite').innerHTML = `El término ${num} de la sucesión de Fibonacci es: ${anterior}`
    }
    
}