# Creando clases

# Librerías para manejar las fechas y la librería para generar números aleatorios + librería calendar para saber si es año bisiesto o no

from datetime import datetime, date
from random import randint
from calendar import isleap #(devuelve true or false si es bisiesto o no)

# formato de fechas en anglosajón, queremos en español (esto en mac no funciona)
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

class Generador_Fechas:
    ''' Generador de fechas en función del año'''
    def __init__(self):
        self.anyo = datetime.now().year #para escoger el año actual

    def genera_fecha(self):
        '''Generar un mes aleatorio'''
        mes = randint(1,12)

        match mes:
            case 2:
                if isleap(self.anyo):
                    dia = randint(1,29)
                else:
                    dia = randint(1,28)
            case 4 | 6 | 9 | 11:
                dia = randint(1,30)
            case _:
                dia = randint(1,31)
        
        return date(self.anyo, mes, dia)
    
    def genera_fecha_aleatorias(self, numero):
        fechas = [self.genera_fecha() for _ in range(numero)] # El guión es por convención de python, es sólo para generar una variable que luego no se utilizará.
        
        return fechas
    
    def ordena_fechas(self, fechas):
        for fecha in sorted(fechas):
            print(fecha.strftime('%A, %d de %m de %Y'))
    

# Instancia a la generación de dechas aleatorias

generador = Generador_Fechas()

# Generamos una lista de 10 fechas aleatorias

fechasAleatorias = generador.genera_fecha_aleatorias(10)

# Mostramos las fechas ordnadas

fechasOrdenadas = generador.ordena_fechas(fechasAleatorias)