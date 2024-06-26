import os
import json
from funciones.leer_archivo import Lectura_archivo

class Buscar_contacto:
    @classmethod
    def __init__(cls, ruta):
        os.system('cls')
        cls.usuarios = Lectura_archivo.lee_archivo(ruta)
        cls.listaUsuarios = json.loads(cls.usuarios)

        cls.nombre = input('Introduce el nombre a buscar: ').lower().strip()

        cls.usuarioPresente = False

        for cls.usuario in cls.listaUsuarios:
            if cls.nombre in cls.usuario['nombre']:
                print(f'{cls.usuario['nombre']}\t {cls.usuario['apellidos']}\t {cls.usuario['telefono']}\t {cls.usuario['mail']}')
                cls.usuarioPresente = True
        else: # Se ejecuta después del for
            if cls.usuarioPresente:
                pass
            else:
                print('El usuario no está registrado.')
        