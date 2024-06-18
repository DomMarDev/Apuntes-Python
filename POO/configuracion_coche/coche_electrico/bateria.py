class Bateria:
    def __init__(self, modelo_bateria = 'M140'):
        self.modelo_bateria = modelo_bateria
    
    def __str__(self):
        modelo_bateria = input('Introduzca un modelo de batería (Enter para modelo estándar): ')
        if modelo_bateria:
            self.modelo_bateria = modelo_bateria
        
        return f'El modelo de batería que llebva este coche es: {self.modelo_bateria}'