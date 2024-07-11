import os
def clear_screen():
    os.system('cls')

def pause_screen():
    print('Pulse enter para continuar')
    input()


#Funciones

def anadir_libro(biblioteca):
        
    while True:
        titulo = input('Ingrese el título del libro').lower()
        if not titulo:
            print('El campo titulo no puede estar vacío')
        else:
            break

    while True:
        autor = input('Ingrese el autor del libro').lower()
        if not autor:
            print('EL campo no puede estar vacio')
        else:
            break
        
    while True:
        try:
            anyo = int(input('Ingrese el año del libro'))
            break
        
        except ValueError:
            print('Inserte un año válido')
        
    biblioteca.append({'titulo' : titulo, 'autor' : autor, 'año' : anyo})

    print('Libro introducido con éxito')

    return biblioteca


def mostrar_libros(biblioteca):
    if biblioteca:
        print('Libros en la biblioteca:')
        for libro in biblioteca:
            print(f'- Título {libro['titulo'].capitalize()}, Autor: {libro['autor'].title()}, Año Publicación: {libro['año']}')
    else:
        print('No hay libros en la biblioteca.')


def buscar_libros_por_autor(biblioteca):
    control = True
    while control:
        autor=input('Dame el nombre del autor:').lower()
        if not autor:
            print('Ingrese el nombre de un autor')
        else:
            control = False
    libros_autor = [libro for libro in biblioteca if libro['autor'] == autor]

    # libros_autor =[]
    # for libro in biblioteca:
    #     if libro['autor'] == autor:
    #         libros_autor.append(libro)
    if libros_autor:
        print(f'Libros de {autor.title()}:')
        for libro in libros_autor:
            print(f'-Título: {libro['titulo'].capitalize()}, Año: {libro['año']}')
    else:
        print(f'No se han encontrado libros de {autor}.')


def eliminar_libro(biblioteca):
    control = True
    while control:
        titulo = input('Introduce el título a eliminar').lower()
        if not titulo:
            print('Introduce un título, el cmapo no puede estar vacío.')
        else:
            control = False
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            biblioteca.remove(libro)
            print('Libro eliminado con éxito.')
            return
        else:
            print('No se encontró el libro con el título especificado')


# Programa Principal

def gestionar_biblioteca(biblioteca):
    while True:
        clear_screen()
        print('''
        Menú de Opciones:
            1) Añadir
            2) Mostrar
            3) Buscar
            4) Eliminar
            5) Terminar
    ''')
        opcion = input('Seleccione una opción:')

        if opcion == '1':
            # pass
            clear_screen()
            anadir_libro(biblioteca)
            pause_screen()
        elif opcion == '2':
            clear_screen()
            mostrar_libros(biblioteca)
            pause_screen()
        elif opcion == '3':
            clear_screen()
            buscar_libros_por_autor(biblioteca)
            pause_screen()
        elif opcion == '4':
            clear_screen()
            eliminar_libro(biblioteca)
            pause_screen()
        elif opcion == '5':
            print('Terminando el programa')
            break
        else:
            print('Opción no contemplada')
            pause_screen()

biblioteca = []

gestionar_biblioteca(biblioteca)




