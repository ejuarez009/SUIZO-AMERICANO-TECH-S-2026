"use strict";
let pos = 0;
function call_prefix() {
    const input = document.getElementById('input');
    const output = document.getElementById('output');
    if (!input || !output) {
        return;
    }
    ;
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
            if (post == "F" || prev == "F") {
                return "Es Falso";
            }
            else {
                return "Es Verdadero";
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
