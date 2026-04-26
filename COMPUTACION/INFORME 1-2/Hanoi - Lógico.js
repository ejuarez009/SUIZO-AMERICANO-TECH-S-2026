function call_hanoi(){
    let num = Number(document.getElementById('input_anillos').value)
    let torre1 = "Torre 1"
    let torre2 = "Torre 2"
    let torre3 = "Torre 3"
    let resultado = hanoi(num, torre1, torre2, torre3)
    document.getElementById('output_movs').innerHTML = resultado
}



function hanoi(n, t1, t2, t3){
    let movimiento = ""
    if (n==1){
        movimiento += `Mover ${n} anillo; desde ${t1}, hacia ${t3}` 
    }
    else{
        movimiento += hanoi(n-1,t1,t3,t2) + '<br>'
        movimiento += hanoi(1,t1,t2,t3) + '<br>'
        movimiento += hanoi(n-1,t2,t1,t3)
    }
    return movimiento 
}