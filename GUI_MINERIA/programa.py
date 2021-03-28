from tkinter import *
import pathlib
import os.path
from tkinter import messagebox
from PIL import Image, ImageTk

class Programa:
 
    
    def __init__(self, title, geometry, ruta, ruta_alt, resi):
        self.title = title
        self.geometry = geometry
        self.ruta = ruta
        self.ruta_alt = ruta_alt
        self.resi = resi
        
    def cargar(self):
        # ventana principal o ventana raiz
        ventana = Tk()
        self.ventana = ventana
        
        # Titulo
        ventana.title(self.title)
        
        # Dimensionarlo
        ventana.geometry(self.geometry)
        
        # ICONO
        #ruta = str(pathlib.Path().absolute()) + "/12. Tkinter/imagenes/logo_minsup_uncp.ico"
        ruta = os.path.abspath(self.ruta)
        
        if not os.path.isfile(self.ruta):
            ruta = os.path.abspath(self.ruta_alt)
        
        ventana.iconbitmap(ruta)
        
        # Estatico el dimensionamiento
        if self.resi:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
            
        
        
    def frame(self, ancho, altura, fondo, borde, relieve, fila, columna, pegado):
        marco = Frame(self.ventana, width=ancho, height=altura)
        marco.config(
            bg = fondo,
            bd = borde,
            relief = relieve
            )
        marco.grid(row=fila, column=columna, sticky=pegado)
        
    def imagenes(self, ruta, ruta_alt, fila, columna):
        rute = os.path.abspath(ruta)
        if not os.path.isfile(ruta):
            rute = os.path.abspath(ruta_alt)
        imagen = Image.open(rute)
        render = ImageTk.PhotoImage(imagen)
        
        Label(self.ventana, image = render).grid(row=fila, column=columna)
    
    def texto(self, marco, textos, color_fondo, color_letra, fila, columna, lapso, pegado):
        # Texto
        texto = Label(marco, text=textos)
        texto.config(
            bg = color_fondo,
            fg = color_letra
            )
        texto.grid(row=fila, column=columna, columnspan=lapso, sticky=pegado)
    
    
    def formulario(self, marco, fila, columna, pegado):
        formulario = Entry(marco)
        formulario.grid(row=fila, column=columna, sticky=pegado)
        
    def boton(self, marco, texto, comando, fila, columna):
        boton = Button(marco, text= texto, command= comando)
        boton.grid(row=fila, column=columna)
        
    def salir(self):
        resultado = messagebox.askquestion("Salir", "¿Estas seguro que quieres salir?")
        
        if resultado != "no":
            self.ventana.destroy()
    
    def alerta_info(self, texto):
        messagebox.showinfo("Informacion", texto)
        
    def alerta_peligro(self, texto):
        messagebox.showwarning("Peligro", texto)
    
    def alerta_error(self, texto):
        messagebox.showerror("Error", texto)
        
    def menu(self):
        mi_menu = Menu(self.ventana)
        self.ventana.config(menu=mi_menu)
        archivo = Menu(mi_menu, tearoff=0)
        
        return [mi_menu, archivo]      
        
    def arrancar(self):     
        self.ventana.mainloop()
