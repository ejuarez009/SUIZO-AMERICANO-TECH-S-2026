import time
import random

def insertion(): 
    inicio = time.time()
    for i in range(1, len(vector)): 
        j = i -1
        while j >= 0 and vector[j] > vector[j+1]:
            vector[j], vector[j+1] = vector[j+1], vector[j]
            j -= 1
    fin = time.time()
    tiempo_total = fin - inicio
    return vector, f"{tiempo_total:.10f} segundos"

def own_sort():
    inicio = time.time()
    for _ in range(len(vector)): 
        for i in range(len(vector)): 
            element = vector[i]
            if element > vector[i]: 
                vector[i], vector[i-1] = vector[i-1], vector[i]
            else: 
                break
    
    fin = time.time()
    tiempo_total = fin - inicio
    return vector, f"{tiempo_total:.10f} segundos"

def burbuja(): 
    inicio = time.time()
    for i in range(len(vector) -1): 
        for j in range(0, len(vector)-i-1): 
            if vector[j] > vector[j+1]: 
                vector[j], vector[j+1] = vector[j+1], vector[j]
    fin = time.time()
    temp_final = fin - inicio
    return vector, f"{temp_final:.10f} segundos"


vector = [random.randint(1,50) for _ in range(20)]
print("Vector original:", vector)

print("Vector ordenado por insercion:", insertion())
print("Vector ordenado por own_sort:", own_sort())
print("Vector ordenado por burbuja:", burbuja())