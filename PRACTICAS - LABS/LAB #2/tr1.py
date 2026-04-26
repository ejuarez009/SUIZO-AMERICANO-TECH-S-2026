#Ejemplo con treeview
from tkinter import *;from tkinter import ttk, filedialog as f, simpledialog, messagebox as ms
import pickle
import os.path

#Funciones de carga
def cargar_tree():
    rt = f.askopenfilename()
    rtn['text']=f"{rt}"
    maxi = os.path.getsize(rt)
    pos=0
    with open(rt,'rb') as ar:
        while pos<maxi:
            fila = pickle.load(ar)
            tr.insert('',END,values=fila)
            pos=ar.tell()
    

def recorrido():
    #for pos in tr.get_children():
    #    print (pos)
    #tr.selection_set('I002')
    #tr.delete('I001')
    if tr.selection():
       print(tr.selection()[0])
    else:
       print("Debe seleccionar un elemento")
       
def guarda():
    gd = Toplevel(v)
    gd.geometry("200x200")
    #Datos
    n = Entry(gd,width=50)
    n.pack()
    car = Entry(gd,width=50)
    car.pack()
    

    def g():
        nn = n.get()
        cc = car.get()
        lista = [nn,cc]
        rt = rtn['text']
        with open (rt,'ab') as ar:
            pickle.dump(lista,ar)

    def crear():
        rt = f.asksaveasfilename()
        rtn['text']=f"{rt}"
    
    bt=Button(gd,text="Crear ruta nueva",command=crear)
    bt.pack(side='left')
    bt=Button(gd,text="Guardar",command=g)
    bt.pack(side='left')

    gd.mainloop()

def ci():
    dato=simpledialog.askstring("Input", "Ingrese el dato a buscar")
    seleccion = []
    encontrado=False
    for posicion in tr.get_children():
        if dato in str(tr.item(posicion)['values']):
            seleccion.append(posicion)
            encontrado=True
    if encontrado:
        tr.selection_set(seleccion)
    else:
        print("El dato no fue localizado")    

def editar():

    if (tr.selection()):
        vedit = Toplevel(v)
        vedit.geometry("200x300")
    
        tnombre = Entry(vedit,width=25)
        tnombre.pack()
        tcarr = Entry(vedit,width=25)
        tcarr.pack()
       
    
        id = tr.selection()[0]
        lista = tr.item(id)['values']  
        tnombre.insert('insert',lista[0]) 
        tcarr.insert('insert',lista[1])
       
        def actualizar():
            n = tnombre.get()
            c = tcarr.get()
         
            id = tr.selection()[0]
            tr.item(id,values=(n,c))

            #Actualizar archivo
            ar = rtn['text']
            f = open(ar,'wb')
            for fila in tr.get_children():
                x = tr.item(fila)
                lst = [*x.values()]
                lista = lst[2]
                #lista.insert(0,lst[0]) #inserta el dato que se encuentra en la posicion [0] de lst al inicio de la lista
                pickle.dump(lista,f)

        #Boton de actualizar datos
        bact = Button(vedit,text="Actualizar datos",command=actualizar)
        bact.pack()

        vedit.mainloop()
    else:
        ms.showinfo("Advertencia","Debe selecciona un registro para modificar")




#objetos
v = Tk()
v.geometry("610x280")
#Creacion del Treeview
tr = ttk.Treeview(v,height=10)
tr['columns']=("c1","c2")
#Creacion de las columnos y encabezados
#tr.column("#0",width=50,minwidth=15)
tr.heading("#0",text="C", anchor="center")
tr.heading("c1",text="Nombre")
tr.heading("c2",text="Carrera")
tr.pack()
rtn = Label(v,text="")
rtn.pack()

#Botones para funcionalidad de ejemplos
b1 = Button(v,text="Cargar datos al tree",command=cargar_tree)
b1.pack(side="left")
b2 = Button(v,text="Cargar datos y generar Entrys",command=recorrido)
b2.pack(side="left")
b3 = Button(v,text="Guardar datos de los Entrys",command=guarda)
b3.pack(side="left")
b4 = Button(v,text="Realiza la consulta individual",command=ci)
b4.pack(side="left")
b5 = Button(v,text="Modifica",command=editar)
b5.pack(side="left")


v.mainloop()
