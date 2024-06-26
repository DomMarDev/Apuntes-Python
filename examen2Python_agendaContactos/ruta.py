# Creando ruta absoluta, la carpeta datos la tenemos que crear nosotros. 

import os


def ruta():
    ruta_relativa = 'datos/usarios.json'

    ruta_absoluta = os.path.abspath(ruta_relativa)

    return f'{ruta_absoluta}'

# if __name__ == '__mian__':
#     print(ruta())