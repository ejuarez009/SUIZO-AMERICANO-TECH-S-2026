
from tkinter import*; from tkinter import messagebox as mb 

class app(Tk): 
    def __init__(self): 
        super().__init__()
        
        self.geometry("600x600")
        self.title("Auto: Elmer Juarez")
        
        Label(text="Ingrese la operación lógica").pack()
        self.entry_exp = Entry()
        self.entry_exp.pack()

        self.label_result = Label(text="--expression--", fg="gray")
        self.label_result.pack()
        
        Button(text="Prefix", command=self.call_prefix).pack()
    
    
    def call_prefix(self): 
        try: 
            expresion = str(self.entry_exp.get()).strip().upper()
        except ValueError: 
            mb.showerror("Atencion", "Ingrese una expresion valida")
            return 
        self.pos = -1
        resultado = self.prefix(expresion)
        if resultado == "V": 
            resultado = "Es verdadero"
        else: 
            resultado = "Es falso"
        self.label_result.config(text=f"{resultado}", fg="black")
        
    
    def prefix(self, expresion):
        self.pos +=1        
        char = expresion[self.pos]
        if char == "V":
            return "V"
        if char == "F": 
            return "F"
        else: 
            if char == "&": 
                prev = self.prefix(expresion)
                post = self.prefix(expresion)
                if prev == "V" and post == "V": 
                    return "V"
                else: 
                    return "F"
            
            if char == "|": 
                prev = self.prefix(expresion)
                post = self.prefix(expresion)
                if prev == "F" or post == "F": 
                    return "V"
                else: 
                    return "F"
            
            if char == "!": 
                post = self.prefix(expresion)
                if post == "V": 
                    return "F"
                else: 
                    return "V"    

app().mainloop()