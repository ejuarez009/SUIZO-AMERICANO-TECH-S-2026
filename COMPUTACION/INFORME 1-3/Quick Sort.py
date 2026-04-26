vector = [7,3,4,3,8,9,1,5]

co = 0

def quicksort(L:list,c): 
    if len(L) < 2: 
        return L
    else: 
        e = L[0]
        L1 = []
        L2 = []
        
        for i in L[1:]:
            c += 1
            if i < e: 
                L1.append(i)
            else: 
                L2.append(i)
        
        return quicksort(L1,c) + [ e ] + quicksort(L2,c)


print(quicksort(vector,co))