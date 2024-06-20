# Importamos las funciones de pause_screen y clear_screen del módulo screen.py
from libro.screen import pause_screen, clear_screen

# Importamos las clases Biblioteca (principal) y Libro (derivada)
from libro.libro import Biblioteca, Libro

# Declaramos la lista que contendrá los diccionarios correspondientes a los libros de la biblioteca
biblioteca = []

# Instanciamos miBiblioteca y mi_libro
# miBiblioteca = Biblioteca(biblioteca)
mi_libro = Libro(biblioteca)


# Programa Principal donde se muestra el menú de acciones de una biblioteca

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

    # Se llaman a los diferentes métodos correspondientes a la clase derivada Libro
    if opcion == '1':
        # pass
        clear_screen()
        mi_libro.anadir_libro()
        pause_screen()
    elif opcion == '2':
        clear_screen()
        mi_libro.mostrar_libros()
        pause_screen()
    elif opcion == '3':
        clear_screen()
        mi_libro.buscar_libros_por_autor()
        pause_screen()
    elif opcion == '4':
        clear_screen()
        mi_libro.eliminar_libro()
        pause_screen()
    elif opcion == '5':
        print('Terminando el programa')
        break
    else:
        print('Opción no contemplada')
        pause_screen()