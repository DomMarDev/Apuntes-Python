# Importaciones
import os

from ruta import ruta
from agenda.agenda import Abrir_archivo
from funciones.anadir_contacto import Add_usuario
from funciones.leer_contacto import Leer_contactos
from funciones.buscar_contacto import Buscar_contacto
from funciones.editar_contacto import Editar_contacto

# ScriptPrincipal

class Menu:
    def __init__(self):
        os.system('cls')
        self.menu = ''' 
        Agenda personal
        1) Añadir contacto
        2) Lista de contactos
        3) Buscar
        4) Editar
        5) Cerrar
        '''
        print(self.menu)

        self.opcion = input('Introduzca una opción: ')

        match(self.opcion):
            case '1':
                Add_usuario(ruta())
                Add_usuario.add_usuario()
            case '2':
                Leer_contactos(ruta())
            case '3':
                Buscar_contacto(ruta())
            case '4':
                Editar_contacto(ruta())
            case '5':
                print('Saliendo de la agenda.')
                exit() # Te cierra la terminal de Python
            case _:
                print('Opción no contemplada')
    
        os.system('pause')
        self.__init__() # Función recursiva para que te vaya imprimiendo el método de __init__

miArchivo = Abrir_archivo()
miMenu = Menu()