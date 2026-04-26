def log(b, expo): 
    if expo == 0:
        print(b, expo) 
        return 1
    
    elif expo % 2 == 0: 
        print(b, expo)
        return log(b * b, expo // 2) 
    else: 
        print(b, expo)
        return b * log(b * b, (expo - 1) // 2)

print(log(2, 10))

