// #=========================================================DCOUMENTACION INTERNA=======================================================================================================================================================
// # -- Objetivo: Resolver el problema de calcular la potencia de un número utilizando tanto iteración como recursión, y comparar los resultados obtenidos por ambos métodos.
// # -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
// # -- Descipcion: Los algoritmos de potencia son métodos para calcular la potencia de un número. Se implementan tanto de manera recursiva como iterativa para comparar su eficiencia y funcionamiento.
// # -- Lenguaje: JavaScript y HTML para la interfaz gráfica.
// # -- Recursos: Navegador Web
// # -- Procesos: 
// #    1. Implementar la función de potencia de manera recursiva.
// #    2. Implementar la función de potencia de manera iterativa.
// # -- Historia: Fecha de creacion 18/03/2026 Fecha de modificacion: 20/03/2026
// # -- Ajustes pendientes: Ninguno 
// # ======================================================================================================================================================================================================================================-->


function ite_log2(){
    let base = Number(document.getElementById("input_base").value);
    let exponente = Number(document.getElementById("input_exponente").value);
    let potencia = 1
    if (exponente < 0){
            exponente = -exponente
            for (let i=1; i<=exponente; i++){
            potencia *= 1/ base   
            }
    }
    else{
        for (let i=1; i<=exponente; i++){
        potencia *= base
        }    
    }
    
    document.getElementById('output_ite').innerHTML = `La potencia en iteracion es: ${potencia}`
}


function call_log2(){
    let base = Number(document.getElementById("input_base").value);
    let exponente = Number(document.getElementById("input_exponente").value);
    let potencia = recu_log2(base, exponente)
    document.getElementById('output_rec').innerHTML = `La potencia en recursion es: ${potencia}`
}

function recu_log2(b, expo){
    if (expo == 0){
        return 1
    }
    else if (expo<0){
        return 1 / recu_log2(b, -expo) 
    }

    else{
        let potenciado = recu_log2(b, Math.trunc(expo/2))
        if (expo % 2 == 0){
            return potenciado * potenciado
        }
        else{
            return potenciado * potenciado * b
        }
    }
}