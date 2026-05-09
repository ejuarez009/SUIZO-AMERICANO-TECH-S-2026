
import re


num = 5
lista = []
def conjetura(num):
    lista.append(num)
    if num == 1: 
        return num
    else:
        if num % 2 == 0: 
            return conjetura(num// 2)
        else: 
            return conjetura((num*3)+1)

print(conjetura(num))

while num != 1: 
    if num % 2 == 0: 
        tn = num //2
    else: 
        tn = (num*3)+1
    #print(tn)
    num = tn