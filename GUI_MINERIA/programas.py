from tkinter import *
from tkinter import ttk
import pathlib
import os.path
from tkinter import messagebox
from PIL import Image, ImageTk

class Programas():
    def seguridad(self):
        ventana = Tk()
        
        ventana.title("Security and Safety | Erick Tocasca")
        ventana.geometry("600x600")
        ventana.resizable(0,0)
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
                
        Button(ventana, text="Estres Termico").grid(row= 0, column=2)
        Button(ventana, text="Ruido Ocupacional").grid(row= 1, column=2)
        Button(ventana, text="Consumo Basal").grid(row= 2, column=2)
        Button(ventana, text="Consumo Basal").grid(row= 3, column=2)
        Button(ventana, text="Consumo Basal").grid(row= 4, column=2)
        
        ventana.mainloop()
    
    def Cur_Ton_Ley(self):
        # Definir ventana
        ventana = Tk()
        ventana.title("Proyecto con Tkinter | Erick Tocasca")
        #ventana.geometry("400x400")
        ventana.minsize(400, 400)
        ventana.resizable(0,0)
        
        # Pantallas
        def home():
            # Montar Pantalla
            home_label.config(
                fg = "white",
                bg = "black",
                font = ("Arial",30),
                padx = 160,
                pady = 20
                )
            home_label.grid(row=0, column=0)
            
            products_box.grid(row=2)
            
            # Encabezado
            home_label.config(
                fg = "white",
                bg = "black",
                font = ("Arial",30),
                padx = 160,
                pady = 20
                )
            home_label.grid(row=0, column=0, columnspan=15)
            
            # Campos del formulario
            home_frame.grid(row=1)
            home_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            home_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            
            home_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            home_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
            
            home_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
            home_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
            home_description_entry.config(
                width = 30,
                height = 5,
                font = ("Consolas", 10),
                padx = 15,
                pady = 15
                )
            
            home_separator.grid(row=4)
            
            boton.grid(row=5, column=1, sticky=NW)
            boton.config(
                padx=15,
                bg = "black",
                fg = "white"
                )
            
            # Listar productos
            """
            for product in products:
                if len(product) == 3:
                    product.append("added")
                    Label(products_box, text=product[0]).grid()
                    Label(products_box, text=product[1]).grid()
                    Label(products_box, text=product[2]).grid()
                    Label(products_box, text="-------------------").grid()
            """
            
            for product in products:
                if len(product) == 3:
                    product.append("added")
                    products_box.insert("",0,text=product[0], values=(product[1]))
            
            # Ocultar otras pantallas
            add_label.grid_remove()
            info_label.grid_remove()
            data_label.grid_remove()
            add_frame.grid_remove()
            
            return True
        
        def graph():
            # Encabezado
            add_label.config(
                fg = "white",
                bg = "black",
                font = ("Arial",30),
                padx = 160,
                pady = 20
                )
            add_label.grid(row=0, column=0, columnspan=15)
            
            # Campos del formulario
            add_frame.grid(row=1)
            add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            
            add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
            
            add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
            add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
            add_description_entry.config(
                width = 30,
                height = 5,
                font = ("Consolas", 10),
                padx = 15,
                pady = 15
                )
            
            add_separator.grid(row=4)
            
            boton.grid(row=5, column=1, sticky=NW)
            boton.config(
                padx=15,
                bg = "black",
                fg = "white"
                )
            
            # Ocultar otras pantallas
            home_label.grid_remove()
            info_label.grid_remove()
            data_label.grid_remove()
            products_box.grid_remove()
            
            return True
        
        def info():
            info_label.config(
                fg = "white",
                bg = "black",
                font = ("Arial",30),
                padx = 100,
                pady = 20
                )
            info_label.grid(row=0, column=0)
            
            data_label.grid(row=1, column=0)
            
            # Ocultar otras pantallas
            home_label.grid_remove()
            add_label.grid_remove()
            add_frame.grid_remove()
            products_box.grid_remove()
            
            return True
        
        def add_product():
            products.append([
                name_data.get(),
                price_data.get(),
                add_description_entry.get("1.0","end-1c")
                ])
            name_data.set("")
            price_data.set("")
            add_description_entry.delete("1.0", END)
            
            home()
        
        # Variables Importantes
        products = []
        name_data = StringVar()
        price_data = IntVar() 
        
        # Definir campos de pantalla (INICIO)
        home_label = Label(ventana, text="Inicio")
        #products_box = Frame(ventana, width=250)
        Label(ventana).grid(row=1)
        products_box = ttk.Treeview(height=12, columns=2)
        products_box.grid(row=1, column=0, columnspan=2)
        products_box.heading("#0", text="Producto", anchor=W)
        products_box.heading("#1", text="Precio", anchor=W)
        
        # Definir campos de pantalla (ADD)
        add_label = Label(ventana, text="Grafica")
        
        # Crear campos del formulario
        add_frame = Frame(ventana)
        add_name_label = Label(add_frame, text="Producto:")
        add_name_entry = Entry(add_frame, textvariable = name_data)
        
        add_price_label = Label(add_frame, text="Precio:")
        add_price_entry = Entry(add_frame, textvariable = price_data)
        
        add_description_label = Label(add_frame, text="Descripcion:")
        add_description_entry = Text(add_frame)
        
        # Crear campos del formulario
        home_frame = Frame(ventana)
        home_name_label = Label(home_frame, text="Producto:")
        home_name_entry = Entry(home_frame, textvariable = name_data)
        
        home_price_label = Label(home_frame, text="Precio:")
        home_price_entry = Entry(home_frame, textvariable = price_data)
        
        home_description_label = Label(home_frame, text="Descripcion:")
        home_description_entry = Text(home_frame)
        
        # Separador para boton
        home_separator = Label(home_frame, text="")
        
        # Definir el boton
        boton = Button(home_frame, text="Guardar", command=add_product)
        
        # Separador para boton
        add_separator = Label(add_frame, text="")
        
        # Definir el boton
        boton = Button(add_frame, text="Guardar", command=add_product)
        
        # Definir campos de pantalla (INFO)
        info_label = Label(ventana, text="Informacion")
        data_label = Label(ventana, text="Creado por Erick Tocasca - 2020")
        
        # Cargar Pantalla Inicio
        home()
        
        # Menu superior
        menu_superior = Menu(ventana)
        
        menu_superior.add_command(label="Inicio", command=home)
        menu_superior.add_command(label="Grafica", command=graph)
        menu_superior.add_command(label="Informacion", command=info)
        menu_superior.add_command(label="Salir", command=ventana.destroy)
        
        
        # Cargar Menu
        ventana.config(menu=menu_superior)
        
        # Cargar ventana
        ventana.mainloop()