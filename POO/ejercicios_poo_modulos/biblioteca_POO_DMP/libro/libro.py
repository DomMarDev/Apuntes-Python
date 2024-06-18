# Voy a tener dos clases: la primera de ellas será Biblioteca y será la principal, la segunda será una clase derivada a la que he llamado Libro 
class Biblioteca:
        '''Clase Biblioteca:
            - Es la clase principal de Libro.
            - Recibe la lista biblioteca del menú principal como atributo.
            - Contiene : método __init__ con parámetros self y biblioteca 
        '''
        def __init__(self, biblioteca):
            self.biblioteca = biblioteca        
    

class Libro(Biblioteca):
    '''Clase Libro:
        - Es la clase derivada de Biblioteca.
        - Se encuentran definidos los métodos necesarios para gestionar la biblioteca de forma simple.
        - Contiene: 
            * método __init__ con parámetros self y biblioteca
                * función super() para llamar el métido __init__ de la clase Biblioteca
            * método anadir_libro
            * método mostrar_libros
            * método buscar_libros_por_autor
            * eliminar_libro'''
    def __init__(self, biblioteca):

        super().__init__(biblioteca)      

    def anadir_libro(self):
        '''Método para añadir libros en la biblioteca:
            
            Se solicita al usuario:
                - Título del libro
                - Autor del libro
                - Año de publicación del libro
            
            Se aplica control de entrada para cada uno de los datos pedidos al usuario.

            Se retorna la lista (biblioteca) de diccionarios con el último libro añadido por el usuario.
                - Se usa el método .append()
        '''
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
            
        self.biblioteca.append({'titulo' : titulo, 'autor' : autor, 'año' : anyo})

        print('Libro introducido con éxito')

        return self.biblioteca
    
    def mostrar_libros(self):
        '''Método para mostrar los libros de la biblioteca:
                        
            Se recorre la lista de diccionarios (biblioteca) y se muestran todos los libros de esta.
            Se usa un bucle for para recorrer la lista.
            Si no hay libros en la lista biblioteca retorna el mensaje 'No hay libros en la biblioteca.'
        '''
        if self.biblioteca:
            print('Libros en la biblioteca:')
            for libro in self.biblioteca:
                print(f'- Título {libro['titulo'].capitalize()}, Autor: {libro['autor'].title()}, Año Publicación: {libro['año']}')
        else:
            print('No hay libros en la biblioteca.')


    def buscar_libros_por_autor(self):
        '''Método para buscar libros en la biblioteca dado un autor:
            
            Se muestra al usuario la lista de libros (o no) con el método mostrar_libros

            Se solicita al usuario:
                - Autor del libro
            
            Se aplica control de entrada para cada uno de los datos pedidos al usuario.

            Si hay libros del autor se recorre la lista de diccionarios (biblioteca) y se printan todos aquellos libros del autor especificado.
                - Se usa un bucle for para ello.

            Si no hay libros del autor introducido, se retorna el mensaje 'No se han encontrado libros del autor.'
        '''
        self.mostrar_libros()

        control = True
        while control:
            autor=input('Dame el nombre del autor:').lower()
            if not autor:
                print('Ingrese el nombre de un autor')
            else:
                control = False
        libros_autor = [libro for libro in self.biblioteca if libro['autor'] == autor]

        if libros_autor:
            print(f'Libros de {autor.title()}:')
            for libro in libros_autor:
                print(f'-Título: {libro['titulo'].capitalize()}, Año: {libro['año']}')
        else:
            print(f'No se han encontrado libros de {autor}.')


    def eliminar_libro(self):
        '''Método para eliminar libros de la biblioteca dado un título de libro:
            
            Se muestra al usuario la lista de libros (o no) con el método mostrar_libros

            Se solicita al usuario:
                - Título del libro
            
            Se aplica control de entrada para cada uno de los datos pedidos al usuario.

            Se retorna la lista (biblioteca) de diccionarios sin el libro borrado por el usuario.
                - Se usa un bucle y un condicional for para ello.
                - Se usa el método .remove()

            Si no hay libros del autor introducido, se retorna el mensaje 'No se encontró el libro con el título especificado.'
        '''       
        self.mostrar_libros()
        
        control = True
        while control:
            titulo = input('Introduce el título a eliminar').lower()
            if not titulo:
                print('Introduce un título, el cmapo no puede estar vacío.')
            else:
                control = False
        for libro in self.biblioteca:
            if libro['titulo'] == titulo:
                self.biblioteca.remove(libro)
                print('Libro eliminado con éxito.')
                return
            else:
                print('No se encontró el libro con el título especificado')

