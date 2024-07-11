# Fonaments de Programació (PDF)

## **¿Qué es programar?**

Programar: Programar és escriure instruccions  específiques perquè una máquina entengui,  processi i executi una sèrie de tasques.

Todos los procesos que hacemos “és programar”, entonces todo lo que hacemos en el ordenador lo es. Incluso las IA al calcular o al hacer busquedas en ellas, es programar, lo que lo hace muy rápido porque ya lo tienen codificado.

Quan parlem de màquines ens referim a  tots els “sistemes” que puguin processar informació (Ordinador, tablet,smartphone,  electrodoméstics,…)

Todo tiene sistemas de procesamiento. Un smartwatch es mucho más potente en unidades de procesamiento que un ordenador de la nasa de hace 30 años

## **Què és un llenguatge de programació?**

Un llenguatge de programació és un  llenguatge que ens permet comunicar-nos  amb una màquina i escriure programes  que permeti a aquesta interpretar les  nostres instruccions

Podem clasificar els **llenguatges** de  programació en **tres grans categories:**

### Llenguatge de máquina

![](https://lh7-us.googleusercontent.com/9bgxydomlggFP6zeA6uCdOad8EwkS9wateWGtTeFoOD98HmPbyATdU0aAhs82HsAbk5t0MOR9ypPV5xfGhSbiRw_FG6lEZ2HmwKa-RbEZjdMVFtfjC_bpaYC6mGH9qfbPWLwc_sW_aKYGngEia56S4k)

* Aquest tipus de llenguatge está escrit perquè sigui entés directament pel processador
* Lo que interpreta la máquina
* Les seves instruccions són cadenesbinaries (0 i 1), que indiquen les operacions i la direcció de memòria que es farà servir
* També podemprogramar fent servir codi hexadecimal que converteix allò que escribim en termes binaris perquè l’ordinador ho pogui entendre![](https://lh7-us.googleusercontent.com/kEXJYQRcTRuLSt5gaELNXBI5YL_qA0a0yFkuXF-LdEjzEtBtL56HcL9UjYV8UCVJNYhelitCt_SMwowLgbC8gZS4K29JDHN_pdhNbuD7SMoAFXfqCsxTNlMkRhDwCclfEt_-0ZmhD282Ylxgq7X3UiM)

![](https://lh7-us.googleusercontent.com/4zrbexxzlHPSSzu4Kbm2IPvhWFYgWotIqr-x0v6oVLnBklbD0gAclOig3z68RFHJs5vZjaPP5OmZcSlRCQ4DgO1TBGUydJW1_9wjYDMFTQcdcgnvfbvC87JpHm_XnddDwx1RBB2lXA43yXnlBpo5OCc)

**Ventajas:**

* Possibilitat de carregar (transferir un programa a la  memoria) sense la necessitat de traduir les  instruccions perquè l’ordinador les entengui.
* La velocitat d’execució és superior a qualsevol altre llenguatge de programació, porque no hay que traducirlo.

**Inconvenientes:**

* Els programes només s’executen al mateix procesador (CPU).
* Codificació més complexa i lenta.
* Dificultat per verificar i posar a punt els programes.

### Llenguatge de Baix Nivell

![](https://lh7-us.googleusercontent.com/eOPparvyjZHxP99-Kb2Jtm6RSN0r_oHPXE-bgtHexx-my0pcPircZ1AcB5yP5GBcF_9f7F-1pRzKxQKv4lyn3-YpdU3atoLx6_I8EpeEr3ODi4Rvl4vTKt90C4lHNfXfHTzQPZfh4w2gxv0mnR1UD3U)

* Són llenguatges que ensamblen grups de conmutadors necessaris per expresar una mínima lògica aritmètica (vinculats íntimament al hardware)
* En microprocesadores etc, el ordenador tampoco lo interpreta como tal
* 16 bits, Ensamblan conjunto de conmutadores
* Requereixen una fase de traducció al llenguatge máquina per poder ser executat directament per la computadora. (se necesita ensamblar)
* El llenguatge per excelencia és l’ensamblador. Les instruccions es coneixen com nemotècnics, per exemple:
  * Operacions aritmètiques: ADD (sumar), SUB (resta), DIV (división),…
* Actualment es fa servir en espais acadèmics o d’investigación, així com al treball amb micro-controladors (CMOS/BIOS) i electrónica (firmware).

**Ventajas:**

* Major velocitat de codificació
* Major velocitat de càlcul (una instrucción en un  llenguatge de Baix Nivell probablemente equival a una  instrucción en codi màquina

**Inconvenientes:**

* Dependència total de la máquina (programar en  llenguatge ensamblador en PC és diferente de  programar en Mac.
* Els programador estàn obligats a conèixer aspectes del hardware.

### Llenguatge d’Alt Nivell

En 1 sola linea puedes imprimir un hello word

![](https://lh7-us.googleusercontent.com/QIFWb5bs5atpBg67ljBfneyE9zGgzera4athBX1I7AVlRBzRW74QDkiQISql3Dq2wYE23NqySX4-tF3h11fZRK6l--K3c4b5QgNdLF37A6r4wWoeJR2WdKYSLgy9N39qPJvY0NuUrmehX5S_RM1KMPw)

![](https://lh7-us.googleusercontent.com/cv2446Arg8ZUJIQ7qTNouOKRxz6FYbHF_TLJChnM7xFClJ3lJTd7LjxRudppD_qbJ_P9J015Opz9dBi39OC87XHER941GEVgDJwFCskcZmeob3HbnIZOc6Bks1xyPuvjs2cEg7MYlFdv7qq615ucyqI)

* Cualquiera que se asemeja al inglés y luego el ordenador lo interpreta.
* Aquests llenguatges són els més utilitzats pels programadors, estan dissenyats perquè les persones escriguin i entenguin els programes d'un mode molt més fàcil que els llenguatges màquina i ensambladors.
* Los que usan programadores.

**Ventajas:**

* Independència de la máquina. Independiente del Sistema Operativo (SO).
* Processos o funcions previamente definides.  En entorno gráfico y hay definiciones ya preseteadas
* Temps d’aprenentatge relativamente més curt. (puede que sí, pero depende y puede ser largo el aprendizaje)
* Permeten més flexibilitat al desenvolupador.

**Inconvenientes:**

* No del todo real si trabajas bien con recursos de memoria
* No s’aprofita el 100% dels recursos de la máquina  en comparació amb els llenguatges anteriors.
* Augment de l’ús de memoria.
* Temps d’execució relativamente major (una línea  de codi equival a vàries línies de codi máquina). aunque es rápida

(Esta clase entra en teoría)

# Fundamentos de algoritmia (PDF)

## ¿Qué es un algoritmo?

Un algoritme és una seqüencia lógica de pasos a fer per poder resoldre un problema determinat

* A los programadores nos viene bien el papel y boli, porque tenemos que desarrollar algoritmos y cuantos más micropasos tengamos puede ser más facil de resolver un problema más grande.
* La algoritmia sirve para tener los pasos necesarios para resolver un problema.
* A mejor definido, mejor será nuestro código.

## Regles que han de cumplir els algoritmes

* Han de ser **precisos**: tenir un pasa pas lògic i puntual.
* Han de ser **definits**: l’algorismeté que comportar-se de la mateixaforma sempre.
* Han de ser **finits**: l’algorisme ha de tenirun nombre finit de pasos, té que acabar en un moment.

## Parts d’un algoritme

![](https://lh7-us.googleusercontent.com/Mjmxdd5vXlW6SfgzelqUU3etJCD6QXTyqdqA96Dv4sKak2Q2_ODuFodxpDIm_mjwsk3gAKLF_7Fxas7ob38GnybFBPKc7Xa1ZS8Zz3jdu4H_jWmRTVwAHbFQVhht4f1iF_NPGEw_7ZzXq3JSNHIow1Y)

* **Entrada**: correspona les dades que l’algorismerep.
* **Procés**: equivala les accionsque es realitzensobre les dades d’entrada.
* **Sortida**: el resultatde les accionssobre les dades d’entrada.

Ayer definiamos variables, asignamos entrada, procesos y al final una salida de datos

## Algoritmo de la vida diaria

* Aquest tipus d’algoritme és aquell que ens ajuda a resoldre problemes quotidians, i els fem sense donar-nos compte seguint una metodologia per resoldre’ls.

Ejemplo:

![](https://lh7-us.googleusercontent.com/wR4TOSBeayxq7RcwmKzafYd2JUlXB4fi2UsVdjlxeOB9t4da-fOBVN-M-hKeLTb42WHdIOsAkqy519wqRiFt1Bsb94DpC8SaRid_uySpaKEtVOec9v1ETfTZD1RXhuj1ehEqdT8mUmLxA1yDj4tdJIw)

Se podría añadir más procesos y sería mejor.

Puede haber más de una solución posible.

## Algoritmo computacional

* Els algorismes computacionals permeten definir els processos per donar solució a problemàtiques mitjançant operacions lògiques a un computador.
* Aquests a diferència dels anteriors han de ser desenvolupats seguint una **metodologia definida per a la solució de problemes.** (enfocamentde la solució, sintaxi…)

Al final los procesos van a ser bastante mecánicos

## Llenguatges algorítmics

* Defineixen la forma com ens comunicarem per mitjà d'algoritmes, amb l'objectiu que sigui la màquina la que ens entengui.
* Puedes tener errores que has de interpretar
* Els algoritmes es poden resoldre mitjançant l'aplicació de diferents tècniques, en aquest cas podem ressaltar **4 llenguatges** que ens permetran descriure els passos d'un algoritme de manera més detallada i estructurada (estos 3 más el de **progrmación**):
  * **Llenguatge Natural**
    * Aquest llenguatge ens permet descriure la seqüència lògica de passos d'una forma més natural, fem servir un vocabulari quotidià en descriure els passos de forma simple sense tecnicismes.![img](https://lh7-us.googleusercontent.com/9z0n_TzI2G9Hjs_eQpG5x0sdTggTqd07JXcaDBHPSGrCokxOGmIyYDzFgvH1GJzCvyG27Hg5DC_hwwbgJEiLddC_UHEpBs4lvzI_2xG1GjWYIjhCBQCQZqF8w3J70C7YVBNOr4M6_jGb74gwu-OazKA)
    * Introducir los datos, etc
  * **Diagrames de flux**
    * Representen els algorismes per mitjà de símbols que faciliten l'enteniment de la solució o el procés plantejat.
    * Diferentes simbolos con descripción:![img](https://lh7-us.googleusercontent.com/iXMFH_liCu6X1zg34CDUv2gfjqpRdPs1jewGZvZCiKxSCMOCdg4PuUKEwgQCmiO-SU-aRrmuEzOo4DTHxsezRF1UITG2qcaWItE7lAv9NbCwQnx0iAFQUPhACQaJ8j8OFhbhRVyC6TJ39uHAZTzvHak)

![](https://lh7-us.googleusercontent.com/hbVTcCehAl_aTZYSKUplqN8p_-jJ32mAVnfu3d7mVTtJoYWMYB_Wr9q3MgdM6d934c2ZeHCdsWtwg5eOZegme3X6cEGzQJVj8oqqMeYXV_tmOzqj5wotWUeN1mvXj6AqoIzG4BuAQYuNFAm-iMIOwmY)

* **Pseudocódigo**
  * El seudocodi compleix la mateixa funció però orientat a definir la solució d’un problema d'una forma més precisa i buscant definicions formals, generalment es fan servir per resoldre problemes mitjançant algoritmes computacionals.
  * El seudocodi ha de complir amb les següents característiques:
    * Ser precís i definit.
    * Evitar diverses interpretacions (ambigüitat). Evitar siempre ambiguedad
    * Fer servir termes formals però familiars al sentit comú.
    * Eliminar instruccions innecessàries.
  * Regles bàsiques:![](https://lh7-us.googleusercontent.com/MbXA1P0FHufIb8SOrXlVTYubE4oNgUTl1GFpIjY7f9jzrM0zrJxKWten4k60MnD3KTFDnLDxOz7xBZaRovjRduKfLaPm6ZaTA-dhwvX3jzg80r2ViebesOBzUkYu_RkhYCy2ZUjm8SJ4w7uF6N8Pm28)
  * Limitarem amb les paraules **INICIO** i **FINAL** l’algoritme.
  * Al final de sentència farem servir “;” (punto y coma)
  * Les **variables** les declararem abans de fer-les servir. Como el diagrama de flujo.
  * Tenim que indicar el tipus de dada de cada variable.

Al final de sentencia (en python no), se usa el punto y coma (como javascript etc)

## ¿Qué es una variable?

* Una variable és un contenidor que pot emmagatzemar informació i pot canviar en el temps, ja que el seu contingut pot variar.
  * ¡En Python una variable es una etiqueta a la que le asociamos a un tipo de dato!
* Per regla general, les variables les podem declarar amb un identificador i un tipus de dada que l’acompanya

![](https://lh7-us.googleusercontent.com/8LWQN1IHOXJpSw7iXondQ5GgyPJrAbHZG65spAHKyQY_dPCsAcvANZ6asg2-jMz2PPRsfoXwAAk-vV_nE7gg5oBp0paicDmzVwTUX2WW3WCxRn5Xo_GnX96tX-Ewm8NcJFNHR1qiXZmuXFYCpQYWWTA)

A ver, el tipo de dada serían los números (Enteros, reales…) o letras.

El identificador es el nombre que le damos a ese tipo de datos.

## ¿Cómo nombramos a una variable?

* El primer carácter ha de ser alfabètic(a…z, A..Z) o $.
* Després poden anar caràcters alfanumèrics.
* Els identificadors no poden ser paraules reservades del llenguatge.
* És molt recomanable fer servir la regla **camelCase**.

  * Tiene que empezar con una letra y ha de ser minúsicula.
  * Todas las siguientes palabras irán con la primera letra en mayúscula.
* No poden haver-hi espaisni signes de puntuació.

  * el guión bajo si se acepta como signo de puntuación
* La majoria de llenguatges són **case sensitive**.

  * El método en que escribes los nombres (identificadores) de las variables, atributos, métodos de clase y clases.
  * Ej.: camelCase

## ¿Que es un tipo de dato?

* Les variables corresponen a contenidors de memoria on enmagatzemem valors.
* Aquests valors estàn associats a un tipus de dada específica:
  * **Numéric** (sencer, decimal).
  * **Text** (un carácter o una cadena de caràcters).
  * **Lògic** (veritato mentida / SI o NO)

## Ejemplos de programaEn Python -> Las arrays no existen (matrices), pero si diccionarios etc

* Realitzarem amb llenguatge natural, diagrama de flux i seudocodi, un algoritme que faci la suma de 2 nombres i mostri el resultat.

  * Lenguaje natural![img](https://lh7-us.googleusercontent.com/204OTFcL0xifX26nTTPJgRG3CZz5frS1uYDiWcbRJQtbtz6F6ikEy2bUS0CRl3Kn1VuawibbG3WrotIKqIoNUJiunB9LYLR54Ypb_DLRGPOBZWSdXZqwKKtz3zp8aX9d19ax3M_T3Oyk1oeq8IYn1N4)
  * Diagrama de flujo

    * inicio, declaración, operaciones e imprimir resultado + fin
      ![img](https://lh7-us.googleusercontent.com/ZSsDl09OLK3L0hU-eCUwi05Cn7bdr8wqN47_s6MAGElRZbciBwQE4eVwIVigKy1jTl9ZAtZtm2s8GCtiAhJPAQVw4qW7jSWbp1nnWWIaNS_RWsbEE4NZjVrauhOqEAUsAt3Q2BxJmaxROvuM9g22bi8)
  * Pseudocódigo![img](https://lh7-us.googleusercontent.com/lsVjCuZAf4A6H5mTp9c_hojOgG0mmjRN8rGTCvS9BDDfEYdL3GDMLqM0OnN8KotDY9eF_RpVEyD-mTzmMCSogMZZD5Jy15VM0uYQDi_8oJW-J5KnS6jOP8_G_InUc9bjuX0VF9kbRFZzwvPhHdymOfo)
* Toda linea acaba en punto y coma.

## Prueba de escritorio EXAMEN*************

* Quanes realitzaun algoritme, l'ideal és verificar el procés per assegurar-nos que compleix allò que s'esperava, per això s'aplica una tècnica anomenada “Prova d'Escriptori”.
* La prova d'escriptori **consisteix en un seguiment pas a pas de l'execució de l'algorisme, per validar aquest procés, determinar quins són els valors pas a pas i verificar així el funcionament desitjat.**![](https://lh7-us.googleusercontent.com/FUg78xANEL3z9qMsc-mY9AaqnRPXIopGkKqHtC5qohkaihQM706bEk6hX1lD-DfbPoYXrGSBUU_bdYf8Ld5ovluzpG0-LFgVnhcIQ7SDPxN2xfw6bKGpDtE7VaOTEw8fuhdW7hjgy9ff0sxzITysOPI)

**	**Ej. Prueba escritorio —------>

Ejercicios:

Realitzar els següents algorismes:

* Escriure un programa que converteixi un valor donat en graus Fahrenheit a graus Celsius. Recordeu que la fórmula per a la conversió és:

  ````
  C = (F-32)*5/9
  ````

![](https://lh7-us.googleusercontent.com/os-FWpF4Jf4ClSRxpZgx_Fs7ZimsNbC0hVT2SGdm__iJl57eZqtrzhIi-pbfJ67cmCf1G81Fp-cmX9MuIghzYJ2-KnAp-4kE-fD5Rr0RLW1ebMDsvEsB8lARI_tl_CClcp9Gab55EgLG3JfaLcPTQxo)

* Calcular la mitjana de tres números demanats per teclat.

![](https://lh7-us.googleusercontent.com/xo8cLj4TVjxkcGcfXSHGx_0ZdsVF8A5dTZU7Botw8q7zWUoUqpP96O5RFyoIU3M3QDd9nThD9VNgEyOABzdf06qo11I7T_zPwcgYQFPOIvt-2K9FrMVxivHmlyFc2wVdqGyxWOzmFSFU4-_InTXX5gI)

* Realitza un programa que rebi una quantitat de minuts i mostri per pantalla a quantes hores i minuts correspon. Per exemple: 1000 minuts són 16 hores i 40 minuts.

![](https://lh7-us.googleusercontent.com/PVY4xJiAFkDTOe02ospMNWPU2hF2J6kNYR894tAqfaarm2tj0_rrSOOUd_TgqWDEkOkuROeA1iSeoJhJxCx4C_UQmF3fWJt_b6Lu3guMIhI8F70JRwQTQBgDGlW15EhgA_1I5MJa37BOgdL6yw8meUw)

* Un alumne vol saber quina serà la seva qualificació final en la matèria d'Algorismes. Aquesta qualificació es compon dels percentatges següents:

  * 55% de la mitjana de les tres qualificacions parcials.
  * 30% de la qualificació de l'examen final.
  * 15% de la qualificació d'un treball final.

![](https://lh7-us.googleusercontent.com/Wn0K7lmzLE9bqoqXxFbugubYH8bL8U7bBKmwfEh_-DXI5i48uB3m1mZc1rMS3xDunihkbJtwwwR_s7RyrAjdl-FqRMPh4GTO6nKKVgGlLfNsDuuWvPRRFa2fTwItyrIdZinfv5EGrwpIdoDuWPPJfRE)

![](https://lh7-us.googleusercontent.com/vsFAtywgf-BxxpEUIcrr2laNNvAtizK_UimsNVTc8Uhz1xIv6PFJqecim0avDajubS-PHVcIwkg7qgI4mKqY3Joc7ytwFPgn2c_Pm6MnxZgGO9ldqmD0nv6AwKG6u5zE-KHiVVEx_FClGaxPENx1_P0)

* Una botiga ofereix un descompte del 15% sobre el total de la compra i un client vol saber quant haurà de pagar finalment per la compra.

![](https://lh7-us.googleusercontent.com/UlE4LyI8ff_lv_foF8iClZj3t7Pq3_vJXKQqXFoZwAO9g83f6Y5KUBGAo-2EllHOFvpvuedaeFSapmsozlfeVGWMC3C4NuTmcqrdVBkAPCP0bjMB4SVqDhY48VjGNaU6Z7K8NBb-UoZs86aY72B5zw0)

![](https://lh7-us.googleusercontent.com/zQ5_8j9ljy-z1etBzHTugPmY8Q1A_eVSxGSxvgI2t_-cOUwsFA2Uyjlbxz-a6lsyoAwyWkvvy4TGrggKT7Q8Ibi7CSObS9Y8MeyMQ5aPf4hbsgUZ3dO700oPHQTEYQBBXRanzKQT0R7pVvLOXDoYN3I)

* Realitzar un algoritmes que llegeixi un número i que mostri la seva arrel quadrada i la seva arrel cúbica.

![](https://lh7-us.googleusercontent.com/2UUS4Pc-NMbDcg0mmUvRyjig9iYn-mevmVT-RgTJCBKUmBUrZkK8RTjixyAq7xBhNKdoD89JLjEzSaxOzSYADAPNR24JfiTDxb4ci3kzuadrdJzTcZi5EV8pXNLr4t1dfY-auFSgppYCfoRvW8wawO4)

Estructuras condicionales:

Hasta ahora, en estructura secuencial una orden va detrás de otra. Ahora queremos estructuras de control, donde se pueden tomar decisiones.

Condicionales simples:

**	**En lenguaje en C -> estructura “sweetcase”, en python no existe

**	**FlowGorithm no lo tiene tampoco

Se usa la herramienta de control Si

![](https://lh7-us.googleusercontent.com/9AiUY2lVsQ4RbvGGWeJTGkf7Ct2rFibWJzVg9QWXJVAuM5Xl7GhFhzshedomOvKwHzXxfm6VIoGDPB2LpIpu95aAgiuU5QFTuxFFpYlRwjcoZo7-aZ2cCmzBIo7Rk2g4pfagza-9PmGNhevZpfFwlHU)

**	**El resultado siempre será true o false, es un resultado boleano

![](https://lh7-us.googleusercontent.com/GtomjXPGF3Lfx1VDaXzzzcloiFIvygCG7zoviH-nMsG2-dL2ckVOU5FDyzEMnNuJ_llymZ3y0-zatOc7-6ovKhmLXH0oF8law8fxpwXwmB23aVb-hyfb8UA54P-4SNniyrQ2rU2BTL86Y-md9J8n2eE)

podemos poner <= a un número

Para comparaciones se usan los siguientes símbolos:

== igual a

<= menor o igual a

> = mayor o igual a

!= o <>  diferente

< menor que

> mayor que

con igual (=) estás asignando valor, no es igual a!

![](https://lh7-us.googleusercontent.com/oi98AI7xmLEuc4YJoS5pjWnXECVbBAzEdZ_sf_dgVZ60PS0tjNOvsJya2G1r3lKR1WMCoWeiEE5Fq1SkwcZkZ706g3A8q3bc19aVd9XQa15Cf6TBqr4W_MK1Sfh_AhE2-ti_TGyge7x8NhcvZXvKxP0)

Cumplir dos condiciones o más:

AND && : Se tiene que cumplir las dos condiciones

OR  || (alt gr + 1) : Se tiene que cumplir una u otra condición

![](https://lh7-us.googleusercontent.com/Sd0TnF9-0vaui--Zc44kbLn4bhejqQyty9h2NHa3Hr09pBNTiuzg7NDaOhyKqlGv4hyaeIliW9XhGpPJq0LhyVljZ_KmpXdg5vPiu8znuQhgGIJqfO7Fs2F4r_3retSw-AgqBsVbvpCOqXlvUWM12Ug)

Condicional anidado:

![](https://lh7-us.googleusercontent.com/g_f20KHgccYNMOvwVbA0tCBbFz7IywCYpb1H5KNRq5OpcWlBAm1M5B7T5CIIfCb9ZusWBIhW4ojGvygMYzNX6NfZd5XKwcAedeHfihF4KJUZmpPOXBTnTv7OWNntRKrR1vTv8JClnW4C4hKWGo9vg7s)

Esto sirve mucho para entrar en una cuenta, un control de usuario

Ejercicio:

Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no:

![](https://lh7-us.googleusercontent.com/FgV1EZltnzpM4jDAcczvcO_0lKkvclxhHsjqREMHMJNGVxIzb8YX8OVpMMeEdZlE0RsUxEJVIfaQhqA8rQxd8vxiixkmJIryKDTn2rft2iDXMilBCLN5v7GVoTC7wNAPaRVz4uNXExB0JarmNS52HdM)

Escribe un programa que lea un número e indique si es par o impar:

![](https://lh7-us.googleusercontent.com/iixMwwC2us6qXELhFc3TrKnzFpy_Ub6Y5Ug5F8ujcK1ngkP3i0KidL0Qi2J7u6ORQutmdQth-VKI_9ji61cOst-lTZhxnibki-8PaK8YxrMoR_UkqlZyu90wkd70D2R11WnXyK9sN17tqvOozpM7UXA)

Si es negativo, tenemos que dar otro condicional o da error.

![](https://lh7-us.googleusercontent.com/mtfSWOKT4wSXV2iWVcuibx9saWIEWGSHmeMLyFNM1Sy6p4A-nd27pfOQF2Ym96jRjZPLQ-p_waK6ZcCvp5a9iPlxFlzaLYv4Tf94s6BW4BpSbMyaWAE9PmJom68_Hcnu2WEVppR26GCyNKgJMe0oB-U)

para hacer número absoluto existe la función ABS(número) o abs ()

![](https://lh7-us.googleusercontent.com/LzRPcXRKs5gbFk9kAgWjf0vY0r-wYqkCFu5oD6ZwwXEeCI9ISIBEDMVLygDx_vj_lE8r3J0dyczpfPEsM5G6PRpGNqpQUB8DLbmSGtNTub-8VN3-EIyycvHSImlZpAddQGHI6Gw4Uprp-X3DDUwczTU)

Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

![](https://lh7-us.googleusercontent.com/h4DG6WNZGzIWV02iAvXAYNXkWaNqIo_jxqRLJ4OAsolwiJrvVaCkMnjmWSt4vnfzi6t5rMnxeV20dJ2EZknjo_iK8FyQ-xzcYlt_tld4F_M_Cc6RvrQ5RKVqBPl_WQmKTI2GaDi307SLp4MDpo98VSA)


---




# Estructuras condicionales

## Pràctica3. Estructures condicionals

Al ejecutarse la instrucción `si` se evalúa la condición lógica. Si la condición lógica es **Verdadera** se ejecutan de manera secuencial el bloque de instrucciones  *Salida...* . Si la condición es **Falsa** no se ejecuta el bloque de instrucciones. Una vez ejecutado el `si` (opción verdadera o falsa) se continúa la ejecución de forma secuencial por la siguiente instrucción, en caso de haberla.


## Operadores de comparación

| Operador | Descripción    |
| :------: | --------------- |
|    <    | Menor que       |
|    <=    | Menor o igual a |
|    >    | Mayor que       |
|    >=    | Mayor o igual a |
|    ==    | Igual           |
| != ó <> | Diferente       |

---


1. Desenvolupa els següents algorismes:* Escriu un programa que demani un número d'usuari i una contrasenya i si s'ha introduït “pepe” i “asdasd” s'indica “Has entrat al sistema”, sinó que dóni un missatge d'error.
   ![1715177475331](image/080524_Estructuras_condicionales/1715177475331.png)
2. Realitza un algorisme que calculi la potència, per això demana per teclat la base i l'exponent. Poden passar tres coses:

* L'exponent sigui positiu, només heu d'imprimir la potència.
* L'exponent sigui 0, el resultat és 1.
* L'exponent sigui negatiu, el resultat és 1/potència amb l'exponent positiu.

![1715181961388](image/080524_Estructuras_condicionales/1715181961388.png)

![1715177164238](image/080524_Estructuras_condicionales/1715177164238.png)

* 
* Algorisme que demani dos números 'nota' i 'edat' i un caràcter 'sexe' i mostri el missatge 'ACCEPTADA' si la nota és major o igual a cinc, l'edat és major o igual a divuit i el sexe és 'F' . En cas que es compleixi el mateix, però el sexe sigui 'M', heu d'imprimir 'POSSIBLE'. Si no es compleixen aquestes condicions s'ha de mostrar “NO ACCEPTADA”.

![1715177955894](image/080524_Estructuras_condicionales/1715177955894.png)

* Algorisme que demani tres números i els mostri ordenats (de major a menor)

![1715190048783](image/080524_Estructuras_condicionales/1715190048783.png)

![1715190070237](image/080524_Estructuras_condicionales/1715190070237.png)

mejora por si tienes números iguales: el 8 8 3 no me funciona

![1715191820575](image/080524_Estructuras_condicionales/1715191820575.png)

(pasar el bueno)

* El director d'una escola organitza un viatge d'estudis i requereix determinar quant ha de cobrar a cada alumne i quant ha de pagar a la companyia de viatges pel servei. La manera de cobrar és la següent: si són 100 alumnes o més, el cost per cada alumne és de 65 euros; de 50 a 99 alumnes, el cost és de 70 euros, de 30 a 49, de 95 euros, i si en són menys de 30, el cost de la renda de l'autobús és de 4000 euros, sense importar el nombre d'alumnes. Realitzeu un algorisme que permeti determinar el pagament a la companyia d'autobusos i el que ha de pagar cada alumne pel viatge.

  ![1715180408854](image/080524_Estructuras_condicionales/1715180408854.png)

  ![1715263412603](image/080524_Estructuras_condicionales/1715263412603.png)
* Escriviu un programa que demani un nombre enter entre un i dotze i imprimeixi el nombre de dies que té el mes corresponent.

![1715181426998](image/080524_Estructuras_condicionales/1715181426998.png)



---




# Estructura iterativas

3 tipos

![1715264505469](image/090524/1715264505469.png)

ciclos do o hacer

  Los otros dos no sabemos cuantas veces, dependen de una condición

## CICLO FOR: (o para)

Tenemos que usar una variable para la cantidad de veces del contador

**Sabemos cantidad de iteraciones que se van a realizar**

Dar valor inicial del contador ( 0 o 1)

Y el valor final 9 (si el primero era 0), para que haga 10 ciclos

puede ser de incrementar o decrementar

Funciones un número determinado de veces (iteraciones) que conocemos

Para hacer tabla mutiplicar, o para hacer operaciones un número de veces.

![1715264644226](image/090524/1715264644226.png)

Ejemplo valor inicial 1 hasta 10:

![1715264694967](image/090524/1715264694967.png)

## CICLO WHILE: (o mientras)

Aquí lo que establecemos es una condicion (numérica o no, como un boleano, letras...)

Ha de tener un control para parar el bucle (debajo de la salida), en este caso para que siga después del 1

no sabemos cuantas veces, dependen de una condición

![1715265265181](image/090524/1715265265181.png)

## Ciclo DO WHILE: (o hacer)

La orden se ejecuta como mínimo una vez

no sabemos cuantas veces, dependen de una condición

Primero haces una condición de verdadero o falso

usarlo para cuando las funciones del bucle como mínimo hayan de producirse 1 vez

![1715265658996](image/090524/1715265658996.png)

## WHILE vs DO while

en el while si no se cumple condición, no se va a producir.

En do while, todo y que variable inicial no cumpla condición si se produce el primer ciclo

# Ejercicios o Aplicaciones

Realizar un algoritmo que pida numeros (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

![1715269716665](image/090524_estructuras_iterativas/1715269716665.png)

Profe:

![1715269902729](image/090524_estructuras_iterativas/1715269902729.png)

Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

-Mio

![1715274376808](image/090524_estructuras_iterativas/1715274376808.png)

-Profe

![1715274981469](image/090524_estructuras_iterativas/1715274981469.png)

y para controlar los decimales:

![1715275275810](image/090524_estructuras_iterativas/1715275275810.png)

contador es el numero de datos que va introduciendo el usuario

while porque si el usuario te da un 0, no quiere que ejecute ningún cálculo

Si no pulsa 0, la suma se va acumulando junto al contador

Al poner 0, salta y evalua:

    -Primer resultado es 0

    -Si el primero no es 0, calcula la media

ToFixed convierte lo de dentro en una cadena "XXXX", para volver a un número real has de poner ToReal antes.

*Crea una aplicación que permita adivinar un número. La aplicación va a generar un número aleatorio del 0 al 100. A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. Además, los intentos que te quedan (tienes 10 intentos para acertarlo). El programa temina cuando se acierta el número (además te dice cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

    función Random (101), para generar un número aleatorio del 0 al 100 (es decir, entre 0 y el número que le demos, menos 1)

-Mio

![1715350175857](image/090524_estructuras_iterativas/1715350175857.png)

![1715350195764](image/090524_estructuras_iterativas/1715350195764.png)

Se puede optimizar el mío

-Profe

![1715349314575](image/090524_estructuras_iterativas/1715349314575.png)

    segunda versión en el mobil (pasarlo)

10/05/24

Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario

![1715353457753](image/090524_dia10_estructuras_iterativas/1715353457753.png)

![1715360313946](image/090524_dia10_estructuras_iterativas/1715360313946.png)

![1715355191430](image/090524_dia10_estructuras_iterativas/1715355191430.png)

-profe:

![1715362274538](image/090524_dia10_estructuras_iterativas/1715362274538.png)

    para negativos lo duplicas y pones valores absoultos y, al final multiplicas por -1

esta disposición del codigo es aurea, y es elegante! Algo fundamental para una empresa

Ejercicio extra:

*Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado

![1715371048440](image/090524_Más_dia10_estructuras_iterativas/1715371048440.png)


# Estructuras iterativas

Las estructuras iterativas (también llamadas estructuras repetitivas, ciclos o bucles), nos permiten ejecutar una serie de instrucciones un número determinado de veces o bien mientras se cumple determinada condición.

## Ciclo FOR o PARA

![1715584226551](image/03_estructuras_iterativas/1715584226551.png)

La instrucción `Para` ejecuta una secuencia de instrucciones un número determinado de veces.

![1715584348778](image/03_estructuras_iterativas/1715584348778.png)

* Al ingresar al bloque, la variable `contador` recibe el `valor inicial` y se ejecuta la secuencia de instrucciones que forma el cuerpo del ciclo.
* Luego se incrementa la variable `contador` en `paso` unidades y se evalúa si el valor almacenado en `contador` superó al `valor final`.
* Si esto es falso se repite hasta que `contador` supere a `valor final`.
* Por defecto, el Paso es de a `1` y la dirección `Incrementar`. Podemos modificar el paso según lo necesitado y la dirección a `Decrementar`.

## Ciclo WHILE o Mientras

![1715584527393](image/03_estructuras_iterativas/1715584527393.png)

La instrucción `Mientras` ejecuta una secuencia de instrucciones mientras una condición sea verdadera.

* Al ejecutarse esta instrucción, la condición es evaluada. Si la condición resulta verdadera, se ejecuta una vez la secuencia de instrucciones que forman el cuerpo del ciclo. Al finalizar la ejecución del cuerpo del ciclo se vuelve a evaluar la condición y, si es verdadera, la ejecución se repite. Estos pasos se repiten mientras la condición sea verdadera.
* Se puede dar la circunstancia que las instrucciones del bucle no se ejecuten nunca, si al evaluar por primera vez la condición resulta ser falsa.
* Si la condición siempre es verdadera, al ejecutar esta instrucción se produce un ciclo infinito. A fin de evitarlo, las instrucciones del cuerpo del ciclo deben contener alguna instrucción que modifique la o las variables involucradas en la condición, de modo que ésta sea falsificada en algún momento y así finalice la ejecución del ciclo.

## Ciclo DO WHILE o Hacer

![1715584650668](image/03_estructuras_iterativas/1715584650668.png)

La instrucción `Hacer` ejecuta una secuencia de instrucciones hasta que la condición sea verdadera.

* Al ejecutarse esta instrucción, la secuencia de instrucciones que forma el cuerpo del ciclo se ejecuta una vez y luego se evalúa la condición. Si la condición es falsa, el cuerpo del ciclo se ejecuta nuevamente y se vuelve a evaluar la condición. Esto se repite hasta que la condición sea verdadera.
* Hay que tener en cuenta que, dado que la condición se evalúa al final, las instrucciones del cuerpo del ciclo serán ejecutadas al menos una vez.
* Además, a fin de evitar ciclos infinitos, el cuerpo del ciclo debe contener alguna instrucción que modifique la o las variables involucradas en la condición de modo que en algún momento la condición sea verdadera y se finalice la ejecución del ciclo.


---



# Estructuras de datos

Las matrices en python no existen, están en un modulo externo y se tienen que importar.

## Una Array / Matriz / Arreglo

Si tenemos que almacenar unos nombres dentro de una variable (en una clase)

 Sería tal que:

- alumno1
- alumno2
- alumno3...
- alumnoN

-**Array es una estructura que puede almacenar tantos datos como queramos.** Tiene un valor tal que:

array [valor1, valor2, valor3... valorN]

    El valor puede ser entero, real cadena de caracteres o boleano, pero siempre el mismo tipo de dato (no en todos los lenguajes).

-Tiene siempre un í**ndice que empieza siempre por 0, que corresponde al valor 1, el índice del ultimo valor será la longitudArray-1**

## Ejemplos

![1715695127697](image/140524_Matrices/1715695127697.png)

nombre variable, tipo de dato + matriz y tamaño

![1715695258385](image/140524_Matrices/1715695258385.png)

nombre variable y entre corchetes el nombre del índice

![1715695268464](image/140524_Matrices/1715695268464.png)

![1715695296047](image/140524_Matrices/1715695296047.png)

![1715695463904](image/140524_Matrices/1715695463904.png)

Consola nos da:

![1715695493776](image/140524_Matrices/1715695493776.png)

## La función PARA junto a las Array

La función PARA es de vital importancia para leer una array si es muy larga:

![1715695742081](image/140524_Matrices/1715695742081.png)

Tienes que tener una variable contador declarada antes, para hacer el bucle y poder representar los valores dentro del array.

![1715695788496](image/140524_Matrices/1715695788496.png)

Array para introducir datos:

![1715695952097](image/140524_Matrices/1715695952097.png)

declarar la variable del numero total de la matriz

![1715696051633](image/140524_Matrices/1715696051633.png)

![1715695942272](image/140524_Matrices/1715695942272.png)

![1715696100320](image/140524_Matrices/1715696100320.png)

## Para guardar una array

Ahora falta iniciar cada uno de los indices:

    para ello tendremos la variable contador, en la salida le tenemos que poner contador +1(para que el usuario lo vea), ya que el contador que vale 0 es el alumno 1, e indice de la Array = 0!

![1715696571856](image/140524_Matrices/1715696571856.png)

Ayuda -> documentación tienes las -> funciones intrinsecas -> Size () , para saber la cantidad de datos que tiene el array

    Size () , para saber la cantidad de datos que tiene el array, o la longitud de la misma array

Ahora recorremos de nuevo la array:

![1715697028844](image/140524_Matrices/1715697028844.png)

![1715697413422](image/140524_Matrices/1715697413422.png)

 **el segundo bucle recorre la array**  y te printa el alumno con el índice.

## Ejercicios:

*Realizar un programa que defina un vector llamado "vector_numero" de 10 enteros, a continuación lo inicialice con valores aleatorios ( del 1 al 10) y posteriormente muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.

- mio

![1715699418302](image/140524_Matrices/1715699418302.png)

- Profe

![1715699613999](image/140524_Matrices/1715699613999.png)

* Se requiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno ( comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

![1715705086225](image/140524_Matrices/1715705086225.png)

![1715705103061](image/140524_Matrices/1715705103061.png)

- Profe

![1715705967755](image/140524_Matrices/1715705967755.png)

![1715705984221](image/140524_Matrices/1715705984221.png)

![1715706000042](image/140524_Matrices/1715706000042.png)

*Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. Copia los elemenos del vector en otro vector pero en orden inverso, y muestralo por pantalla.

![1715709723880](image/140524_Matrices/1715709723880.png)

![1715709736451](image/140524_Matrices/1715709736451.png)

*Programa que declare un vector de diez elementos enteros y pida números para rellenarlo hasta que se llene el vector o se introduzca un número negativo. entonces se debe imprimir el vector (sólo los elementos introducidos)

![1715718750586](image/140524_Matrices/1715718750586.png)

![1715780859452](image/140524_Matrices/1715780859452.png)

![1715780875934](image/140524_Matrices/1715780875934.png)

 Con este cambio usando el -1 me evito de que salga el número negativo. Aún así no es recomendable usar el PARA, sólo usarlo en numero determinado de iteraciones.

-Profe

![1715781735948](image/140524_Matrices/1715781735948.png)

*Hacer un programa que inicialice un vector de números (10 enteros) con valores aleatorios, y posteriormente ordene los elementos de menor a mayor.

![1715788381402](image/140524_Matrices/1715788381402.png)

![1715788405569](image/140524_Matrices/1715788405569.png)

*Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco ( " * " ). Al finalizar se mostrará los siguientes datos:

    -Todos los alumnos mayores de edad.

    -El alumno mayor (el que tiene más edad)

![1715796346115](image/140524_Matrices/1715796346115.png)

![1715796364577](image/140524_Matrices/1715796364577.png)

![1715796382410](image/140524_Matrices/1715796382410.png)



# Estructuras de datos

Hasta ahora, para hacer referencia a un dato utilizábamos una variable. El problema se plantea cuando tenemos gran cantidad de datos que guardan entre sí una relación. No podemos utilizar una variable para cada dato.

Para resolver estas dificultades se agrupan los datos en un mismo conjunto, estos conjuntos reciben el nombre de  **estructura de datos** .

## Arregos o arrays

Un array (o arreglo) es una estructura de datos con elementos homogéneos, del mismo tipo, numérico o alfanumérico, reconocidos por un nombre en común. Para referirnos a cada elemento del array usaremos un índice (empezamos a contar por 0).

## Declaración de un array

![1715856893736](image/04_estructuras_de_datos/1715856893736.png)

Asignaremos un nombre al array, el tipo de dato que vamos a tratar, y su tamaño (longitud o dimensión).

## Acceso a los datos del array

Para acceder a cada uno de los datos de un array, usaremos su índice encerrado entre corchetes "[]": `nombreArray[indice]`

Para acceder a todos los elementos de un array, podemos hacer uso de un bucle (el ideal es el bucle **PARA** o **FOR**).

Como el índice de un array siempre empieza por el número "0", la última posición siempre será la longitud del array menos 1.

Ejemplo:

![1715857175758](image/04_estructuras_de_datos/1715857175758.png)

En este caso podemos observar lo siguiente:

* Declaramos un array de cadenas de carácteres con una longitud de 3 elementos.
* Inicializamos manualmente cada uno de los elementos del array, accediendo por su índice.
* Declaramos un contador para el bucle FOR.
* Recorremos el array empezando por la posición 0 (primer índice) hasta la posición 2 (longitud 3, restamos 1).

![1715857366167](image/04_estructuras_de_datos/1715857366167.png)



---




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



# Programación estructurada (funcional)

La programación estructurada (modular o funcional) es un paradigma de la programación orientado a mejorar la claridad, la calidad y el tiempo de desarrollo de un programa o algoritmo, usando subrutinas (funciones o procedimientos) y tres estructuras: secuencial, condicional e iterativa.

Este paradigma de la programación consiste en dividir un programa entero en módulos o subprogramas para hacerlo más legible y manejable.

Cuando aplicamos programación modular, un problema complejo lo dividimos en diversos subproblemas más simples, y éstos a su vez en otros más simples todavía.

Además, el hecho de usar subrutinas nos permite reulitzar código y no tener que repetirlo infinidad de veces.

## Tipos de subrutinas

Tenemos dos clases de subrutinas:

* Funciones: una subrutina que devuelve un valor.
* Procedimientos: una subrutina que devuelve ningún resultado.

Cada una de ellas tiene dos fases de ejecución: definición y llamada.

Para poder hacer uso de una subrutina, primero ésta tiene que estar definida. Es la parte en la que definimos todas las acciones que va a llevar a cabo.  La segunda fase, la llamada, es cuando vamos a decirle que ejecute las acciones que hemos definido.

## Parámetros y argumentos

Tanto las funciones como los procedimientos pueden llevar argumentos o parámetros, y aunque son prácticamente lo mismo, conviene diferenciarlos:

* Parámetros: son las variables que recibe la función y se crean cuando la definimos. Su contenido lo reciben cuando llamamos a la función con los argumentos.
* Argumentos: son las expresiones que usamos cuando llamamos a la función.

## Scope o ámbito de las variables

Las variables definidas dentro de una función no existen en otras funciones o el programa principal. De la misma forma, las variables del programa principal no existen dentro de la función. (Nota: aunque ésto no es del todo cierto en algunos lenguajes de programación como JavaScript).

## Ejemplos:

### Procedimiento sin parámetros

![1716301540488](image/05_programacion_estructurada/1716301540488.png)![1716301553234](image/05_programacion_estructurada/1716301553234.png)

### Procedimiento con parámetros

![1716301591023](image/05_programacion_estructurada/1716301591023.png)![1716301603055](image/05_programacion_estructurada/1716301603055.png)

### Función con parámetros

![1716301639043](image/05_programacion_estructurada/1716301639043.png)![1716301651904](image/05_programacion_estructurada/1716301651904.png)


---
