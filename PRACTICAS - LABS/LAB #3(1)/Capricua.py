lista = []
def collatz(num):
    lista.append(num)
    if num == 1: 
        return lista
    else: 
        if num % 2 == 0: 
            return collatz(num//2)
        else: 
            return collatz((num *3)+1)


print(collatz(7))