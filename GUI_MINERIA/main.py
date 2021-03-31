from tkinter import *
import pathlib
import os.path
from tkinter import messagebox
from PIL import Image, ImageTk
from programas import Programas


ventana = Tk()

ventana.title("Mining App | Erick Tocasca")
ventana.geometry("1065x620")
ventana.resizable(0,0)
ventana.iconbitmap("../Imagenes/lobo.ico")

imagen = Image.open("../Imagenes/BIENVENIDO.jpg")
render = ImageTk.PhotoImage(imagen)
        
Label(ventana, image = render).grid(row=0, column=0)

#Comandos para los menus
seguridad = Programas().seguridad
curva = Programas().Cur_Ton_Ley
scoop = Programas().scoop

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo Archivo")
archivo.add_separator()
archivo.add_command(label="Abrir")
archivo.add_command(label="Abrir el ultimo cerrado")
archivo.add_command(label="Abierto recientemente")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.destroy)

programas = Menu(mi_menu, tearoff=0)
programas.add_command(label="Seguridad", command=seguridad)
programas.add_separator()
programas.add_command(label="Curva-Ton-Ley", command=curva)
programas.add_command(label="ScoopTram", command=scoop)
programas.add_command(label="Sostenimiento")
programas.add_separator()
programas.add_command(label="Ventilación")
programas.add_command(label="lerch-grossman")
programas.add_command(label="Abierto recientemente")
programas.add_separator()
programas.add_command(label="Salir", command=ventana.destroy)


mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_cascade(label="Programas", menu=programas)
mi_menu.add_command(label="Buscar")
mi_menu.add_command(label="Ayuda")


ventana.mainloop()