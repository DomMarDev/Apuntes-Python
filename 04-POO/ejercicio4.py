import math

class Calculadora:
    def __init__(self):
        self.numeros = []

        for i in range(1,3):
            while True:
                try:
                    self.numeros.append(float(input(f'Introduce el número {i}:')))
                    break
                except ValueError:
                    print('Introduzca un número correcto.')
    
    def suma(self):
        print(f'El resultado de la suma es: {math.fsum(self.numeros)}')
    
    def resta(self):
        rest = self.numeros[0] - self.numeros[1]
        print(f'El resultado de la resta es: {rest}')
    
    def multiplicacion(self):
        mult = self.numeros[0] * self.numeros[1]
        print(f'El resultado de la multiplicación es: {mult}')

    def division(self):
        try:
            div = self.numeros[0] / self.numeros[1]
            print(f'El resultado de la división es: {math.floor(div)}') # redonde de la división a la baja
        except ZeroDivisionError:
            print('No se puede dividir por 0.')

calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()