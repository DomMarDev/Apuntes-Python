# Funcion que manda el pedido de la pizza
def make_pizza(size, *toppings):
    ingredientes = ', '.join(ingrediente for ingrediente in toppings)
    print(f'\nHaciendo una pizza de tamaño {size} con los siguientes ingredientes: {ingredientes}')