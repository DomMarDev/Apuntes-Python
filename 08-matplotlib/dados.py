from random import randint
import plotly.express as px # importamos plotly

class Dado:
    ''' Una clase que representa un dado de x caras'''

    def __init__(self, num_caras= 6):
        ''' Por defecto el dado tiene 6 caras'''
        self.num_caras = num_caras

    def tirada(self):
        ''' Devuelve un número aleatorio entre 1 y el número de caras'''
        return randint(1, self.num_caras)
    
miDado = Dado() #instanciamos

misTiradas = [] # acumular datos del dado

for tirada in range(1000):
    tirada = miDado.tirada()
    misTiradas.append(tirada)

# print(misTiradas[:100]) # que muestre las 100 primeras

frecuencias = []
analisis_resultado = range(1, miDado.num_caras+1) # son los 6 lados del dado
for valor in analisis_resultado:
    frecuencia = misTiradas.count(valor)
    frecuencias.append(frecuencia)
# print(frecuencias)

# hacemos el histograma de frecuencias
titulo= 'Resultado de tirar un D6 1000 veces'
etiquetas= {
    'x': 'Cara del dado',
    'y': 'Frecuencia de resultados'
}

fig = px.line(x=analisis_resultado, y = frecuencias, title= titulo, labels= etiquetas)
fig.show() 
# se puede guardar etc en el navegador que te genera el host local. Se genera un html

# podemos poner line (gráfico de líneas) en vez de bar, scatter (gráfico de puntos)