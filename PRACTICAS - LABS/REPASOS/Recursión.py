#FACTORIAL
def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)

#EXPONENTE
def potencia(base, exponente): 
    if exponente == 0: 
        return 1
    else: 
        return base * potencia(base, exponente-1)

#FIBONNACI 
def fibo(n): 
    if n<= 2: 
        return n -1
    else: 
        return fibo(n-1) + fibo(n-2)

#MULTIPLICACION 
def multi(n1, n2): 
    if n1 == 0 or n2 == 0: 
        return 0 
    if n2 == 1: 
        return n1
    else: 
        return n1 + multi(n1, n2-1)
    
#MCD
def maxi(n1, n2):
    mayor = max(n1,n2)
    menor = min(n1,n2)
    if menor == 0: 
        return mayor
    else: 
        residuo = mayor % menor
        return maxi(menor, residuo)
    
    
def sumi(num): 
    if num < 10: 
        return num 
    else: 
        ulti = num % 10 
        numsinulti = num // 10 
        return ulti + sumi(numsinulti)

def sum_vectores(vector): 
    if len(vector) == 0: 
        return 0 
    else: 
        ultimoelemento = vector[len(vector) - 1]
        vectorsinelemento = vector[:-1]
        return ultimoelemento + sum_vectores(vectorsinelemento)


#!PALINDROMO 
#TODOvolver a practicar palindromo, es un ejercicio interesante para entender la recursividad.
def palindromo(palabra:str): 
    palabra = palabra.lower().strip()
    if len(palabra) == 0 or len(palabra) == 1: 
        return "Es palindromo"
    else:
        if palabra[0] == palabra[len(palabra) - 1]:
            return palindromo(palabra[1:-1])
        else: 
            return "No es palindromo"
print(palindromo("Anita lava latina"))

def invertir(num:int):
    if num < 10: 
        return num 
    else: 
        ultimo = num % 10
        numsinultimo = num // 10 


print(invertir(5875))

def invertir_pal(palabra:str): 
    if palabra == "": 
        return palabra
    else: 
        ultimo = palabra[len(palabra)-1]
        palabrasinultimo = palabra[:-1]
        return ultimo + invertir_pal(palabrasinultimo)

print(invertir_pal("HOLA"))

def sum_digitos(num):
    if len(str(num)) == 1: 
        return num 
    else:
        ultimo = str(num)[len(str(num))-1]
        numsinultimo = str(num)[:-1]
        total = int(ultimo) + sum_digitos(int(numsinultimo))
        
        if total < 10:
            return total

        else: 
            total_fin = str(total)[:-1]
            totalsinfin = str(total)[len(str(total))-1]
            tt = int(total_fin) + int(totalsinfin)
            return tt

print(sum_digitos(5558))


def sumi_digitos(num:int):
    if num < 10: 
        return num 
    else:
        ultimo = num % 10
        numsinultimo = num // 10
        total = ultimo + sumi_digitos(numsinultimo)
        if total < 10:
            return total
        else:
            return sumi_digitos(total)

def primo(num, i): 
    if num == 1: 
        return "No es primo"
    if i == 1: 
        return "Es primo"
    else: 
        if num % i == 0:
            return "No es primo"
        else: 
            return primo(num, i-1)

print(primo(7,6))