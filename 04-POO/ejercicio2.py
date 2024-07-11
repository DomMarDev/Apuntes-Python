import os

def clear_screen():
    os.system('cls')

class Persona:
    '''Inicializamos los atributos'''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        if self.edad >= 18:
            self.mayor = 'Mayor de edad'
        
        else:
            self.mayor = 'Menor de edad'
    
    def __str__(self):
        return f'Nombre {self.nombre}\nEdad: {self.edad}\n Resultado: {self.mayor}'

class Datos:
    def __init__(self):
        while True:
            self.nombre = input('Introduzca el nombre:')
            if not self.nombre:
                print('El nombre no puede estar vacío.')
            else:
                break
        while True:
            try:
                self.edad = int(input(f'Introduzca la edad de {self.nombre.title()}:'))
                break
            except ValueError:
                print('Vuelva a introducir la edad.')

clear_screen()
datos = Datos()

persona = Persona(datos.nombre, datos.edad)

print(persona)