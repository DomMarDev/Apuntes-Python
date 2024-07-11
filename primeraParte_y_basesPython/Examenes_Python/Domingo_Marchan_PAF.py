import os

def clear_screen():
    ''' 
        Función para limpiar la pantalla del terminal
    '''
    os.system('cis')

def pause_screen():
    ''' 
        Función para pausar la pantalla del terminal
    '''
    print('Pulse enter para continuar')
    input()



# función de pedir y verificar la tarea y descripcion

def tarea_descripcion(listaTarea, listaDescripcion, estado):
    '''
        Esta funcion sirve para introducir una nueva tarea con una descripción asociada y darle el estado de pendiente.
        Si no se pone ninguna descripción, el bucle se repite.
        Si todo está correcto, me añade los nuevos datos en las respectivas listas y te lo retorna. 
    '''
    print('Vamos a insertar una Tarea')
    while True:
        tarea= input('Dame el nombre de la tarea')
        descripcion= input('Dame la descripción de la tarea')
        estadoTarea = 'Pendiente'
       
        
        if descripcion == '':
                print('No has introducido ninguna descripción')
                
                
        else:
                listaTarea.append(tarea)
                listaDescripcion.append(descripcion)
                estado.append(estadoTarea)
                break
                
    return listaTarea, listaDescripcion, estado


#Lista vacía?

def listaVacia(listaTarea):
    ''' 
        Esta función sirve para verificar que una lista está vacía mediante el uso del método len().
        Si la longitud le la lista == 0, no hay elementos dentro de la lista y, por tanto, está vacía.
    '''
    
    if len(listaTarea) == 0:
        print('\n La lista está vacía')
        return len(listaTarea) == 0
        

# Eliminar tarea 

def eliminar_tarea(listaTarea, listaDescripcion, estado):
    ''' 
        Esta función sirve para eliminar una tarea con su descripción y estado.
        Todo se ejecuta a partir de preguntar qué tarea vamos a borrar.
        Con el índice de la tarea (numérico), podemos eliminar la tarea y se verifica que este indice esté dentro del rango permitido.
        Se retornan las listas actualizadas si está todo correcto.
    '''

    printar_tareas(listaTarea, listaDescripcion, estado)

    print('Dime que tarea quieres eliminar') 
    
    tarea_Eliminada = int(input('Dame el valor de la lista:'))
    
    if tarea_Eliminada - 1 > len(listaTarea) - 1 or tarea_Eliminada == 0:
        print('\nEl número de la tarea introducido no es correcto o no corresponde con ninguna tarea.')
    else:
        tarea_Eliminada = tarea_Eliminada -1

        del listaTarea[tarea_Eliminada]
        del listaDescripcion[tarea_Eliminada]
        del estado[tarea_Eliminada]
        
    return listaTarea, listaDescripcion, estado

def completar_tarea(listaTarea, listaDescripcion, estado):
    ''' 
        Esta función sirve para completar una tarea (se actualiza la lista estado).
        Todo se ejecuta a partir de preguntar qué tarea vamos a completar.
        Con el índice de la tarea (numérico), podemos completar la tarea y se verifica que este indice esté dentro del rango permitido.
        Se retornan la lista actualizada de estado si está todo correcto.
    '''

    printar_tareas(listaTarea, listaDescripcion, estado)

    print('Dime que tarea quieres completar') 
    
    tarea_Completada = int(input('Dame el valor de la lista a completar:'))

    
    if tarea_Completada - 1 > len(listaTarea) - 1 or tarea_Completada == 0:
        print('\nEl número de la tarea introducido no es correcto o no corresponde con ninguna tarea.')
    else:
        tarea_Completada = tarea_Completada -1
        estado[tarea_Completada]  = 'Completada'


    return estado

def printar_tareas(listaTarea, listaDescripcion, estado):
     ''' 
        Esta función permite imprimir las listas correspodientes a la tarea, descripción de tarea y estado de tarea.
        Se recorre con un bucle for la lista tarea para coger el índice de la lista y así poder imprimir cada una de las listas con un índice numérico.
        (Puede hacerse mejor con el método enumerate(), pero a mi me gusta más hacerlo así)
     '''
     for i in listaTarea:
                index = listaTarea.index(i)
                indexTarea = index +1
                
                print(f' Tarea {indexTarea} {listaTarea[index]} ({estado[index]}) : {listaDescripcion[index]}')



#verificar indice 


    
listaTarea = []  

listaDescripcion = []

estado = []

while True:
    ''' 
        Menú que muestra las diferentes opciones a realizar para añadir un titulo de tarea y descripción de la misma.
        Opciones:
        1) Añadir Tarea 2) Eliminar Tarea 3) Completar Tarea 4) Mostrar tareas 5) Salir'
    '''
    
    print('Dame la opción a realizar: \n 1) Añadir Tarea\n 2) Eliminar Tarea\n 3) Completar Tarea \n 4) Mostrar tareas\n 5) Salir')
    
    opcion = int(input('Escoges la opción:'))
    
   
    if opcion == 1:
        #Añadir opcion y verificar que descripción no está vacía
        if listaVacia(listaTarea):
             listaTarea, listaDescripcion, estado = tarea_descripcion(listaTarea, listaDescripcion, estado)
        else:
             listaTarea, listaDescripcion, estado = tarea_descripcion(listaTarea, listaDescripcion, estado)

        
 
    elif opcion == 2:
        # Eliminar tarea y verificar indice y la lista está vacía o no
        if listaVacia(listaTarea):
            pass
        else:
            listaTarea, listaDescripcion, estado = eliminar_tarea(listaTarea, listaDescripcion, estado)
        pause_screen()
        clear_screen()

    elif opcion == 3:
        # Completar una tarea y verificar si la lista está vacia
        if not listaVacia(listaTarea):
            estado = completar_tarea(listaTarea, listaDescripcion, estado)
        pause_screen()
        clear_screen()       
    
    elif opcion == 4:
        # Mostrar la lista con la tarea completa o pendiente
        if listaVacia(listaTarea):
                    pass
        else:        
            printar_tareas(listaTarea, listaDescripcion, estado)
        pause_screen()
        clear_screen()

    elif opcion == 5:
        # Salir
        print('Has seleccionado salir')
        print('Fin del Programa')
        break
    else:
        print('Opcion no contemplada')
    
    print('Paso realizado\n')