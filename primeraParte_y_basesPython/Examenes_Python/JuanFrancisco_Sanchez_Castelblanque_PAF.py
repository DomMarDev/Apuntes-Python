import os
opcion = 0
listaTareas = []

def BorrarPantalla():
    os.system('cls')

def AgregarTarea():
    '''
        Función que sirve para agregar una cadena de carácteres al final de una lista mutable
    '''
    print("\nIntroduzca una breve descripción de la tarea:")
    tarea = input() + " (PENDIENTE)"
    if tarea == " (PENDIENTE)":
        print("La descripción de la tarea no puede estar vacía")
        AgregarTarea()
    else:
        listaTareas.append(tarea)
    

def BorrarTarea():
    '''
        Función que sirve para borrar una tarea correspondiente al índice facilitado por el usuario.
        Se le mostrará la lista y realizaremos un bucle While mientras no se introduzca un índice válido
    '''
    tareaBorrada = False
    MostrarLista()
    if ListaVacia() == False:
        print("\nIntroduce el índice de la tarea que deseas borrar")
        while tareaBorrada == False:
            indice = int(input())
            if indice - 1 > listaTareas.__len__() - 1 or indice == 0:
                print("\nEl índice introducido no es correcto o no corresponde con ninguna tarea en la lista. Repita de nuevo:")
            else:
                del listaTareas[indice - 1]
                print("Se ha borrado la tarea")
                tareaBorrada = True

def ListaVacia():
    '''
        Función con retorno condicional que comprobará en cada paso por el programa si la lista se encuentra vacía
    '''
    if listaTareas.__len__() > 0:
        estaVacia = False
    else:
        estaVacia = True
    return estaVacia

def MostrarLista():
    '''
        Función que mostrará la lista mediante un FOR, con un enumerate. 
        En el mismo tiempo usaremos el contador 'i' para ir colocando a la izquierda el índice de cada elemento
    '''
    if ListaVacia() == False:
        print("")
        for i, tarea in enumerate(listaTareas):
            print(f'{i+1}. {tarea}')
    else:
        print("\nLa lista está vacia")

def CompletarTarea():
    '''
        Función que substituirá el (PENDIENTE) por (COMPLETADA)
        Primero mostraremos la lista de tareas al usuario, y posteriormente pediremos el índice de la tarea que corresponda
        Crearemos una variable auxiliar donde almacenar la cadena enteramente junto con (PENDIENTE) procedente de la lista
        Crearemos otra cadena que almacenará unicamente la tarea, sin el estado de la tarea
        Por último almacenaremos en la lista el contenido de la variable 'tarea' mas el estado (COMPLETADO)
    '''
    MostrarLista()
    if ListaVacia() == False:
        print("\nIntroduce el índice de la tarea que deseas completar")
        tareaCompletada = False
        while tareaCompletada == False:
            indice = int(input())
            if indice - 1 > listaTareas.__len__() - 1 or indice == 0:
                print("\nEl índice introducido no es correcto o no corresponde con ninguna tarea en la lista. Repita de nuevo:")
            else:
                guardarTodo = listaTareas[indice - 1]
                if guardarTodo[-11:] == "(PENDIENTE)":
                    tarea = guardarTodo[:-11] + " (COMPLETADO)"
                    listaTareas[indice - 1] = tarea
                    print("Se ha completado la tarea")
                    tareaCompletada = True
                else:
                    print("Esta tarea ya esta completada")

BorrarPantalla()
print("=====----- / Bienvenido al gestor de tareas \ -----=====")
# Bucle para la selección del menú
while(opcion != 5):
    print(
        "\nIndica que opción deseas hacer:\n"
        "1. Agregar una tarea a la lista\n"
        "2. Borrar una tarea de la lista\n"
        "3. Completar una tarea de la lista\n"
        "4. Mostrar la lista de tareas\n"
        "5. Salir"
    )
    opcion = int(input())

    if opcion <= 5 and opcion >= 1:
        if opcion == 1:
            os.system('cls')
            AgregarTarea()
        elif opcion == 2:
            os.system('cls')
            BorrarTarea()
        elif opcion == 3:
            os.system('cls')
            CompletarTarea()
        elif opcion == 4:
            os.system('cls')
            MostrarLista()
    else:
        print("Introduce una opción válida\n")

print("¡Hasta la próxima!")
            