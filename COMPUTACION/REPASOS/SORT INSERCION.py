from random import randint

tamaño = int(input("Ingrese el tamaño:"))

vector = [0] * tamaño 
for i in range(1, len(vector)): 
    vector[i] = randint(1,10)
    j = i 
    while j > 0 and vector[j] < vector[j-1]: 
        vector[j], vector[j-1] = vector[j-1], vector[j]
        j -= 1
        
print(vector)