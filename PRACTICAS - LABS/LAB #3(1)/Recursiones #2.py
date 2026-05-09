

#===========================BUSQUEDA BINARIA ===========================
import re

num = 8
vector = [1,2,3,4,5,6,7,8]
li = 0
ls = len(vector)-1
def busquedabin(num, vector, li, ls): 
    if li>ls: 
        return "No encontrado"
    else: 
        mitad = (li + ls) // 2
        if vector[mitad] == num: 
            return f"El numero {num} si esta, en la posicion {mitad+1}"
        
        else:
            if vector[mitad] > num:
                ls = mitad - 1
                return busquedabin(num, vector, li, ls)
            else: 
                li = mitad + 1
                return busquedabin(num, vector, li, ls)

#print(busquedabin(num, vector,li, ls))

#=====================INRVETIR NUMERO=====================

def invertir(num):
    contador = 0
    if num < 10: 
        return num 
    
    else: 
        ulti = num % 10 
        sinulti = num // 10 
        temp = sinulti
        
        while temp > 0: 
            temp = temp // 10 
            contador += 1
        
        elevado = ulti * (10**(contador))
        
        return elevado + invertir(sinulti)
        
#print(invertir(1234))


#============Palindromo==================
def palindromo(palabra): 
    if len(palabra) <=1: 
        return "Es palindromo"
    else: 
        if palabra[0] == palabra[-1:]: 
            return palindromo(palabra[1:-1])
        else: 
            return "No es Palindromo"

#print(palindromo("anna"))

#===============Palindromo de un vector==============
def pvector(vector): 
    if len(vector) <=1: 
        return "Es palindromo"
    else: 
        if vector[0] == vector[-1:]: 
            return pvector(vector[1:-1])
        else: 
            return "No es palindromo"


#============Mayores/Cantidad=========
def mayores(num, cont, mayor): 
    if num < 10: 
        return mayor, cont
    else: 
        ulti = num % 10 
        sinulti = num // 10 
        if ulti > mayor: 
            mayor = ulti
            cont = 0
        if ulti == mayor: 
            cont += 1
        return mayores(sinulti, cont, mayor)

#print(mayores(67768, 0, 0))

def nump(num, cont, div): 
    if cont == num: 
        return "Es perfecto"
    else: 
        if num % div == 0: 
            cont += div
        if cont > num: 
            return "No es perfecto"
        
        return nump(num, cont, div+1)
    
#print(nump(73,0,1))


vector = [1,2,4,5]
def vectormayor(vector): 
    if len(vector) <=1: 
        return vector 
    else: 
        primero = vector[0]
        ultimo = vector[-1]
        if primero > ultimo: 
            return vectormayor(vector[:-1])
        else: 
            return vectormayor(vector[1:])
        
#print(vectormayor(vector))

def pospares(vector, acu): 
    if len(vector)<=1: 
        return acu
    else: 
        ulti = vector[-1]
        sinulti = vector[:-1]
        largo = len(vector)
        if largo % 2 == 0: 
            acu += ulti
            return pospares(sinulti, acu)
        else: 
            return pospares(sinulti, acu)
        
#print(pospares(vector,0))

#========================GAUSS==================
def gauss(num): 
    if num == 0: 
        return 0
    else: 
        return num + gauss(num-1)

#print(gauss(100))

#=====================TORRES DE HANNOI==================
def hannoi(anillos, a, b, c): 
    if anillos == 1: 
        return print(f"Mover {a} hacia {c}")
    else: 
        hannoi(anillos-1, a,c,b)
        hannoi(1,a,b,c)
        hannoi(anillos-1,b,a,c)

#print(hannoi(2,"T1","T2","T3"))

#=======================C0NTAR DIGITOS==================
num = 1
def contardigitos(num): 
        if num < 10: 
            return 1
        else: 
            sinulti = num // 10
            return 1 + contardigitos(sinulti)

#print(contardigitos(num))


def capicua(num): 
    if len(num) <= 1: 
        return "Es capicua"
    else: 
        ultimo = num[-1] 
        primero = num[0]
        if primero == ultimo: 
            sinup = num[1:-1]
            return capicua(sinup)
        else: 
            return "No es capicua"


#print(capicua("15155"))

def invertirnum(num): 
    if num < 10: 
        return num 
    else: 
        ulti = num % 10 
        sinult = num // 10 
        
        lent = sinult
        c = 0
        while lent > 0: 
            lent = lent // 10
            c+=1
            
        elevado = ulti * (10**c)
        return elevado + invertirnum(sinult)
    
print(invertirnum(123))

def invt(num): 
    if num < 10: 
        return num
    else: 
        ult = num % 10 
        sinult = num // 10 
        elevaldo = ult * 10**(len(str(sinult)))
        return elevaldo + invt(sinult)

print(invt(123))

def bina(num): 
    if num == 0:
        return "" 
    else: 
        resto = num % 2
        numb = num // 2 
        return bina(numb) + str(resto)

print(bina(4))

def bint(bins): 
    if bins == "": 
        return 0 
    else: 
        pass