# 1) Importando el módulo entero. 

# import pizza

# pizza.make_pizza('mediana', 'peperoni', 'champiñones', 'piña', 'jamón')


# 2) Importando una función específica del módulo. 
    
    # Si quieres añadir más funciones se separan por comas

# from pizza import make_pizza

# make_pizza('familiar', 'jamón', 'champiñones')

# # 3) Importando todas las funciones de un módulo.

     # Si el módulo tiene el mismo nombre que las funciones que tenemos aquí las sobreescribe. Es peligroso, mejor eviatarla.

# from pizza import *
# make_pizza(('familiar', 'jamón', 'champiñones'))

# 4) Creando alias a módulos y a funciones.

    # Módulos:
# import pizza as pi

    # Alias:
from pizza import make_pizza as mp
mp('familiar', 'jamón', 'champiñones')