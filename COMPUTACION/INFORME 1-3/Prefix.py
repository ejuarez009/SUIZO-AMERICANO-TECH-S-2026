from tkinter import Entry, Label, Button, messagebox as mb, Tk

class Prefix(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("300x200")
        self.config(bg="lightgreen")
        self.title("PREFIX - Elmer Juarez C5A")
        
        Label(text="Ingrese la expresion Prefix", bg="lightgreen").pack()
        self.entry_exp = Entry(self)
        self.entry_exp.pack()
        Button(text="Resolver expresion", command=self.resolver, bg="pink").pack()
        self.label_result = Label(text="", bg="lightgreen")
        self.label_result.pack()
        
        
    
    def resolver(self): 
        try: 
            expresion = self.entry_exp.get().strip()
        except TypeError: 
            mb.showwarning("Error", "Ingrese una expresion válida")
        self.pos = -1
        resultado = self.prefix(expresion)
        self.label_result.config(text=f"La expresion es: {resultado}", bg="lightgreen", font=("arial", 10, "bold"))
        
    
    def prefix(self,expresion:str):
        self.pos += 1
        caracter=expresion[self.pos]
        if caracter == "V": 
            return "Verdadero"
        if caracter == "F": 
            return "Falso"
        else: 
            if caracter == "&": 
                prev = self.prefix(expresion)
                post = self.prefix(expresion)
                if prev == "V" and post == "V": 
                    return "Verdadero"
                else: 
                    return "Falso"

            if caracter == "|": 
                prev = self.prefix(expresion)
                post = self.prefix(expresion)
                if prev == "V" and post == "F": 
                    return "Falso"
                else: 
                    return "Verdadero"
                
            if caracter == "!": 
                post = self.prefix(expresion)
                if post == "V": 
                    return "Falso"
                else: 
                    return "Verdadero"
    
Prefix().mainloop()