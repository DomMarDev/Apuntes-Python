import csv
from pathlib import Path
from datetime import datetime as dt
import matplotlib.pyplot as plt


path = Path('./datos/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_rows = next(reader) # rescata la primera linea, queremos la cabecera (reader)



# print(header_rows)

# for i, columna in enumerate(header_rows):
    
#     print(i, columna)

# La fecha esta en la en la fila 2 y la precipitación en el 5

fechas, precipitaciones= [], []

for fila in reader:
    fecha_actual = dt.strptime(fila[2], '%Y-%m-%d')
    print(fecha_actual)
    try:        
        precipitacion = float(fila[5])
    except ValueError:
        pass
        # print(f'Falta el dato de la {fecha_actual}')
    else:
        fechas.append(fecha_actual)
        precipitaciones.append(precipitacion)


# Trazamso las temperaturas máximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(16,9), dpi=128) # dpi = puntos por pulgada

ax.plot(fechas, precipitaciones, color= 'red')

# añadimos estilos
ax.set_title('Precipitaciones diarias en Sitka, año 2021', fontsize= 20)
ax.set_xlabel('', fontsize = 14)
fig.autofmt_xdate() # autoformato que dibuja la etiqueta del eje x en formato diagonal
ax.set_ylabel('Temperatura (ºF)', fontsize = 14) # alt 176 para grados
ax.tick_params(labelsize=12)
plt.show()