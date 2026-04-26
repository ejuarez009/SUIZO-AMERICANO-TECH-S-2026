import tkinter 

class app(tkinter.Tk): 
    def __init__(self): 
        super().__init__()
        self.geometry("300x300")
        
        tkinter.Label(text="Ingrese el número 1:").pack()
        self.entry_num1 = tkinter.Entry(width=10)
        self.entry_num1.pack()
        tkinter.Label(text="Ingrese el número 2:").pack()
        self.entry_num2 = tkinter.Entry(width=10)
        self.entry_num2.pack()
        
        tkinter.Button(text="Numeros Amigos", command=self.mandar).pack()
        
        self.label_reult = tkinter.Label(text="")
        self.label_reult.pack()
        
    
    def mandar(self): 
        try: 
            numero1 = int(self.entry_num1.get())
            numero2 = int(self.entry_num2.get())
        except ValueError: 
            return 
        num_amigo = self.numeros_amigos(numero1, numero2)
        if num_amigo == True: 
            self.label_reult['text'] = f"Los numeros: {numero1, numero2} si son números amigos"
        else: 
            self.label_reult['text'] = "No son numeros amigos"
    
    def numeros_amigos(self, num1, num2): 
        acu1 = 0
        acu2 = 0 
        for divi in range(1, num1): 
            if num1 % divi == 0: 
                acu1 += divi
        
        for divi in range(1,num2): 
            if num2 % divi == 0: 
                acu2 += divi
                
        return (num1 == acu2) \
            and (num2 == acu1) #Los parentesis garantizan el orden de la comparacion # \: Continuacion de linea
    
    #def recu_divis(self, num)-> int: 
        #pass
        

app().mainloop()