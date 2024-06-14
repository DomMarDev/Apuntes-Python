class Alumno:
    def __init__(self):
        '''Inicio los atributos de la clase Alumno'''
        self.nombre = input('Introduzca su nombre:')
        while True:
            try:
                self.nota = float(input('Introduzca la nota:'))
                while self.nota < 0 or self.nota > 10:
                    self.nota = float(input('Introduzca la nota:'))
                if self.nota >= 5:
                    self.aprobado = 'Ha aprobado el curso!'
                else:
                    self.aprobado = 'No ha aprobado el curso!'
                break
            except:
                print('Introduzca una nota válida')
                continue
    
    def __str__(self):
        return f'Nombre: \t\t {self.nombre}\n Nota: \t\t {self.nota}\n Resultado: \t\t {self.aprobado}'
    
alumno1 = Alumno()
print(str(alumno1)) # String opcional