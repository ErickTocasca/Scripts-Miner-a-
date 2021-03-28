from tkinter import *
import pathlib
import os.path
from tkinter import messagebox
from PIL import Image, ImageTk

ventana = Tk()

ventana.title("Mining App | Erick Tocasca")
ventana.geometry("1065x604")
ventana.resizable(0,0)
ventana.iconbitmap("../Imagenes/lobo.ico")

imagen = Image.open("../Imagenes/BIENVENIDO.jpg")
render = ImageTk.PhotoImage(imagen)
        
Label(ventana, image = render).grid(row=0, column=0)

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

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Buscar")
mi_menu.add_command(label="Ayuda")


ventana.mainloop()