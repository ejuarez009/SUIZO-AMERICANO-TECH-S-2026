from tkinter import*; import pickle; from tkinter import messagebox as mm
from tkinter import filedialog as f;import os; from tkinter import ttk;from datetime import datetime
from tkinter import simpledialog as sd
class app(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Repaso Binarios")
        Button(text="Crear/Abrir",font="Arial 16 bold",command=self.crear).place(x=10,y=10)
        Button(text="Grabar",font="Arial 16 bold",command=self.grabar).place(x=10,y=60)
        Button(text="Leer",font="Arial 16 bold",command=self.leer).place(x=10,y=110)

        self.correlativo=Label(text="",font="Arial 16 bold");self.correlativo.place(x=200,y=10)
        lista=["Nombre","Genero","Fecha","Duracion","Interprete","Frecuencia"]
        for i in range(len(lista)):
            Label(text=lista[i],font="Arial 16 bold").place(x=180,y=i*30+50)
        self.cajanombre=Entry();self.cajanombre.place(x=300,y=60)
        self.cajagenero=Entry();self.cajagenero.place(x=300,y=90)
        self.cajafecha=Entry();self.cajafecha.place(x=300,y=120)
        self.cajaduracion=Entry();self.cajaduracion.place(x=300,y=150)
        self.cajainterprete=Entry();self.cajainterprete.place(x=300,y=180)
        self.cajafrecuencia=Entry();self.cajafrecuencia.place(x=300,y=210)
    def crear(self):
        n=mm.askyesno("","Desea utilizar un archivo existente")
        if n:
            self.ruta=f.askopenfilename(filetypes=[("Archivos Binarios","*.bin")],defaultextension=".bin")
            self.correlativo['text']=str(self.correlativofun()+1)
        else:
            self.ruta=f.asksaveasfilename(filetypes=[("Archivos Binarios","*.bin")],defaultextension=".bin")
            self.correlativo['text']=str(self.correlativofun()+1)
            
    def validarfecha(self,f):
        try:
            datetime.strptime(f,"%d/%m/%Y")
            return True
        except:
            return False
        
    def validarduracion(self,f):
        try:
            datetime.strptime(f,"%M:%S")
            return True
        except:
            return False
        
    def grabar(self):
        nombre=self.cajanombre.get()
        genero=self.cajagenero.get()
        fecha=str(self.cajafecha.get())
        duracion=self.cajaduracion.get()
        interprete=self.cajainterprete.get()
        frecuencia=int(self.cajafrecuencia.get())
        tiposgenero=["rock","pop","reggaeton","electronica","instrumental"]
        if self.validarduracion(duracion) and self.validarfecha(fecha) and (genero in tiposgenero) and (frecuencia>0 and frecuencia<26):
            playlist=""
            calificacion=frecuencia//5 +1
            match genero:
                case "rock":
                    playlist="exitos de rock"
                case "pop":
                    playlist="exitos de pop"
                case "reggaeton":
                    playlist="exitos de reggaeton"
                case "electronica":
                    playlist="exitos de electronica"
                case "instrumental":
                    playlist="exitos de instrumental"
            
            datos=[nombre,genero,playlist,fecha,duracion,interprete,str(frecuencia),str(calificacion)]
            with open(self.ruta,'ab') as archivo:
                pickle.dump(datos,archivo)
            self.cajanombre.delete(0,END);self.cajagenero.delete(0,END);self.cajafecha.delete(0,END);self.cajaduracion.delete(0,END);self.cajainterprete.delete(0,END);self.cajafrecuencia.delete(0,END)
            self.actualizar()
        else:
            mm.showerror("","Datos Invalidos")
            
    def actualizar(self):
        self.tree.delete(*self.tree.get_children())
        with open(self.ruta,'rb') as archivo:
            maximo=os.path.getsize(self.ruta)
            pos=0
            linea=1
            while pos<maximo:
                datos=pickle.load(archivo)
                self.tree.insert("",END,text=str(linea),values=(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7]))
                pos=archivo.tell()
                linea+=1

    def leer(self):
        self.tree=ttk.Treeview(columns=("c1","c2","c3","c4","c5","c6","c7","c8"))
        self.tree.place(x=10,y=300)
        Button(text="Eliminar",font="Arial 16 bold",command=self.eliminar).place(x=10,y=250)
        Button(text="Actualizar",font="Arial 16 bold",command=self.actualizar).place(x=150,y=250)
        Button(text="Modificar",font="Arial 16 bold",command=self.modificar).place(x=300,y=250)
        Button(text="Buscar",font="Arial 16 bold",command=self.buscar).place(x=450,y=250)
        self.tree.heading("#0",text="Correlativo")     
        self.tree.heading("c1",text="Nombre")
        self.tree.heading("c2",text="Genero")
        self.tree.heading("c3",text="Playlist")
        self.tree.heading("c4",text="Fecha")
        self.tree.heading("c5",text="Duracion")
        self.tree.heading("c6",text="Interprete")
        self.tree.heading("c7",text="Frecuencia")
        self.tree.heading("c8",text="Calificacion")
        self.tree.column("#0",width=80)
        self.tree.column("c1",width=80)
        self.tree.column("c2",width=80)
        self.tree.column("c3",width=80)
        self.tree.column("c4",width=80)
        self.tree.column("c5",width=80)
        self.tree.column("c6",width=80)
        self.tree.column("c7",width=80)
        self.tree.column("c8",width=80)
        self.actualizar()
        
    def eliminar(self):
        if self.tree.selection():
            id=self.tree.selection()[0]
            self.tree.delete(id)
            with open(self.ruta,'wb') as archivo:
                for fila in self.tree.get_children():
                    x=self.tree.item(fila)
                    lst=[*x.values()]
                    pickle.dump(lst[2],archivo)
        self.actualizar()
    def modificar(self):
        if self.tree.selection():
            id=self.tree.selection()[0]
            self2=Toplevel(self)
            self2.geometry("600x300")
            lista=["Nombre","Genero","Fecha","Interprete","Frecuencia"]
            for i in range(len(lista)):
                Label(self2,text=lista[i],font="Arial 16 bold").place(x=10,y=i*30+10)
            nuevonombre=Entry(self2);nuevonombre.place(x=150,y=10)
            nuevogenero=Entry(self2);nuevogenero.place(x=150,y=40)
            nuevofecha=Entry(self2);nuevofecha.place(x=150,y=70)
            nuevointerprete=Entry(self2);nuevointerprete.place(x=150,y=100)
            nuevofrecuencia=Entry(self2);nuevofrecuencia.place(x=150,y=130)
            valores=self.tree.item(id)['values']
            playlist=valores[2]
            duracion=valores[4]
            calificacion=valores[7]
            def renovar():
                datos=[nuevonombre.get(),nuevogenero.get(),playlist,nuevofecha.get(),duracion,nuevointerprete.get(),nuevofrecuencia.get(),calificacion]
                id=self.tree.selection()[0]
                self.tree.item(id,values=(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7]))
                with open(self.ruta,'wb') as archivo:
                    for fila in self.tree.get_children():
                        x=self.tree.item(fila)
                        lst=[*x.values()]
                        pickle.dump(lst[2],archivo)

            Button(self2,text="Update",font="Arial 12 bold",command=renovar).place(x=10,y=250)

    def buscar(self):
        self3=Toplevel(self)
        self3.geometry("600x600")
        lista=["Nombre","Genero","Playlist","Fecha","Duracion","Interprete","Frecuencia","Calificacion"]
        for i in range(len(lista)):
            Label(self3,text=lista[i],font="Arial 16 bold").place(x=10,y=i*30+10)
        cajanombre=Entry(self3);cajanombre.place(x=150,y=10)
        cajagenero=Entry(self3);cajagenero.place(x=150,y=40)
        cajaplaylist=Entry(self3);cajaplaylist.place(x=150,y=70)
        cajafecha=Entry(self3);cajafecha.place(x=150,y=100)
        cajaduracion=Entry(self3);cajaduracion.place(x=150,y=130)
        cajainterprete=Entry(self3);cajainterprete.place(x=150,y=160)
        cajafrecuencia=Entry(self3);cajafrecuencia.place(x=150,y=190)
        cajacalificacion=Entry(self3);cajacalificacion.place(x=150,y=220)
        def bs():
            nombrebuscar=cajanombre.get()
            generobuscar=cajagenero.get()
            playlistbuscar=cajaplaylist.get()
            fechabuscar=cajafecha.get()        
            duracionbuscar=cajaduracion.get()
            interpretebuscar=cajainterprete.get()
            frecuenciabuscar=cajafrecuencia.get()
            calificacionbuscar=cajacalificacion.get()
            valoresdisponibles=[nombrebuscar,generobuscar,playlistbuscar,fechabuscar,duracionbuscar,interpretebuscar,frecuenciabuscar,calificacionbuscar]
            valoresutilizables=[]
            for i in valoresdisponibles:
                if i!="":
                    valoresutilizables.append(i)
            seleccion=[]
            for fila in self.tree.get_children():
                valores=self.tree.item(fila)['values']
                c=0
                for i in valoresutilizables:
                    if i in valores:
                        c+=1
                if c==len(valoresutilizables):
                    seleccion.append(fila)
            self.tree.selection_set(seleccion)
        Button(self3,text="Buscar",font="Arial 14 bold",command=bs).place(x=10,y=260)
            
            
    def correlativofun(self):
        with open(self.ruta,'rb') as archivo:
            pos=0
            maximo=os.path.getsize(self.ruta)
            c=0
            while pos<maximo:
                pickle.load(archivo)
                pos=archivo.tell()
                c+=1
            return c

app().mainloop()