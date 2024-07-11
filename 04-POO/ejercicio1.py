# 1. Ejercicio 1: Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

# Primera solución. Aquí no hay diferencia con la programación funcional.

class Alumno:
    ''' Inicializando los atributos de la clase Alumno'''
    def inicializar(self, nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')
    
    def resultado(self):
        if self.nota < 5:
            print('El alumno ha suspendido.')
        else:
            print('El alumno ha aprobado.')

# Bloque principal del programa

alumno1 = Alumno()
alumno2 = Alumno()

#Inicializar los atributos

alumno1.inicializar('Ivan', 8)
alumno2.inicializar('Pedro', 4)

#Imprimimos resultados

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()
