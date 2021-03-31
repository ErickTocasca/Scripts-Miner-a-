from tkinter import *
from tkinter import ttk
import pathlib
import os.path
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#from matplotlib.pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import filedialog

class Seguridad():
    def Ventana(self):
        ventana = Tk()
        ventana.title("Seguridad | Erick Tocasca")
        ventana.iconbitmap("../Imagenes/lobo.ico")
        
        # CREACIÓN DE FRAMES
        Frame1 = Frame(ventana, width=100)
        Frame1.grid(row=0, column=0, padx=20, pady=20, sticky=NW)
        Frame2 = Frame(ventana, width=100)
        Frame2.grid(row=0, column=1, padx=20, pady=20, sticky=NW)
        Frame3 = Frame(ventana, width=100)
        Frame3.grid(row=1, column=0, padx=20, pady=20, sticky=NE)
        Frame4 = Frame(ventana, width=100)
        Frame4.grid(row=1, column=1, padx=20, pady=20, sticky=NW)
        
        # CREACIÓN DE IMAGENES
        imagen = Image.open("../Imagenes/minero.jpg")
        render = ImageTk.PhotoImage(imagen)       
        Label(Frame2, image = render).grid(row=0, column=0)
        
        imagen1 = Image.open("../Imagenes/epp.jpg")
        render1 = ImageTk.PhotoImage(imagen1)       
        Label(Frame3, image = render1).grid(row=0, column=11, columnspan=11, sticky=NE)
        
        
        # CREACIÓN DE LABELS 
        label = Label(Frame1, text="Seguridad y Salud\nen Minería")
        label.config(fg = "black",
                bg = "gold",
                font = ("Black Arial",20),
                padx = 10,
                pady = 8)
        label.grid(row=0, column=0, sticky=N)
        
        # CREACIÓN DE BOTONES
        label1 = Button(Frame4, text="Base Datos")
        label1.config(fg = "black",
                bg = "gold",
                font = ("Black Arial",10),
                padx = 22,
                pady = 2)
        label1.grid(row=0, column=0, sticky=W)
        separador1 = Label(Frame4)
        separador1.config(bg="orange", padx=59)
        separador1.grid(row=1)
        
        label2 = Button(Frame4, text="Agentes Fisico")
        label2.config(fg = "black",
                bg = "gold",
                font = ("Black Arial",10),
                padx = 12,
                pady = 2)
        label2.grid(row=2, column=0, sticky=W)
        separador2 = Label(Frame4)
        separador2.config(bg="orange", padx=59)
        separador2.grid(row=3)
        
        label3 = Button(Frame4, text="Agente Químico")
        label3.config(fg = "black",
                bg = "gold",
                font = ("Black Arial",10),
                padx = 9,
                pady = 2)
        label3.grid(row=4, column=0, sticky=W)
        separador3 = Label(Frame4)
        separador3.config(bg="orange", padx=59)
        separador3.grid(row=5)
        
        label4 = Button(Frame4, text="Ruido Ocupacional")
        label4.config(fg = "black",
                bg = "gold",
                font = ("Black Arial",10),
                #padx = 1,
                pady = 2)
        label4.grid(row=6, column=0, sticky=W)
        separador4 = Label(Frame4)
        separador4.config(bg="orange", padx=59)
        separador4.grid(row=7)
        

        # MENU
        
        
        mi_menu = Menu(ventana)
        ventana.config(menu=mi_menu,
                       bg = "orange")
        
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



vent = Seguridad().Ventana()















