import os
import json
from pathlib import Path

from funciones.leer_archivo import Lectura_archivo

class Editar_contacto:
    @classmethod
    def __init__(cls, ruta):
        os.system('cls')
        cls.path = Path(ruta)
        cls.usuarios = Lectura_archivo.lee_archivo(ruta)
        cls.listaUsuarios = json.loads(cls.usuarios)

        #Introducimos datos del usuario

        cls.nombre = input('Nombre del usuario: ').lower().strip()
        cls.apellidos = input('Apellidos del usuario: ').lower().strip()

        cls.indice = None

        for cls.usuario in cls.listaUsuarios:
            cls.nombrePresente = cls.nombre == cls.usuario['nombre']
            cls.apellidoPresente = cls.apellidos == cls.usuario['apellidos'] 

            if cls.nombrePresente and cls.apellidoPresente:
                cls.indice = cls.listaUsuarios.index(cls.usuario)

        if cls.indice != None:
            print(f'{cls.listaUsuarios[cls.indice]['nombre']}\t{cls.listaUsuarios[cls.indice]['apellidos']}\t{cls.listaUsuarios[cls.indice]['telefono']}\t{cls.listaUsuarios[cls.indice]['mail']}')
            while True:
                print('---- Selecciona la opción a editar ----')
                print('''
                      1) Nombre
                      2) Apellidos
                      3) Telefono
                      4) Mail 
                      5) Volver''' )
                opcion = input('Introduzca la opción deseada: ') 
                match(opcion):
                    case '1':
                        cls.nombre = input('Introduzca el nombre: ').lower().strip()
                        cls.listaUsuarios[cls.indice]['nombre'] = cls.nombre

                    case '2':
                        cls.apelllidos = input('Introduzca el apellido: ').lower().strip()
                        cls.listaUsuarios[cls.indice]['apellidos'] = cls.apelllidos
                    case '3':
                        cls.telefono = input('Introduzca el teléfono: ').lower().strip()
                        cls.listaUsuarios[cls.indice]['telefono'] = cls.telefono
                    case '4':
                        cls.mail = input('Introduzca el mail: ').lower().strip()
                        cls.listaUsuarios[cls.indice]['nmail'] = cls.mail                    
                    case '5':
                        break
                    case _:
                        print('Opción no contemplada')
                
            cls.contenido = json.dumps(cls.listaUsuarios, indent = 4, sort_keys = False)
            cls.path.write_text(cls.contenido)
        else:
            print('No se ha encontrado el usuario.')
