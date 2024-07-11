import os
import json
from pathlib import Path

from funciones.leer_archivo import Lectura_archivo

class Add_usuario:

    @classmethod #metiodo estatico
    def __init__(cls, ruta):
        os.system('cls')
        cls.path = Path(ruta)
        cls.usuarios = Lectura_archivo.lee_archivo(ruta)
        cls.listaUsuarios = json.loads(cls.usuarios) # rescatando el archivo y lo tenemos en memoria
        # print(cls.listaUsuarios)
    
    @classmethod
    def add_usuario(cls):
        cls.nombre = input('Introduce el nombre de usuario').lower().strip() # strip elimina espacios a izq y derecha, lstrip para izq, rstrip a derecha sólo
        cls.apellidos = input('Introduce el apellido de usuario').lower().strip()
        cls.telefono = input('Introduce el telefono de usuario').lower().strip()
        cls.mail = input('Introduce el mail de usuario').lower().strip()

        # Comprobamos si el usuario ya está en la lista
        cls.usuarioPresente = False # Variable auxiliar
        for cls.usuario in cls.listaUsuarios: #Saber si los caracteres están dentro de ese campo
            cls.nombrePresente = cls.nombre in cls.usuario['nombre']
            cls.apellidoPresente = cls.apellidos in cls.usuario['apellidos'] 
            if cls.nombrePresente and cls.apellidoPresente:
                cls.usuarioPresente = True

        # Si el usuario no está en la lista, lo añadimos
        if not(cls.usuarioPresente):
            cls.datoUsuario = {
                'nombre': cls.nombre,
                'apellidos': cls.apellidos,
                'telefono': cls.telefono,
                'mail': cls.mail
            }
            cls.listaUsuarios.append(cls.datoUsuario) 
            cls.contenido = json.dumps(cls.listaUsuarios, indent = 4, sort_keys = False)
            cls.path.write_text(cls.contenido)
        else:
            print('El usuario ya está introducido.')          
