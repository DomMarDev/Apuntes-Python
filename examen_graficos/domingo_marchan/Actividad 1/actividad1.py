from pathlib import Path
import csv
import plotly.express as px



#leer datos como sifuera cadena y lo leemos

path = Path('./datos/world_fires_1_day.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_rows = next(reader) # rescata la primera linea, queremos la cabecera (reader)

for i, columna in enumerate(header_rows):
    
    print(i, columna)

# latitud en 0, longitud en 1, intensidad en 2

latitudes, longitudes, intensidades = [], [], []
for fila in reader:

    latitud = float(fila[0])
    longitud = float(fila[1])
    intensidad = float(fila[2])
    latitudes.append(latitud)
    longitudes.append(longitud)
    intensidades.append(intensidad)

# print(latitudes[:10])
# print(longitudes[:10])
# print(intensidades[:10])
title = 'Incendios Globales'


fig = px.scatter_geo(lat = latitudes, 
                    lon= longitudes, 
                    size= intensidades, 
                    title= title, 
                    color = intensidades, 
                    color_continuous_scale = 'viridis', # px.colors.named_colorscales() 
                    labels= {'color': 'Intensidad'}, 
                    projection= 'natural earth',                     
                    # hover_name= eq_titles, # la coma al final es por si queremos añadir más cosas
                   )
fig.show()