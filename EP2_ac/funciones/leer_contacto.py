import json
import os
from pathlib import Path

from funciones.leer_archivo import Lectura_archivo

class Leer_contactos:
    @classmethod
    def __init__(cls,ruta):
        os.system('cls')
        cls.usuarios = Lectura_archivo.lee_archivo(ruta)
        cls.listaUsuarios = json.loads(cls.usuarios)

        if not(cls.listaUsuarios):
            print('No hay contactos en la lista.')
        else:
            for cls.usuario in cls.listaUsuarios:
                print(f'{cls.usuario['nombre']}\t {cls.usuario['apellidos']}\t {cls.usuario['telefono']}\t {cls.usuario['mail']}')