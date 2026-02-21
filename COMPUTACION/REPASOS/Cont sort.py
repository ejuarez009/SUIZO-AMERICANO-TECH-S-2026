
from random import randint

size_vector = int(input("Ingrese el tamaño del vector: "))

vector = [0] * size_vector
for i in range(size_vector):
    element = randint(1, size_vector)
    vector[i] = element
    if vector[i-1] > vector[i]:
        vector[i] = vector[i-1] + element

print(vector)