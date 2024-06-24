# Importamos las librerías de Tkinter y la de utilidades de ventana para centrarla y leerla.
# Fuente: https://www.youtube.com/watch?v=fDyO2vKrSfw&t=6s&ab_channel=Autodidacta
import tkinter as tk
from tkinter.font import BOLD
from pathlib import Path

import utilidades_ventana.generic as utl



class MenuPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Panel Maestro') # Se coloca el título de la ventana
        
        # Se busca el ancho y lo alto de la ventana, para que se maximice
        w, h = self.ventana.winfo_screenmmwidth(), self.ventana.winfo_screenmmheight()
        
        # Formateo de tuplas donde se indica el ancho y lo alto
        self.ventana.geometry("%dx%d+0+0" % (w,h))
        
        # Configuramos el fondo de la ventana -> blanco (#fcfcfc). Y que no redimensione la ventana.
        self.ventana.config(bg = '#fcfcfc')
        self.ventana.resizable(width = 0, height = 0 )



        # Importamos el logo de la carpeta imagenes, le asignamos un tamaño y la ponemos dentro de una etiquta (toda la pantalla)
        ruta_logo = Path('factura_DM\imagenes\cuadrado.png')
        logo = utl.leer_imagen(ruta_logo, (200, 200))

        label = tk.Label(self.ventana, image = logo, bg = '#fcfcfc')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.ventana.mainloop()



