import os

def clear_screen():
    os.system('cls')

class Triangulo:
    def __init__(self):
        self.lados = []
        for i in range(1,4):
            while True:
                try:
                    self.lados.append(float(input(f'Introduzca el lado {i}:')))
                    break
                except ValueError:
                    print('Introduzca un valor numérico correcto.')
    
    def imprime(self):
        for i, lado in enumerate(self.lados):
            print(f'Lado {i+1} del triángulo: {lado} cm')
    
    def triangulo_mayor(self):
        mayor = max(self.lados)
        indiceMayor = self.lados.index(mayor)

        print(f'El lado mayor es el lado {indiceMayor+1}, con {mayor} cm.')
    
    def tipo_triangulo(self):
        if self.lados[0] == self.lados[1] and self.lados[1] == self.lados[2]:
            print('El triángulo es equilátero.')
        
        elif self.lados[0] != self.lados[1] and self.lados[0] != self.lados[2] and self.lados[1] != self.lados[2]:
            print('El triángulo es escaleno.')

        else:
            print('El triángulo es escaleno.')

#Programa principal

triangulo = Triangulo()

triangulo.imprime()
triangulo.triangulo_mayor()
triangulo.tipo_triangulo()