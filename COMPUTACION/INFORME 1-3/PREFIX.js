// <!--=========================================================DOCUMENTACION INTERNA=================================================================================================
// -- Objetivo: Implementar un programa que permita al usuario ingresar una expresión en notación prefix y calcular su resultado.
// -- Autor: Elmer Juarez / Correo de contacto: e24.elmerjuarez.juareza@suizoamaericano.edu.gt
// -- Descripción: El programa permite al usuario ingresar una expresión en notación prefix, calcular su resultado y mostrarlo en una interfaz gráfica.
// -- Lenguaje: HTML, Javascript y CSS
// -- Recursos: Navegador Web.
// -- Procesos: 
//       1. El usuario ingresa una expresión en notación prefix.
//       2. El programa evalúa la expresión y calcula su resultado.
//       3. El resultado se muestra en la interfaz gráfica.
// -- Historia: 
//       Fecha de creación: 24/04/2026
//       Fecha de modificación: 26/04/2026
// -- Ajustes pendientes: Mejorar la visualización de expresiones largas, agregar más operadores.
// -- Cambios Realizados: Implementación del cálculo de expresiones prefix, además de que se agregó un mejor CSS
// ======================================================================================================================================================================================-->

let pos = 0;
function call_prefix() {
    const input = document.getElementById('input');
    const output = document.getElementById('output');
    if (!input || !output) {
        return;
    };

    pos = -1;
    const expresion = input.value;
    const resultado = prefix(expresion);
    output.textContent = String(resultado);
}
function prefix(expresion) {
    pos += 1;
    let char = expresion[pos];

    if (char == "V") {
        return "Es verdadero";
    }
    if (char == "F") {
        return "Es falso";
    }
    else {
        if (char == "&") {
            let post = prefix(expresion);
            let prev = prefix(expresion);
            if (post == "V" && prev == "V") {
                return "Es verdadero";
            }
            else {
                return "Es Falso";
            }
        }
        if (char == "|") {
            let post = prefix(expresion);
            let prev = prefix(expresion);
            if (post == "V" || prev == "V") {
                return "Es verdadero";
            }
            else {
                return "Es falso";
            }
        }
        if (char == "!") {
            let post = prefix(expresion);
            if (post == "F") {
                return "Es Verdadero";
            }
            else {
                return "Es Falso";
            }
        }
    }
}
