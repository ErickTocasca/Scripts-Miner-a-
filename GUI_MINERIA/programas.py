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
from tkinter import filedialog
from archivo import Archivo


class Programas():
    def seguridad(self):
        ventana = Toplevel()
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
    
    def Cur_Ton_Ley(self):
        ventana = Tk()
        
        ventana.title("Curva Tonelaje Ley | Erick Tocasca")
        #ventana.geometry("600x600")
        #ventana.resizable(0,0)
        ventana.iconbitmap("../Imagenes/lobo.ico")
        
        #imagen = Image.open("../Imagenes/BIENVENIDO.jpg")
        #render = ImageTk.PhotoImage(imagen)       
        #Label(ventana, image = render).grid(row=0, column=0)
        
        mi_menu = Menu(ventana)
        ventana.config(menu=mi_menu,
                       bg = "lightblue")
        
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
        
        archivo1 = Archivo()
        
        label = Label(ventana, text="INICIO")
        label.config(fg = "white",
            bg = "black",
            font = ("Arial",30),
            padx = 200,
            pady = 15)
        label.grid(row=0, column=0, columnspan=15)
        
        label1 = Label(ventana, text="Abrir el archivo")
        label1.grid(row=1, column=2)
        Button(ventana, text="Open", command=archivo1.openFile).grid(row= 1, column=8)
        
        label2 = Label(ventana, text="Procesar el archivo")
        label2.grid(row=2, column=2)
        Button(ventana, text="Process", command=archivo1.curva).grid(row= 2, column=8)
        
        label3 = Label(ventana, text="Crear grafico")
        label3.grid(row=3, column=2)
        Button(ventana, text="Graph", command=archivo1.graph).grid(row= 3, column=8)
        
        
        ventana.mainloop()
    
    def scoop(self):
        ventana = Toplevel()
        ventana.title("Scoop Tram | Erick Tocasca")
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
        imagen = Image.open("../Imagenes/scooptram.jpg")
        render = ImageTk.PhotoImage(imagen)       
        Label(Frame2, image = render).grid(row=0, column=0)
        
        imagen1 = Image.open("../Imagenes/FORMULAS.jpg")
        render1 = ImageTk.PhotoImage(imagen1)       
        Label(Frame3, image = render1).grid(row=0, column=11, columnspan=11, sticky=NE)
        
        
        # CREACIÓN DE LABELS 
        label = Label(Frame1, text="""CALCULOS OPERATIVOS 
        CON SCOOPTRAM""")
        label.config(fg = "white",
                bg = "green",
                font = ("Black Arial",20),
                padx = 50,
                pady = 20)
        label.grid(row=0, column=0, sticky=N)
        
        # CREACIÓN DE LABELS PARA INPUTS
        label1 = Label(Frame4, text="Capacidad de Scoop yardas")
        label1.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label1.grid(row=0, column=0, sticky=W)
        entry1 = Entry(Frame4)
        entry1.grid(row=0, column=1)
        separador1 = Label(Frame4)
        separador1.grid(row=1)
        
        label2 = Label(Frame4, text="Distancia de Recorrido m")
        label2.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label2.grid(row=2, column=0, sticky=W)
        entry2 = Entry(Frame4)
        entry2.grid(row=2, column=1)
        separador2 = Label(Frame4)
        separador2.grid(row=3)
        
        label3 = Label(Frame4, text="Tiempo de carguio min")
        label3.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label3.grid(row=4, column=0, sticky=W)
        entry3 = Entry(Frame4)
        entry3.grid(row=4, column=1)
        separador3 = Label(Frame4)
        separador3.grid(row=5)
        
        label4 = Label(Frame4, text="Tiempo de descarga de material min")
        label4.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label4.grid(row=6, column=0, sticky=W)
        entry4 = Entry(Frame4)
        entry4.grid(row=6, column=1)
        separador4 = Label(Frame4)
        separador4.grid(row=7)
        
        label5 = Label(Frame4, text="Tiempo de estacionamiento min")
        label5.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label5.grid(row=8, column=0, sticky=W)
        entry5 = Entry(Frame4)
        entry5.grid(row=8, column=1)
        separador5 = Label(Frame4)
        separador5.grid(row=9)
        
        label6 = Label(Frame4, text="Velocidad de scoop con carga m/min")
        label6.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label6.grid(row=10, column=0, sticky=W)
        entry6 = Entry(Frame4)
        entry6.grid(row=10, column=1)
        separador6 = Label(Frame4)
        separador6.grid(row=11)
        
        label7 = Label(Frame4, text="Velocidad de scoop sin carga m/min")
        label7.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 5,
                pady = 2)
        label7.grid(row=12, column=0, sticky=W)
        entry7 = Entry(Frame4)
        entry7.grid(row=12, column=1)
        separador1 = Label(Frame4)
        separador1.grid(row=13)
        
        label8 = Label(Frame4, text="Horas disponibles h")
        label8.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label8.grid(row=14, column=0, sticky=W)
        entry8 = Entry(Frame4)
        entry8.grid(row=14, column=1)
        separador8 = Label(Frame4)
        separador8.grid(row=15)
        
        label9 = Label(Frame4, text="Horas disponibles M+R")
        label9.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label9.grid(row=16, column=0, sticky=W)
        entry9 = Entry(Frame4)
        entry9.grid(row=16, column=1)
        separador9 = Label(Frame4)
        separador9.grid(row=17)
        
        label10 = Label(Frame4, text="Disponibilidad fisica %")
        label10.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 10,
                pady = 2)
        label10.grid(row=18, column=0, sticky=W)
        entry10 = Entry(Frame4)
        entry10.grid(row=18, column=1)
        separador10 = Label(Frame4)
        separador10.grid(row=19)
        
        label11 = Label(Frame4, text="Factor de llenado")
        label11.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label11.grid(row=20, column=0, sticky=W)
        entry11 = Entry(Frame4)
        entry11.grid(row=20, column=1)
        separador11 = Label(Frame4)
        separador11.grid(row=21)
        
        label12 = Label(Frame4, text="Factor de esponjamiento")
        label12.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label12.grid(row=22, column=0, sticky=W)
        entry12 = Entry(Frame4)
        entry12.grid(row=22, column=1)
        separador12 = Label(Frame4)
        separador12.grid(row=23)
        
        label13 = Label(Frame4, text="Peso especifico de material")
        label13.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label13.grid(row=24, column=0, sticky=W)
        entry13 = Entry(Frame4)
        entry13.grid(row=24, column=1)
        separador13 = Label(Frame4)
        separador13.grid(row=25)
        
        label14 = Label(Frame4, text="Tonelaje por guardia")
        label14.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 5,
                pady = 2)
        label14.grid(row=26, column=0, sticky=W)
        entry14 = Entry(Frame4)
        entry14.grid(row=26, column=1)
        separador14 = Label(Frame4)
        separador14.grid(row=27)
        
        # CREACIÓN DE LABELS PARA OUPUTS
        label20 = Label(Frame6, text="Tiempo de transporte\ncon carga")
        label20.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label20.grid(row=0, column=0, sticky=W)
        separador20 = Label(Frame6)
        separador20.grid(row=1)
        
        label21 = Label(Frame6, text="Tiempo de transporte\nsin carga")
        label21.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 2,
                pady = 2)
        label21.grid(row=2, column=0, sticky=W)
        separador21 = Label(Frame6)
        separador21.grid(row=3)
        
        label22 = Label(Frame6, text="Capacidad real de\nla cuchara")
        label22.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 10,
                pady = 2)
        label22.grid(row=4, column=0, sticky=W)
        separador22 = Label(Frame6)
        separador22.grid(row=5)
        
        label23 = Label(Frame6, text="Tiemoo/ciclo")
        label23.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label23.grid(row=6, column=0, sticky=W)
        separador23 = Label(Frame6)
        separador23.grid(row=7)
        
        label24 = Label(Frame6, text="Nviajes/hora")
        label24.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 25,
                pady = 2)
        label24.grid(row=8, column=0, sticky=W)
        separador24 = Label(Frame6)
        separador24.grid(row=9)
        
        label25 = Label(Frame6, text="Producción/hora")
        label25.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 15,
                pady = 2)
        label25.grid(row=10, column=0, sticky=W)
        separador25 = Label(Frame6)
        separador25.grid(row=11)
        
        label26 = Label(Frame6, text="Tiempo por limpieza")
        label26.config(fg = "white",
                bg = "green",
                font = ("Black Arial",10),
                padx = 5,
                pady = 2)
        label26.grid(row=12, column=0, sticky=W)
        separador26 = Label(Frame6)
        separador26.grid(row=13)
        
        # COMANDO CALCULAR
        def calcular():
            ttcc = np.round((float(entry2.get()) / float(entry6.get())), decimals=2)
            ttsc = np.round((float(entry2.get()) / float(entry7.get())), decimals=2)
            crc = np.round((float(entry1.get())*0.764*float(entry13.get())*float(entry11.get())/float(entry12.get())), decimals=2)
            tc = np.round((float(entry3.get())+ttcc+float(entry5.get())+float(entry4.get())+ttsc), decimals=2)
            nvh = np.round((60 * float(entry10.get()) / tc), decimals=2)
            ph = np.round((crc * nvh), decimals=2)
            tdl = np.round((float(entry14.get()) / ph), decimals=2)
            
            re1 = Label(Frame6, text=ttcc)
            re1.grid(row=0, column=1)
            un1 = Label(Frame6, text="min")
            un1.grid(row=0, column=2)
            re2 = Label(Frame6, text=ttsc)
            re2.grid(row=2, column=1)
            un2 = Label(Frame6, text="min")
            un2.grid(row=2, column=2)
            re3 = Label(Frame6, text=crc)
            re3.grid(row=4, column=1)
            un3 = Label(Frame6, text="TM/cuchara")
            un3.grid(row=4, column=2)
            re4 = Label(Frame6, text=tc)
            re4.grid(row=6, column=1)
            un4 = Label(Frame6, text="min/ciclo")
            un4.grid(row=6, column=2)
            re5 = Label(Frame6, text=nvh)
            re5.grid(row=8, column=1)
            un5 = Label(Frame6, text="viajes/hora")
            un5.grid(row=8, column=2)
            re6 = Label(Frame6, text=ph)
            re6.grid(row=10, column=1)
            un6 = Label(Frame6, text="TM/hora")
            un6.grid(row=10, column=2)
            re7 = Label(Frame6, text=tdl)
            re7.grid(row=12, column=1)
            un7 = Label(Frame6, text="horas")
            un7.grid(row=12, column=2)
        
        # BOTON
        boton =Button(Frame5, text="CALCULAR", command=calcular)
        boton.config(
            bg = "red",
            padx = 30,
            pady = 30
            )
        boton.grid(row=0, column=0)
        
        mi_menu = Menu(ventana)
        ventana.config(menu=mi_menu,
                       bg = "lightblue")
        
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
        
    
    