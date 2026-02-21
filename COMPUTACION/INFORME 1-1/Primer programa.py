import time 

tiempo = time.time() + 5 
numb = 1 
cont_primo = 1
lista = [2]
while time.time() < tiempo: 
    numb += 2
    primo = True
    #factor = 2
    #while factor * factor <= numb: 
    for factor in lista:   
        if numb % factor == 0: 
            primo = False 
            break
        factor += 1
        if primo: 
            cont_primo += 1
            print(numb)
    #for factor in range(2, int)
print(f"Hay {cont_primo} numeros primos")
    

    