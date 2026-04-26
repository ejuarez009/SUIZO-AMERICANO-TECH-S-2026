#repaso de empresa progra
'''
La empresa MEGASYSTEMS S.A, necesita registrar los datos personales de los empleados que laboran en los diferentes
departamentos, para ello se le ha contratado para desarrollar un programa que permita almacenar en un archivo
binario exclusivamente para todos esos datos. Los datos previos a ser almacenados deben cumplir con ciertos
requerimientos para pertenecer al grupo selecto de empleados registrados ante el Ministerio de Trabajo. Los datos son
los siguientes:
1. Los únicos códigos que se pueden almacenar son:
a. MEGA-CB (contabilidad)
b. MEGA-INFO (informática)
c. MEGA-VN (ventas)
d. MEGA-OP (operativos)
2. Los campos para la lista y el archivo son:
a. Código
b. Nombre y apellidos
c. Puesto o Cargo
d. Área (debe corresponder con el código asignado)
e. Sueldo
f. Fecha de contratación
g. Tipo de contrato (INDEFINIDO O TEMPORAL) no se acepta ningún otro tipo de contrato
-El programa debe ser capaz de validar todos los criterios y guardarlos en un archivo binario
-El programa muestra el acceso a dos opciones para su manipulación:
a) Ingreso de datos b) Consulta general de empleados  c)Modificación o eliminación
-Los datos almacenados se deben mostrar en algún objeto de despliegue y no en la consola
-La consulta general es un despliegue en pantalla de todos los datos ingresados al archivo binario
-El programa es capaz de leer archivos que ya existen
'''
'''
interfaz: 10 minutos
'''
from tkinter import filedialog as file, messagebox as ms, ttk, Tk, END, Toplevel as tp
import pickle
class empresa (Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="skyblue")
        #-------------------Interfaz
        self.stack=["dato"]*7
        self.sp=0
        self.correlativos=["código", "nombre completo", "puesto o cargo", "área", "sueldo", "fecha de contratación", "tipo de contrato"]
        self.eti_corre=ttk.Label(self, text=f"Ingresar {self.correlativos[self.sp]}", font=("arial", 12, "bold"), background="skyblue3"); self.eti_corre.pack() #indica que dato ingresar
        self.dato=ttk.Entry(self); self.dato.pack() #permite ingresar dato
        self.eti_stack=ttk.Label(self, text=f"{"  - ".join(self.stack)}", font=("arial", 12, "bold"), background="skyblue3"); self.eti_stack.pack() #muestra el stack
        #treeview
        self.tree=ttk.Treeview(self, show="headings", columns=("c", "nc", "p", "a", "s", "f", "tc"))
        self.tree.heading("c", text="código"); self.tree.column("c", width=80, anchor="center")
        self.tree.heading("nc", text="nombre completo"); self.tree.column("nc", width=110, anchor="w")
        self.tree.heading("p", text="puesto"); self.tree.column("p", width=80, anchor="center")
        self.tree.heading("a", text="área"); self.tree.column("a", width=80, anchor="center")
        self.tree.heading("s", text="sueldo"); self.tree.column("s", width=80, anchor="center")
        self.tree.heading("f", text="fecha de contratación"); self.tree.column("f", width=120, anchor="w")
        self.tree.heading("tc", text="tipo de contrato"); self.tree.column("tc", width=110, anchor="w")
        self.tree.pack()
        #botones
        ttk.Button(self, text="Ingresar dato", command=lambda: self.pushito(self.dato.get())).pack(side="left"); self.bind("<Return>", lambda events:self.pushito(self.dato.get()))
        #lambda es una función sin nombre, la utiliza para invocar a la función y pasarle como parámetro el valor del entry
        ttk.Button(self, text="Consulta específica", command=self.consulta_especifica_inter).pack(side="right")
        ttk.Button(self, text="Consulta general", command=self.consulta_general).pack(side="right")
        ttk.Button(self, text="Eliminar o  modificar", command=self.eliminar_modi).pack(side="right")
        ttk.Button(self, text="Vaciar", command=self.limpiar).pack(side="right")


        res=ms.askyesno("¡BIENVENIDO!", "¿Tiene algún archivo para trabajar?")
        if res:
            self.rt=file.askopenfilename()
        else:
            e=file.asksaveasfilename()
            with open (e, "wb") as bin:
                pass
            self.rt=file.askopenfilename()


    #---------------------------------------------------------
    def pushito (self, e:str):
        if self.sp in range (0, 7):
            if self.sp==3: #como el área s emodifica abajo, aquí solo se mueve el puntero
                self.sp+=1
                self.eti_stack['text']=f"{self.stack}"
                self.eti_corre['text']=f"Ingrese: {self.correlativos[self.sp]}" #modifica la etiqueta
                return 

            if self.sp==0:
                bul=self.validacion(e) #invoca la validación de código
                if bul:
                    pass
                else:
                    ms.showerror("ERROR", "Código inválido")
                    return
            self.stack[self.sp]=e.upper() #maneja todo con mayúsculas
            self.sp+=1

            if self.sp==7:
                self.tree.insert("", END, values=(self.stack)) #guarda los datos
                with open (self.rt, "ab") as bin:
                    pickle.dump(self.stack, bin)
                self.stack=["dato"]*7
                self.sp=0

            try: 
                self.eti_stack['text']=f"{self.stack}"
                self.eti_corre['text']=f"Ingrese: {self.correlativos[self.sp]}" #modifica la etiqueta
            except:
                pass
        else:
            ms.showerror("error", "pila llena")

    #-----------------------------------------
    def validacion(self, cod:str):
        cods=["MEGA-CB","MEGA-INFO","MEGA-VN","MEGA-OP"]
        if cod in cods:
            if cod==cods[0]:
                self.stack[3]="CONTABILIDAD"
            if cod==cods[1]:
                self.stack[3]="INFORMÁTICA"
            if cod==cods[2]:
                print(cods[2])
                self.stack[3]="VENTAS"
            if cod==cods[3]:
                print(cods[3])
                self.stack[3]="OPERATIVOS"
            return True
        else:
            return False
        

        
    #---------------------------
    def consulta_general(self):
        #genera otra ventana y un treeview para la consulta general
        self.tp1=tp(self)
        tree=ttk.Treeview(self.tp1, show="headings", columns=("c", "nc", "p", "a", "s", "f", "tc"))
        tree.heading("c", text="código"); tree.column("c", width=80, anchor="center")
        tree.heading("nc", text="nombre completo"); tree.column("nc", width=110, anchor="w")
        tree.heading("p", text="puesto"); tree.column("p", width=80, anchor="center")
        tree.heading("a", text="área"); tree.column("a", width=80, anchor="center")
        tree.heading("s", text="sueldo"); tree.column("s", width=80, anchor="center")
        tree.heading("f", text="fecha de contratación"); tree.column("f", width=120, anchor="w")
        tree.heading("tc", text="tipo de contrato"); tree.column("tc", width=110, anchor="w")
        tree.pack()
        with open (self.rt, "rb") as bin: #abre el archivo
            while True:
                try:
                    a=pickle.load(bin)
                    tree.insert("", END, values=(a))
                except EOFError: #EOFError quiere decir que ya terminó el archivo, pero en lugar de dar error, lo usa para terminar el ciclo
                    break
        ttk.Button(self.tp1,text="Salir", command=lambda:self.tp1.destroy() )

    def consulta_especifica_inter(self):
        self.tp2=tp(self)
        self.tp2.config(bg="skyblue")
        ttk.Label(self.tp2, text=f"¿Qué campo de los trabajadores busca?", font=("arial", 12, "bold"), background="skyblue3").pack()
        dato=ttk.Entry(self.tp2); dato.pack()
        ttk.Button(self.tp2, text="BuscaR", command=lambda: self.busqueda(dato.get())).pack()


    def busqueda(self, dato:str):
        self.tp2.destroy()
        with open (self.rt, "rb") as bin:
            self.limpiar()
            while True:
                try:
                    a=pickle.load(bin) #carga el primer registro
                    if dato in a: #si lo que el usuario ingresó está dentro de la lista, lo inserta en el tree
                        self.tree.insert("",END, values=(a))
                except EOFError:
                    break

    def eliminar_modi (self):
        self.tp3=tp(self)
        self.tp3.config(bg="skyblue")
        tree=ttk.Treeview(self.tp3, show="headings", columns=("c", "nc", "p", "a", "s", "f", "tc"))
        tree.heading("c", text="código"); tree.column("c", width=80, anchor="center")
        tree.heading("nc", text="nombre completo"); tree.column("nc", width=110, anchor="w")
        tree.heading("p", text="puesto"); tree.column("p", width=80, anchor="center")
        tree.heading("a", text="área"); tree.column("a", width=80, anchor="center")
        tree.heading("s", text="sueldo"); tree.column("s", width=80, anchor="center")
        tree.heading("f", text="fecha de contratación"); tree.column("f", width=120, anchor="w")
        tree.heading("tc", text="tipo de contrato"); tree.column("tc", width=110, anchor="w")
        tree.pack()
        with open (self.rt, "rb") as bin:
            while True:
                try:
                    a=pickle.load(bin)
                    tree.insert("", END, values=a)
                except EOFError:
                    break
        ttk.Label(self.tp3, text="Seleccione el registro que desea manipular").pack()
        ttk.Button(self.tp3, text="Eliminar", command=lambda: self.eliminar(list(tree.item(tree.focus(), "values")))).pack()
        ttk.Button(self.tp3, text="Modificar", command=lambda: self.modificar(list(tree.item(tree.focus(), "values")))).pack()
        #tree.item() devuelve el los valores seleccionados, .item devuelve el correlativo que no se usa y "values" indica que son los valores nada más
    def eliminar (self, dato:list):
        self.tp3.destroy()
        with open(self.rt, "rb") as bin:
            matriz=[] #creo una matriz para los datos que no se eliminan
            while True:
                try:
                    a=pickle.load(bin)
                    if a != dato: #si mi dato es  diferente del registro, quiere decir que no se elimina
                        matriz.append(a)
                except EOFError:
                    break
        with open (self.rt, "wb") as bin2: #se elimina todo el contenudi del archivo
            for guardados in matriz:#se recorre la amtriz
                pickle.dump(guardados, bin2) #se guarda cada elemento de la matriz

    def modificar (self, dato:list):
        self.limpiar()
        self.tp3.destroy()
        matriz=[]
        with open (self.rt, "rb") as bin:
            while True:
                try:
                    a=pickle.load(bin)
                    if a !=dato:
                        matriz.append(a)
                except EOFError:
                    break

        with open (self.rt, "wb") as bin2:
            for guard in matriz:
                pickle.dump(guard, bin2)

        i=0
        for j in dato:
            self.stack[i]=j
            i+=1
        self.sp=0
 
        self.eti_stack['text']=f"{self.stack}"
        self.eti_corre['text']=f"Ingrese: {self.correlativos[self.sp]}" #modifica la etiqueta

        
    def limpiar (self):
        for i in self.tree.get_children():
            self.tree.delete(i)
                    


empresa().mainloop()