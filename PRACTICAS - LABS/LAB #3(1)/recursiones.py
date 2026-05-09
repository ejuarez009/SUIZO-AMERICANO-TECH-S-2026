num = 1

def contardigitos(num): 
        if num < 10: 
            return 1
        else: 
            sinulti = num // 10
            return 1 + contardigitos(sinulti)

print(contardigitos(num))