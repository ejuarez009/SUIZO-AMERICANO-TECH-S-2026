def grabar(self): 
    root = Toplevel(self)
    root.geometry("300x300")
    root.title()
    
    etiquetas = []
    objetos = {}
    for i, etiqueta in enumerate(etiquetas): 
        Label(root,text=etiqueta).grid(row=1, colomn=0)
        
        entry = Entry(self)
        entry.grid(row=i, column=0)
        
        objetos[etiqueta] = entry 
        
    def guardar(): 
        datos = []
        for tcaja in etiquetas: 
            tcaja = objetos[tcaja].get().strip()
            if tcaja == "": 
                return 
            else: 
                datos.append(tcaja)
        
        
        
        
        
        
        try: 
            with open(self.ruta,'ab') as archivo: 
                pickle.dump(datos_bien, archivo)
            mb.showinfo("Atencion", "Se grabo un registro")
        except AttributeError: 
            return 
        
        
        for entry in objetos.values():
            entry.delete(0,END)
        
        self.consulta()
        
    
    
    def modificar(): 
        dato =
        
        volres = None
        fila_objetivo = None
        bandera = False
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)['text']
            if str(dato) == str(correlativo): 
                bandera = True 
                valores = self.tree.item(fila)['values']
                fila_objetivo = fila
                
        if bandera == False: 
            return 
        
        root = Toplevel(self)
        root.geometry()
        
        etiquetas = []
        objetos = {}
        for i, etiqueta in enumerate(etiquetas): 
            Label(root,text=etiqueta).grid(row=i, colomn=0)
            
            entry = Entry(self)
            entry.grid(row=i, column=1)
            
            objetos[etiqueta] = entry
            
        for i in range(len<etiquetas)): 
            etiq = etiquetas[i]
            caja = objetos[etiq]
            caja.insert(0,valores[i])
        
        def cargar(): 
            datos = []
            for entry in objetos.values(): 
                datos.append(entry)
            
            self.tree.item(fila_objetivo, values=datos)
            try: 
                with open(self.ruta,'wb') as archivo:
                    for fila in self.tree.get_children(): 
                        vals_nuevos = self.tree.item(fila)['values']
                        pickle.dump(vals_nuevos, archivo)
    
    
    def eliminar(): 
        dato = 
        bandera = False
        for fila in self.tree.get_children(): 
            correlativo = self.tree.item(fila)['text']
            if str(dato) == str(correlativo): 
                self.tree.delete(fila)
                bandera = True
        if bandera == False: 
            return 

        with open(self.ruta, 'wb') as archivo: 
            for fila in self.tree.get_children(): 
                valores = self.tree.item(fila)['values']
                pickle.dump(valores, archivo) 
            
            self.consulta()

    def consulta(): 
        try: 
            with open(self.ruta, 'rb') as archivo: 
                while True: 
                    try: 
                        registro = pickle.load(archivo)
                        self.tree.insert("", END, values=registro)
                    except EOFError: 
                        break
        except AttributeError: 
            return
            
            