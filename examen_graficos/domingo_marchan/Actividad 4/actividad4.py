import numpy as np

# Creo el array de 20 números aleatorios entre 1 y 50
arr_1 = np.random.randint(1, 51, size= 20)
print(f' Array: {arr_1}')

# Crear un array booleano para indicar si los elementos son mayores de 25

# Reemplazo los números menores o iguales a 25 por False y los mayores por True. Creo un array booleano

lista = []
for valor in arr_1:
    if valor >25:
        valor = True
    else:
        valor = False
    lista.append(valor)

arr_boolean = np.array(lista)

print(f'Array booleano: {arr_boolean}')

# Filtro el array booleano para filtrar los elementos mayores que 25

indice = np.where(arr_boolean == True)

filtro = arr_1[indice]

print(f'Array filtrado que sólo muestra los mayores de 25: {filtro}')

# reemplazo sobre le aray original los elementos menores o iguales a 25 por 0

arr_2 = np.where(arr_1 <= 25, 0, arr_1)

print(f'Array reemplazado: {arr_2}')


    


    