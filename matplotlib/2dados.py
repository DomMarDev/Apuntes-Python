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
    
dado_1 = Dado(8) #instanciamos
dado_2 = Dado(12) #instanciamos

misTiradas = [] # acumular datos del dado

for tirada in range(1000):
    tirada = dado_1.tirada() + dado_2.tirada()
    misTiradas.append(tirada)

# print(misTiradas[:100]) # que muestre las 100 primeras

frecuencias = []
resultado_max = dado_1.num_caras + dado_2.num_caras

analisis_resultado = range(2, resultado_max+1)  # minimo de 2 dados es 2
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

fig = px.bar(x=analisis_resultado, y = frecuencias, title= titulo, labels= etiquetas)
# fig.update_layout(xaxis_dtick= 1) # que el axis aparezca en cada uno de los números

fig.show() 
# se puede guardar etc en el navegador que te genera el host local. Se genera un html

# podemos poner line (gráfico de líneas) en vez de bar, scatter (gráfico de puntos)

# para guardar directamente
fig.write_html('frecuencia_tirada_dos_dados.html')