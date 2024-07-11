''' Primer proyecto por grupos:


Vamos a crear un programa para una agencia de viajes que permita gestionar destinos, clientes y reservas. Este programa tendrá como mínimo las siguientes funcionalidades:
- Añadir un nuevo destino (Código destino, Nombre destino y Precio destino).
- Añadir un nuevo cliente (ID cliente y Nombre cliente).
- Realizar una reserva (Pasaremos un código de destino y un ID de cliente).
- Cancelar una reserva (Pasaremos un código de destino y un ID de cliente).
- Mostrar todos los destinos (Mostraremos código, nombre y precio).
- Mostrar todos los clientes (Mostraremos ID y nombre).
- Mostrar todas las reservas (Mostraremos Cliente y Reserva).

Nuestro programa tiene que cumplir:
- Los parámetros entre paréntesis son orientativos y pueden ayudar a la funcionalidad del programa, podemos decidir otros.
- Las entradas y salidas de datos tienen que ser amigables con el usuario. O sea, darle un formato adecuado.
- Debemos controlar que las entradas de datos cumplan ciertos parámetros y crear las excepciones necesarias.
- Como mínimo deberíamos de tener dos módulos.
- Todas las funciones tienen que tener su correspondiente documentación (docstring), con su funcionamiento, parámetros de entrada y parámetros de salida.
- Uso de Git y GitHub para el control de versiones. Debéis añadirme como colaborador al repositorio de GitHub, donde también se realizará la entrega.
- Formato de entrega: Enlace al repositorio de GitHub (1 por grupo).

Componentes de los grupos:
Grupo 1: Domingo, Hongyin y Enrique.
''' 
destinos = []
clientes = []

#Funciones

def anadir_destino(destinos):
    ''' 
        Función que permite añadir un destino a la lista "destinos".

        Entradas:
            - Código del destino
            - Nombre del destino
            - Precio del destino

        Salidas:
            - Lista de destinos actualizada
    '''
    print('A continuación vas a introducir un nuevo destino a nuestra base de datos.\n Necesitarás:\n \t-Código de destino\n \t-Nombre del destino\n \t-Precio del destino (€)')
    
    codigo = input('Introduce el código asociado al destino').lower()
    destino = input('Introduce el destino').lower()
    while True:
        try:
            precio= float(input(f'Introduce el precio de ir al destino: {destino}.'))
            break
        
        except ValueError:
            print('Has de introducir el precio como un número.')

    destinos.append({'codigo destino': codigo, 'nombre destino': destino, 'precio destino': precio})

    return destinos


def anadir_cliente(clientes):
    ''' 
        Función que permite añadir un nuevo cliente a la lista "clientes".

        Entradas:
            - ID del cliente
            - Nombre del cliente
        
        Salidas:
            - Lista de clientes actualizada
    '''
    print('A continuación vas a introducir un nuevo cliente a nuestra base de datos.\n Necesitarás:\n \t-ID del cliente\n \t-Nombre del cliente')
    
    id_cliente = input('Introduce el ID asociado al cliente').lower()
    nombre_cliente = input('Introduce el nombre del cliente').lower()

    clientes.append({'codigo destino': '', 'nombre destino': '', 'precio destino': '', 'reserva': False, 'codigo destino': '', 'id cliente': id_cliente, 'nombre cliente': nombre_cliente })

    return clientes


def realizar_reserva(clientes, destinos):
    ''' 
        Función que permite realizar una reserva a la lista "clientes".

        Entradas:
            - Código de destino
            - ID de cliente
      
        Salidas:
            - Lista de clientes actualizada
    '''
    print('A continuación vas a cancelar una reserva. \n Necesitarás:\n \t-Código de destino\n \t-ID de cliente')
    codigo_destino = input('Introduce el código del destino para eliminar la reserva').lower()
    id_cliente = input('Introduce el ID del cliente del que quieres eliminar la reserva').lower()

    for cliente in clientes:
        if codigo_destino == cliente['codigo destino'] and id_cliente == cliente['codigo destino']:
            cliente['reserva'] = True
            cliente['codigo destino'] == codigo_destino
            cliente['codigo destino'] == id_cliente
            
            for destino in destinos:
                if codigo_destino == destino['codigo destino']:
                    cliente['nombre destino'] = destino['nombre destino']
                    cliente['precio destino'] = destino['precio destino']
                
                else:
                    pass

        else:
            pass
    # falta decir si no se encuentran el codigo y el id, que lo vuelva a introducir

        # if  codigo_destino !=  and id_cliente

    return clientes  


def cancelar_reserva(clientes):
    ''' 
        Función que permite cancelar una reserva a la lista "clientes".

        Entradas:
            - Código de destino
            - ID de cliente
      
        Salidas:
            - Lista de clientes actualizada
    '''
    print('A continuación vas a realizar una nueva reserva. \n Necesitarás:\n \t-Código de destino\n \t-ID de cliente')
    codigo_destino = input('Introduce el código del destino donde vas a hacer la reserva').lower()
    id_cliente = input('Introduce el ID del cliente').lower()

    for cliente in clientes:
        if codigo_destino == cliente['codigo destino'] and id_cliente == cliente['codigo destino']:
            cliente['reserva'] = False

        else:
            pass
    # falta decir si no se encuentran el codigo y el id, que lo vuelva a introducir

        # if  codigo_destino !=  and id_cliente

    return clientes 


def mostrar_destinos(destinos):
    ''' 
        Función que muestra todos los destinos (Se muestra código, nombre y precio).
    '''
    if destinos:
        print('Lista de destinos en nuestra base de datos:')
        for destino in destinos:
            print(f'Código destino: {destino['codigo destino']} | Nombre del destino: {destino['nombre destino']} | Precio de destino: {destino['precio destino']} ')
    else:
        print('No hay destinos en nuestra base de datos.')


def mostrar_clientes(clientes):
    ''' 
        Función que muestra todos los clientes (Se muestra ID cliente y nombre cliente).
    ''' 
    if clientes:
        print('Lista de destinos en nuestra base de datos:')
        for cliente in clientes:
            print(f'ID cliente: {cliente['id cliente']} | Nombre cliente: {cliente['nombre cliente']}')
    
    else:
        print('No hay clientes en nuestra base de datos.')


def mostrar_reservas(clientes):
    ''' 
        Función que muestra todas las reservas (Se muestra Cliente y Reserva).
    ''' 
    print('Reservas:')
    if clientes:
        for cliente in clientes:
            if cliente['reserva'] == True:
                print(f'ID cliente: {cliente['id cliente']} | Nombre cliente: {cliente['nombre cliente']} | Código destino: {cliente['codigo destino']} | Nombre destino: {cliente['nombre destino']}')
    
    else:
        pass
        # falta verificar que la lista de reservas no esté vacía.


# Principal

def menu_principal(destinos, clientes):


    while True:
        print('¿Qué operación quieres realizar?')
        print(' 1) Añadir un nuevo destino\n 2) Añadir un nuevo cliente\n 3) Realizar una reserva\n 4) Cancelar una reserva\n 5) Mostrar todos los destinos\n 6) Mostrar todos los clientes\n 7) Mostrar todos las reservas\n 8) Salir del programa')
        opcion = input()

        match(opcion):
            case '1':
                anadir_destino(destinos)
            case '2':
                anadir_cliente(clientes)
            case '3':
                realizar_reserva(clientes, destinos)
            case '4':
                cancelar_reserva(clientes)
            case '5':
                mostrar_destinos(destinos)
            case '6':
                mostrar_clientes(clientes)
            case '7':
                mostrar_reservas(clientes)
            case '8':
                print('Has seleccionado salir. Adios.')
                break
            case _:
                print('Opción no contemplada')

menu_principal(destinos, clientes)


