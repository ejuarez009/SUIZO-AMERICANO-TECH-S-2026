vector = [5, 2, 9, 1, 5, 6]

def insercion():
    for i in range(1, len(vector)): 
        j = i - 1
        while j >= 0 and vector[j] > vector[j+1]: 
            vector[j], vector[j+1] = vector[j+1], vector[j]
            j -= 1
    return vector

def burbuja(): 
    for i in range(len(vector)-1): 
        for j in range(0, len(vector)-i-1): 
            if vector[j] > vector[j+1]: 
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector 


print(insercion())
print(burbuja())