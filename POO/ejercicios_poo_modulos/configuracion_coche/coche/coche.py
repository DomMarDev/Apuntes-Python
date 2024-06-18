class Cotxe:
    def __init__(self, marca, modelo, anyo):
        self.marca = marca
        self.modelo = modelo 
        self.anyo = anyo
        self.lectura_kilometros = 1000
    
    def __str__(self):
        coche_usuario = f'{self.anyo} | {self.marca} | {self.marca} | {self.lectura_kilometros}'
        return coche_usuario.title()
    
    def actualizacion_kilometros(self, actualizacion):
        if actualizacion >= self.lectura_kilometros:
            self.lectura_kilometros = actualizacion
            kilometros = f'Este coche tiene {self.lectura_kilometros} kilometros'
        else:
            kilometros = f'Los kilometros actuales no pueden ser inferiores'
        
        return kilometros