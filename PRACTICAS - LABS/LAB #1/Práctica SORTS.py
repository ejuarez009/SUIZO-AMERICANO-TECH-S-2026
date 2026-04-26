vector = [5, 2, 9, 1, 5, 6, 9, 8, 2, 1]


def bubble_sort(): 
    for i in range(len(vector)): 
        for j in range(len(vector)-i-1):
            if vector[j] > vector[j+1]: 
                vector[j], vector[j+1] = vector[j+1], vector[j]
    print(vector)

def insertion_sort(): 
    for i in range(len(vector)): 
        j = i
        while j > 0 and vector[j-1] > vector[j]: 
            vector[j], vector[j-1] = vector[j-1], vector[j]
        j -= 1
    print(vector)

def selection_sort():
    ultimo = len(vector) - 1
    while ultimo >0:
        pos_mayor = 0
        for j in range(ultimo + 1): 
            if vector[j] > vector[pos_mayor]:
                pos_mayor = j 
        vector[ultimo], vector[pos_mayor] = vector[pos_mayor], vector[ultimo]
        ultimo -= 1
    print(vector)

def conteo_sort():
    for i in range(len(vector)): 
        counter = 0 
        for j in range(len(vector)): 
            if vector[i] > vector[j] or (vector[i] == vector[j] and j>i): 
                counter += 1
        vector[counter] = vector[i]
    print(vector)

bubble_sort()
insertion_sort()
selection_sort()
conteo_sort()