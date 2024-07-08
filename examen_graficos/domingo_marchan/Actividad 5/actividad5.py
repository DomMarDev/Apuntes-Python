import numpy as np
'''
Ejemplo:
arr_3 = np.array(
    [
        [ Enero
    Producto A ,B
    Tienda 1[1,2], 
    Tienda 2[3,4],
    Tienda 3[5,6]
        ],
        [ Fbrero
            [7,8], 
            [9,10],
            [11,12]
        ],
        [ Marzo
            [13,14], 
            [15,16],
            [17,18]
        ]
    ]
)
'''

# arr_3d = np.arange(18).reshape(3,3,2) por si queremos generar un array de forma manual, no aleatoria!

arr_3 = np.array(
    [
        [ # PA, PB  Ventas
            [1,2], 
            [3,4],
            [5,6]
        ],
        [
            [7,8], 
            [9,10],
            [11,12]
        ],
        [
            [13,14], 
            [15,16],
            [17,18]
        ]
    ]
)



print('Ventas producto cada mes:')
print(f'Enero: ProductoA = {sum(arr_3[0, :, 0])} ventas')
print(f'Enero: ProductoB = {sum(arr_3[0, :, 1])} ventas')

print(f'Febrero: ProductoA = {sum(arr_3[1, :, 0])} ventas')
print(f'Febrero: ProductoB = {sum(arr_3[1, :, 1])} ventas')

print(f'Marzo: ProductoA = {sum(arr_3[2, :, 0])} ventas')
print(f'Marzo: ProductoB = {sum(arr_3[2, :, 1])} ventas')

# Determinación de la tienda con mayores ventas totales en el mes de febrero
tienda1 = sum(arr_3[1, 0, :])
tienda2 = sum(arr_3[1, 1, :])
tienda3 = sum(arr_3[1, 2, :])

tiendas = [tienda1, tienda2, tienda3]

definTiendas = np.array(tiendas)

if definTiendas.argmax() == 0:
    print(f'La tienda 1 con {tienda1} ventas fué la ganadora del mes de febrero')
elif  definTiendas.argmax() == 1:
    print(f'La tienda 2 con {tienda2} ventas fué la ganadora del mes de febrero')
elif definTiendas.argmax() == 2:
    print(f'La tienda 3 con {tienda3} ventas fué la ganadora del mes de febrero')