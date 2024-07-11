import matplotlib.pyplot as plt

# generamos una lista con números cuadrados como datos para el gráfico
valores_entrada = range(1,5001)
cubos = [x**3 for x in valores_entrada]

# Aquí el estilo (antes de fi, ax)
plt.style.use('ggplot') # guapos: 'ggplot', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-pastel', 'dark_background'...

fig, ax = plt.subplots()
ax.scatter(valores_entrada, cubos, c= cubos, cmap= plt.cm.inferno, s= 10) # en c lo que queremos representar / cmap= plt.cm.[tema]

# Título del gráfico
ax.set_title('Números cúbicos', fontsize= 24) # Titulo grafico
ax.set_xlabel('Valores', fontsize= 14) # Título ejeX
ax.set_ylabel('Cubo del valor', fontsize= 14)# Título ejeY

# Tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(labelsize= 12)

#estilo para cada eje
ax.axis([0,5100, 0, 130_000_000_000]) #eje x (start , finish) eje y (start, finish este lo he calculado elevando al cubo 5000 y sumandole una cantidad para que se vea bien)


plt.show()