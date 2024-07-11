import os

def clear_screen():
    ''' 
        Función para limpiar la pantalla del terminal
    '''
    os.system('cls')

def pause_screen():
    ''' 
        Función para pausar la pantalla del terminal
    '''
    print('Pulse enter para continuar')
    input()

''' 
4.  Escribir un programa en Python que gestione una biblioteca. La biblioteca contiene una colección de libros y cada libro tiene un título, un autor y un año de publicación. 
El programa debe ofrecer las siguientes funcionalidades mediante el uso de funciones:

- Añadir un nuevo libro: Se pedirá al usuario el título, el autor y el año de publicación del libro, y se añadirá a la colección.
- Mostrar todos los libros: Se mostrarán todos los libros en la colección.
- Buscar libros por autor: Se pedirá al usuario el nombre de un autor y se mostrarán todos los libros escritos por ese autor.
- Eliminar un libro: Se pedirá al usuario el título de un libro y se eliminará de la colección si existe.
- Terminar el programa: Finalizar la ejecución del programa.
'''
''' 
    Lista  'biblioteca' donde se van a ir guardando los diccionarios correspondientes a los libros introducidos por el usuario.
'''
biblioteca = []

#Funciones

def nuevo_libro(biblioteca):
    '''Función que pide al usuario el título, el autor y el año de publicación del libro, y se añade a la lista "biblioteca" como diccionario.
        Hay un control de entrada para el valor numérico del año de publicación
        Se retorna la biblioteca con un nuevo diccionario que contiene los datos del libro.

       '''
    
    hay_libro(biblioteca)

    print('\nVamos a añadir un nuevo libro a la biblioteca\n')

    autor = input('Inserta el autor del libro').lower()    
    titulo = input('Inserta el título del libro').lower()

    while True:
        try:
            ano = int(input('Inserta el año de publicación del libro'))
            break
        except ValueError:
            print('No has introducido un valor numérico en el año')

    libro = {'autor': autor, 'titulo': titulo, 'año': ano} 

    biblioteca.append(libro)

    return biblioteca
    

def mostrar_libros(biblioteca):
    ''' 
        Función que muestra los libros de la biblioteca.
        Condicional que revela si no hay libros en la biblioteca.
        Si los hay, se recorre la lista biblioteca y se printan las claves y valores de los libros en cuestión ordenados por orden de entrada en la biblioteca.
    '''
    
    if hay_libro(biblioteca):
        indice = 0
        for libro in biblioteca:
            indice = indice +1
            print(f'Libro {indice}: ', end= ' ')
            print(f'Autor: {libro['autor'].title()} | Título: {libro['titulo'].title()} | Año publicación: {libro['año']}')
            print('\n')
    else:
        pass    


def buscar_libro(biblioteca):
    ''' 
        Función que busca los libros de un autor en la biblioteca
        Condicional que revela si no hay libros en la biblioteca
        Si los hay, se recorre la lista biblioteca y se printan los libros de un autor solicitado
    '''    
    if hay_libro(biblioteca):

        mostrar_libros(biblioteca)

        print('Vamos a buscar los libros dados un autor')

        autor_buscado = input('Dame el autor a buscar').lower()

        print(f'Los libros de {autor_buscado} son:\n')

        indice = 0
        lista_autores = []

        for libro in biblioteca:
            if libro['autor'] == autor_buscado:
                lista_autores.append(libro)
                indice = indice+1
                print(f'Libro {indice}:', end = ' ')
                print(f'Autor: {libro['autor'].title()} | Título: {libro['titulo'].title()} | Año publicación: {libro['año']}')
        if len(lista_autores) == 0:
                print('No tenemos libros de este autor')
        else:
            pass


def eliminar_libro(biblioteca):
    ''' 
    Función para eliminar libros de la bibliteca (si los hay):
        Condicional para saber si no hay libros en la biblioteca.
        Si los hay:
            Se pedirá al usuario el título de un libro y se eliminará de la biblioteca si existe.
            Para ello, la lista_titulos va a guardar todos los libros que contengan el titulo introducido.
            Si la longitud de esta lista, tras recorrer la lista biblioteca, es 0; nos indicará que no hay libros con ese título.
        Retorna la biblioteca.
    '''
    
    lista_titulos = []

    if hay_libro(biblioteca):

        mostrar_libros(biblioteca)

        print(f'\n Vamos a borrar un libro por su título')

        borrar_libro = input('Dame el titulo del libro a eliminar').lower()
        
        for libro in biblioteca:
            if libro['titulo'] == borrar_libro:
                lista_titulos.append(libro)
                print(f'Autor: {libro['autor'].title()} | Título: {libro['titulo'].title()} | Año publicación: {libro['año']} (Eliminado)')
                biblioteca.remove(libro)
            if len(lista_titulos) == 0:
                    print('No tenemos este titulo')
            else:
                pass

    return biblioteca
                

def hay_libro(biblioteca):
    ''' Función que sirve para saber si la biblioteca se encuentra vacía(sin libros).
        Se valora la longitud de la lista biblioteca.
        Si esta no tiene elementos retorna un false y te avisa de que no hay libros en la biblioteca (False).
        Si hay libros dentro de la lista va a retornar un True.
    '''

    bibliotecaVacia = len(biblioteca)

    if bibliotecaVacia == False:
        print('No hay ningun libro en la biblioteca')
    else:
        pass

    return bibliotecaVacia


# Menú
def principal():
    ''' 
        Función principal que contiene el menú usado para la biblioteca.
    '''
    biblioteca = []

    print('Bienvenido a la Biblioteca CIFO Violeta')

    while True:
        ''' 
            Menú que te muestra las diferentes opciones de la biblioteca:
                1) Añadir un nievo libro
                2) Mostrar todos los libros
                3) Buscar libros por autor
                4) Eliminar un libro
                5) Terminar el programa
                Si se pulsa cualquier cosa que no sea un número del 1 al 5 mostrará en pantalla 'opción no contemplada'

        '''
        print('''
                1) Añadir un nievo libro
                2) Mostrar todos los libros
                3) Buscar libros por autor
                4) Eliminar un libro
                5) Terminar el programa
            ''')
        opcion= input('Dame la opcion')

        match(opcion):
            case '1':
                #Opcion 1: Añadir un nievo libro
                nuevo_libro(biblioteca)
                pause_screen()
                clear_screen()
            case '2':
                #Opcion 2: Mostrar todos los libros
                mostrar_libros(biblioteca)
                pause_screen()
                clear_screen()          
            case '3':
                #Opcion 3: Buscar libros por autor
                buscar_libro(biblioteca)
                pause_screen()
                clear_screen()
            case '4':
                #Opcion 4: Eliminar un libro
                eliminar_libro(biblioteca)
                pause_screen()
                clear_screen()
            case '5':
                #Opcion 5: Terminar el programa           
                print('Gracias por su visita')
                break
            case _:
                print('Opción no contemplada')
                clear_screen()
principal()