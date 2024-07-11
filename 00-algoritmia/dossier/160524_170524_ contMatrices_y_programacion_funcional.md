No haremos matrices de dos dimensiones porque flowgorithm no deja.

29 de mayo teoria y 30 práctica avaluación final módulo de intro a la programación

# Programación Funcional

Paradigma de la programación.

Crear subrutinas de un programa para poder reutilizar-las.

    Por ejemplo, tenemos la función o subrutina multiplicar y la vas llamando para cuando quieras multiplicar

## Procedimientos y Funciones

**Procedimiento:** nunca retornan un valor.

**Función**: siempre retorna un valor. a una determinada llamada

    A nivel práctico siempre se llama a todo función.

**Ambas:**

    - pueden llevar argumentos o variables con un valor que les vamos a insertar. No es obligatorio que lo tengan

    - Tienen**dos partes:**

    **Definición:** puedes llamar a parámetros

    **Invocación:** le pasas a la función los argumentos.

    parametros y argumentos es lo mismo, solo que el parámetro 		  pasado a función es el argumento. Son variables

Los argumentos se pueden pasar por valor o referencia:

    Como valor le pasas un número, cadena o lógico

    Como referencia le pasas una variable, que tiene un valor dentro

## Ejemplos Parámetros y Funciones

En flowgorithm:

![1715867315597](image/160524_contMatrices_y_programacion_funcional/1715867315597.png)

![1715867326892](image/160524_contMatrices_y_programacion_funcional/1715867326892.png)

Procedimiento sin parámetro

![1715867375593](image/160524_contMatrices_y_programacion_funcional/1715867375593.png)

![1715867389415](image/160524_contMatrices_y_programacion_funcional/1715867389415.png)

[Para python todo son objetos y, por tanto , la programación se hace orientada a objetos.]

Hasta ahora tenemos subrutinas:

 ![1715867690010](image/160524_contMatrices_y_programacion_funcional/1715867690010.png)

hacemos una salida:

![1715867730681](image/160524_contMatrices_y_programacion_funcional/1715867730681.png)

ahora vamos a principal:

![1715867817497](image/160524_contMatrices_y_programacion_funcional/1715867817497.png)

 el parentesis vacio sirve para:

    Si encontramos a un nombre reservado, va a ser una función o metodo. Si el parentesis está vació va a ser un metodo o función.

![1715867864969](image/160524_contMatrices_y_programacion_funcional/1715867864969.png)

Lo ejecutamos y te muestra el mensaje que habiamos puesto en la salida del mostrarMensaje.

Esto lo guardo y lo llamo "procedimiento sin parametros".

Abrimos uno nuevo procedimiento con parametros:

![1715868248937](image/160524_contMatrices_y_programacion_funcional/1715868248937.png)

El primer parametro será primer argumento y así consecutivamente, ya que el nombre de parámetro (podrías poner el nombre tal cual, pero se usa uno acortado)

![1715868356229](image/160524_contMatrices_y_programacion_funcional/1715868356229.png)

Hacemos función:

![1715868553112](image/160524_contMatrices_y_programacion_funcional/1715868553112.png)

El orden tiene que ser el mismo al que hemos puesto antes. Simplemente le estamos poniendo una etiqueta

Como ningun retorno y aceptar

![1715868656888](image/160524_contMatrices_y_programacion_funcional/1715868656888.png)

Vamos a principal y le das a play

![1715868694873](image/160524_contMatrices_y_programacion_funcional/1715868694873.png)

**Hay que tener en cuenta el ambito de las variables o scope del locke:**

* Una variable sólo existe dentro de la función, no está en el principal.
* Una variable declarada en la función principal sóo está en esta.

No siemrpe es así, pero sí por defecto.

**Una vez la función se deja de ejecutar esa variable no existe.**

La edad tiene ambito en la principal, pero no en la función y al inreves.

Lo guardo como procedimiento con parametros.

Ahora mismo programa, pero en vez de ser procedimiento será una función, por lo tanto retorna un valor:

![1715869191194](image/160524_contMatrices_y_programacion_funcional/1715869191194.png)

En edad vamos a almacenar el resultado de calculo de edad.

Ahora hacemos función

![1715869322266](image/160524_contMatrices_y_programacion_funcional/1715869322266.png)

Aqui si retorno, edad

![1715869355674](image/160524_contMatrices_y_programacion_funcional/1715869355674.png)

Volvemos a principal

![1715869406325](image/160524_contMatrices_y_programacion_funcional/1715869406325.png)

El amito local tiene la funcion edad de la funcion

El ambito principal de edad se encuentra en el la funcion principal

Lo que estamso haciendo es dividir el procedimiento en procesos más pequeños, por lo que si una función de estas falla el programa no deja de funcionar, pero el resto de programa si va a funcionar.

Lo guardo como función como parámetros

## **Ejercicios**

*Crear un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función esMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

-Con retorno

![1715870620965](image/160524_contMatrices_y_programacion_funcional/1715870620965.png)

![1715870637402](image/160524_contMatrices_y_programacion_funcional/1715870637402.png)

Ahora sin retorno:

![1715871967145](image/160524_contMatrices_y_programacion_funcional/1715871967145.png)![1715871832857](image/160524_contMatrices_y_programacion_funcional/1715871832857.png)

 -Profe:

![1715872574531](image/160524_contMatrices_y_programacion_funcional/1715872574531.png)![1715872586740](image/160524_contMatrices_y_programacion_funcional/1715872586740.png)

*Crear una función que calcule la temperatura media de un dia a partir de dos valores (temperatura máxima y temperatura mínima). Crear n programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

-Mio

![1715874257418](image/160524_contMatrices_y_programacion_funcional/1715874257418.png)![1715874270296](image/160524_contMatrices_y_programacion_funcional/1715874270296.png)

-Profe:

![1715879147856](image/160524_contMatrices_y_programacion_funcional/1715879147856.png)![1715879161393](image/160524_contMatrices_y_programacion_funcional/1715879161393.png)

*Crea una función "calcularMaxMin" que recibe una array con valores númerico y devuelve el valor máximo y el mínimo. Crea un programa que llene el array con números aleatorios y muestre el máximo y el mínimo, utilizando la función anterior.

![1715882599176](image/160524_contMatrices_y_programacion_funcional/1715882599176.png)![1715882859058](image/160524_contMatrices_y_programacion_funcional/1715882859058.png)

170524

-Profe

![1715953509099](image/160524_170524_contMatrices_y_programacion_funcional/1715953509099.png)![1715953583944](image/160524_170524_contMatrices_y_programacion_funcional/1715953583944.png)


*Escribir dos funciones que permitan calcular:

    -La cantidad de segundos en un tiempo dado en horas, minutos y segundos.

    -La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas, minutos y segundos o salir del programa.

-Mio

![1715957123352](image/160524_170524_contMatrices_y_programacion_funcional/1715957123352.png)

![1715957208262](image/160524_170524_contMatrices_y_programacion_funcional/1715957208262.png)![1715957384618](image/160524_170524_contMatrices_y_programacion_funcional/1715957384618.png)

![1715957220646](image/160524_170524_contMatrices_y_programacion_funcional/1715957220646.png)![1715957247142](image/160524_170524_contMatrices_y_programacion_funcional/1715957247142.png)


Otra versión:

![1715958206481](image/160524_170524_contMatrices_y_programacion_funcional/1715958206481.png)![1715958220660](image/160524_170524_contMatrices_y_programacion_funcional/1715958220660.png)![1715958233461](image/160524_170524_contMatrices_y_programacion_funcional/1715958233461.png)


Profe:

![1715960003627](image/160524_170524_contMatrices_y_programacion_funcional/1715960003627.png)![1715960017667](image/160524_170524_contMatrices_y_programacion_funcional/1715960017667.png)![1715960030975](image/160524_170524_contMatrices_y_programacion_funcional/1715960030975.png)


Con Int() le quitas los decimales al número de dentro.
