# Creamos un script para generar un archivo json

import os
from pathlib import Path
import json

from ruta import ruta

class Abrir_archivo:
    def __init__(self):
        self.ubicacion = ruta() # Ejecuta ruta
        self.archivoUsuarios = Path(f'{self.ubicacion}')
        try:
            self.usuarios = self.archivoUsuarios.read_text() #Lo lee/hay algo?
            print('Archivo inicializado correctamente')
            os.system('pause')
        except FileNotFoundError:
            self.usuarios = []
            self.contenidoUsuarios = json.dumps(self.usuarios, indent= 4, sort_keys= False)
            self.archivoUsuarios.write_text(self.contenidoUsuarios) # Creamos el archivo con el contenido de sel.usuarios, que es una lista vacía.
            print('Archivo creado!!')
            os.system('pause')

#Prueba unitaria
if __name__ == '__main__':
    miArchivo = Abrir_archivo()