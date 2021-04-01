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
        #ventana = Toplevel()
        ventana.title("Ventilación | Erick Tocasca")
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
        Frame5 = Frame(ventana, width=100)
        Frame5.grid(row=0, column=2, padx=20, pady=20, sticky=NW)
        Frame6 = Frame(ventana, width=100)
        Frame6.grid(row=1, column=2, padx=20, pady=20, sticky=NW)
        
        # CREACIÓN DE IMAGENES
        imagen = Image.open("../Imagenes/ventilacion.jpg")
        render = ImageTk.PhotoImage(imagen)       
        Label(Frame2, image = render).grid(row=0, column=0)
        
        imagen1 = Image.open("../Imagenes/formula_ventilacion.jpg")
        render1 = ImageTk.PhotoImage(imagen1)       
        Label(Frame3, image = render1).grid(row=0, column=11, columnspan=11, sticky=NE)
        
        
        # CREACIÓN DE LABELS 
        label = Label(Frame1, text="REQUERIMIENTO DE AIRE")
        label.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",20),
                padx = 2,
                pady = 2)
        label.grid(row=0, column=0, sticky=N)
        
        # CREACIÓN DE LABELS PARA INPUTS
        label1 = Label(Frame4, text="Trabajadores/turno")
        label1.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label1.grid(row=0, column=0, sticky=W)
        nt = Entry(Frame4)
        nt.grid(row=0, column=1)
        separador1 = Label(Frame4)
        separador1.grid(row=1)
        
        label10 = Label(Frame4, text="HP efectiva")
        label10.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label10.grid(row=2, column=0, sticky=W)
        HP = Entry(Frame4)
        HP.grid(row=2, column=1)
        separador10 = Label(Frame4)
        separador10.grid(row=3)
        
        label2 = Label(Frame4, text="Disponibilidad \nMecanica %")
        label2.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label2.grid(row=4, column=0, sticky=W)
        Dm = Entry(Frame4)
        Dm.grid(row=4, column=1)
        separador2 = Label(Frame4)
        separador2.grid(row=5)
        
        label3 = Label(Frame4, text="Utilización %")
        label3.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label3.grid(row=6, column=0, sticky=W)
        Fu = Entry(Frame4)
        Fu.grid(row=6, column=1)
        separador3 = Label(Frame4)
        separador3.grid(row=7)
        
        label4 = Label(Frame4, text="Consumo Madera %")
        label4.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label4.grid(row=8, column=0, sticky=W)
        fp = Entry(Frame4)
        fp.grid(row=8, column=1)
        separador4 = Label(Frame4)
        separador4.grid(row=9)
        
        label5 = Label(Frame4, text="TMH/guardia")
        label5.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label5.grid(row=10, column=0, sticky=W)
        t = Entry(Frame4)
        t.grid(row=10, column=1)
        separador5 = Label(Frame4)
        separador5.grid(row=11)
        
        label6 = Label(Frame4, text="Temperatura seca °c")
        label6.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label6.grid(row=12, column=0, sticky=W)
        ts = Entry(Frame4)
        ts.grid(row=12, column=1)
        separador6 = Label(Frame4)
        separador6.grid(row=13)
        
        label7 = Label(Frame4, text="Area Labor")
        label7.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 5,
                pady = 2)
        label7.grid(row=14, column=0, sticky=W)
        A = Entry(Frame4)
        A.grid(row=14, column=1)
        separador1 = Label(Frame4)
        separador1.grid(row=15)
        
        label8 = Label(Frame4, text="# niveles >23°c")
        label8.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label8.grid(row=16, column=0, sticky=W)
        n = Entry(Frame4)
        n.grid(row=16, column=1)
        separador8 = Label(Frame4)
        separador8.grid(row=17)
        
        label9 = Label(Frame4, text="Altura Geografica")
        label9.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label9.grid(row=18, column=0, sticky=W)
        alt = Entry(Frame4)
        alt.grid(row=18, column=1)
        separador9 = Label(Frame4)
        separador9.grid(row=19)
        
        
        # CREACIÓN DE LABELS PARA OUPUTS
        
        
        label23 = Label(Frame6, text="Requerimiento de \naire: ")
        label23.config(fg = "black",
                bg = "cyan",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label23.grid(row=6, column=0, sticky=W)
        separador23 = Label(Frame6)
        separador23.grid(row=7)
        
        
        
        # COMANDO CALCULAR
        def calcular():
            
            # Caudal Minimo por Persona
            if 0 < float(alt.get()) < 1500:
                f = 3
            elif 1500 <= float(alt.get()) < 3000:
                f = 4
            elif 3000 <= float(alt.get()) < 4000:
                f = 5
            else:
                f = 6
            
            # Factor de producción        
            if 0 < float(fp.get()) < 20:
                u = 0
            elif 20 <= float(fp.get()) <= 40:
                u = 0.6
            elif 41 <= float(fp.get()) < 70:
                u = 1
            else:
                u = 1.25
            
            # Velocidad Mínima    
            if 0 < float(ts.get()) < 24:
                Vm = 0
            elif 24 <= float(ts.get()) <= 29:
                Vm = 30
                
            QTr = f*float(nt.get())
            QEq = 3 * float(HP.get()) * float(Dm.get()) * float(Fu.get()) / 10000
            QMa = u * float(t.get())
            QTe = Vm * float(A.get()) * float(n.get())
            QT1 = QTr * QMa * QTe + QEq
            QFu = 15 / 100 * QT1
            QTo = QT1 + QFu
            
            
            re4 = Label(Frame6, text=QTo)
            re4.grid(row=6, column=1)
            un4 = Label(Frame6, text="CFM")
            un4.grid(row=6, column=2)
            
        
        # BOTON
        boton =Button(Frame5, text="CALCULAR", command=calcular)
        boton.config(
            bg = "OrangeRed2",
            padx = 30,
            pady = 30
            )
        boton.grid(row=0, column=0)
        
        mi_menu = Menu(ventana)
        ventana.config(menu=mi_menu,
                       bg = "aquamarine")
        
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















