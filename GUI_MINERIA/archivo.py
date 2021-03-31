import tkinter
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

class Archivo():

    def openFile(self):
        filepath = filedialog.askopenfilename()
        self.filepath = filepath
    
    def curva(self):
        data = pd.read_csv(self.filepath)
                
        volumen = data["XINC"]*data["YINC"]*data["ZINC"]
        data = data.assign(VOLUMEN=volumen.values)
        data.shape
        
        ton = data["VOLUMEN"]*data["SG"]
        data = data.assign(TON=ton.values)
        
        columns = ["Li"]
        
        n = 0.1
        dato = [0]
        for i in range(10):
            datos = dato[i] + n
            dato.append(datos)
                
        dfn = pd.DataFrame(dato, columns=columns)
                
        ls = dfn["Li"] + n
        dfn = dfn.assign(Ls = ls.values)
                
        mc = (dfn["Li"] + dfn["Ls"])/2
        dfn = dfn.assign(Mc = mc.values)
                
        tonelaje = []
    
        for i in range(len(dfn["Li"])):
            suma = []
            for j in range(len(data["AU"])):
                ore = data["AU"][j]
                li = dfn["Li"][i]
                if ore > li:
                    suma.append(data["TON"][j])
            tonelaje.append(sum(suma))
                
        Ton = pd.DataFrame(tonelaje, columns = ["Tonelaje"])
        dfn = dfn.assign(Tonelaje = Ton.values)
                
        tones = dfn["Tonelaje"].tolist()
        ton_m = []
                
        for i in range(len(tones)):
            if i+1 in range(len(tones)):
                a = tones[i] + tones[i+1]
            else:
                a = tones[i]
            ton_m.append(a)
                
        tone_m = pd.DataFrame(ton_m, columns=["Tonelaje Mg"])
        dfn = dfn.assign(Tonelaje_Mg = tone_m.values)
                
        suma = []
    
        for i in range(len(dfn["Mc"])):
            n = dfn["Mc"][i] * dfn["Tonelaje_Mg"][i]
            suma.append(n)
                
        ley_media = []
        a = sum(suma)
        ley_media.append(a)
                    
        for i in range(len(dfn["Mc"])):
            suma.pop(0)
            m = sum(suma)
            if m != 0:
                ley_media.append(m)
                
        for i in range(len(ley_media)):
            ley_media[i] = ley_media[i] / sum(dfn["Tonelaje_Mg"])
                        
        ley = pd.DataFrame(ley_media, columns=["Ley Media"])
        dfn = dfn.assign(Ley_Media = ley.values)
                
        ley_de_corte = dfn["Li"].tolist()
        self.ley_de_corte = ley_de_corte
        tonelaje = dfn["Tonelaje"].tolist()
        self.tonelaje = tonelaje
        ley_media = dfn["Ley_Media"].tolist()
        self.ley_media = ley_media
                
        mainpath = r"C:/Users/egt_d/SCRIPTS MINERIA/Scripts-Miner-a-"
        filename = r"CURVA TONELAJE LEY/nuevo2.csv"
        fullpath = os.path.join(mainpath, filename)
                
        dfn.to_csv(fullpath, index=False)
    def graph(self):
        #------------------------------CREAR VENTANA---------------------------------
        root = Tk()
        root.title("Grafica insertada en Tkinter")
        #----------------------GRAFICA----------------------------------------------
        # Create some mock data
        t = self.ley_de_corte
        data1 = self.tonelaje
        data2 = self.ley_media
        
        fig, ax1 = plt.subplots(figsize=(10,10), facecolor="lightyellow")
        plt.suptitle('Curva Tonelaje - ley',color='blue', fontsize=20, fontweight="bold")
        
        color = 'tab:brown'
        ax1.set_xlabel('Ley de Corte')
        ax1.set_ylabel('Tonelaje', color=color)
        ax1.plot(t, data1, color=color)
        ax1.tick_params(axis='y', labelcolor=color, size=20)
        
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        
        color = 'tab:orange'
        ax2.set_ylabel('Ley Media', color=color)  # we already handled the x-label with ax1
        ax2.plot(t, data2, color=color)
        ax2.tick_params(axis='y', labelcolor=color, size=20)
        
        escala = 10
        ticks_x = ticker.FuncFormatter(lambda x, pos:'{:.3f}'.format(x/10))
        ax1.xaxis.set_major_formatter(ticks_x)
        
        ticks_y = ticker.FuncFormatter(lambda y, pos:'{:.1f}'.format(y/10))
        ax1.yaxis.set_major_formatter(ticks_y)
        
        
        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        plt.show()
        
        #---------------------------------------------------------------------------
        canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
        toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        tkinter.mainloop()
