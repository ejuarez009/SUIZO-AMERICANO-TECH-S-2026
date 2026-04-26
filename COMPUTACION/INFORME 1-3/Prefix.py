def prefix(expresion:str):
    global pos 
    pos += 1
    caracter=expresion[pos]
    if caracter == "V": 
        return "V"
    if caracter == "F": 
        return "F"
    else: 
        if caracter == "&": 
            prev = prefix(expresion)
            post = prefix(expresion)
            if prev == "V" and post == "V": 
                return "V"
            else: 
                return "F"

        if caracter == "|": 
            prev = prefix(expresion)
            post = prefix(expresion)
            if prev == "V" and post == "F": 
                return "F"
            else: 
                return "V"
            
        if caracter == "!": 
            post = prefix(expresion)
            if post == "V": 
                return "F"
            else: 
                return "V"
pos = -1

print(prefix("&!FV"))