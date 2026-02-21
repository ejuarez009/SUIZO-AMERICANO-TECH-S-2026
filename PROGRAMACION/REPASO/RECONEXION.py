#Librerías
import os.path #Librería para manejar rutas de archivos / INVESTIGAR 
#from tkinter import *; from tkinter import filedialog as fd

ruta = "C:\\Users\\eajua\\OneDrive\\Documentos\\SUIZO AMERICANO (TECH'S) 2026\\PROGRAMACION\\INFORME 1-1\\C52026.txt" # SE INGRESA LA RUTA ABSOLUTA O LA RUTA EN LA CUAL SE VA A MANEJAR EL ARCHIVO

conunter = 0
with open(ruta, 'r') as archivo: #STREAM - INVESTIGAR
    for linea in archivo.readlines(): 
        for char in linea: 
            if char == "\n" or char == " ": 
                continue
            else: 
                conunter += 1
    
    print(conunter)
            