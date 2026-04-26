import math

def multi(a,b): 
    if a==0 or b ==0: 
        return 0
    if a==1:
        return b
    else: 
        return b + multi(a-1,b)

def invertir(num): 
    if num < 10: 
        return num
    else: 
        ulti = num % 10
        sinulti = num //10 
        digitos = math.floor(math.log10(num))+1
        elevado = ulti * (10**(digitos - 1))
        return elevado + invertir(sinulti)

print(invertir(123))

def palindromo(palabra:str): 
    if len(palabra) <=1: 
        return "Es palindromo"
    else: 
        if palabra[0] == palabra[-1:]:
            return palindromo(palabra[1:-1])
        else: return "No es palidromo"

#print(palindromo("HANNAH"))


def sumar(num:int): 
    if num < 10: 
        return num
    else: 
        ulti = num % 10
        sinulti = num // 10 
        suma =  ulti + sumar(sinulti)
        if suma < 10: 
            return suma
        else: 
            return sumar(suma)

print(sumar(18))


def contarp(num:int): 
    if num < 10 and num%2==0: 
        return 1
    else: 
        ulti = num % 10 
        sinulti = num // 10 
        if ulti % 2 == 0: 
            return 1 + contarp(sinulti)
        else: 
            return contarp(sinulti)

#4674
#467 4 

def contarc(num:int): 
    if num == 0:
        return 0 
    else: 
        ulti = num % 10 
        sinulti = num // 10 
        print(ulti, sinulti)
        if ulti == 0: 
            return 1 + contarc(sinulti)
        else: 
            return contarc(sinulti)
        
        

#10200
#1020  0 1
#102   0 2
#10 


print(contarp(4674))

print(contarc(1020050))


def invertirpalabra(palabra): 
    if len(palabra) <= 1: 
        return palabra
    else: 
        ulti = palabra[-1:]
        sinultimo = palabra[:-1]
        return ulti + invertirpalabra(sinultimo)
    
print(invertirpalabra("HOLA"))

def contarv(palabra): 
    if len(palabra) <= 1: 
        return 0
    else: 
        ulti = palabra[-1:]
        sinulti = palabra[:-1]
        if ulti in "aeiou": 
            return 1 + contarv(sinulti)
        else: 
            return contarv(sinulti)

print(contarv("hola"))


def enthex(num):
    hexas = "0123456789ABCDEF"
    if num == 0: 
        return ""
    else: 
        resto = num % 16 
        reducido = num // 16 
        return  str(enthex(reducido)) + str(hexas[resto]) 

print(enthex(16))

def entbin(num): 
    if num == 0: 
        return ""  
    else: 
        resto = num % 2
        reducido = num // 2
        return str(entbin(reducido)) + str(resto)

print(entbin(8))

def binent(num:str): 
    if num == "": 
        return 0
    else: 
        primero = num[0]
        sinpri = num[1:]
        digito = math.floor(math.log10(int(num)))+1




        

