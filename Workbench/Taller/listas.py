#*******************************************************************
#*                                                                 *
#*            TEORIA LISTAS - TUPLAS - DICCIONARIOS - ETC          *
#*            C O L E C C I O N E S   Y   MUCHO MAAASSSS           *
#*******************************************************************

# Una LIST, es un objeto, es una colección de cosas, pueden ser tareas,
# vegetales, nombres, mercaderías, cualquier cosa.

# Dos formas para declararlas o iniciaizarlas, aunque hay otras.

# 1) Defino una variable y le asigno un tipo lista VACÍO con paréntesis
empty_list1 = list()     # Note que se debe indicar el tipo lista o lo 
print (empty_list1, "esta es la lista 1 con '()'") # considerará una TUPLA
print (type(empty_list1))

# 2) Defino una variable y sé que es del tipo lista por los corchetes '[]'
empty_list2 = []         # A la variable se le asigna una lista vacía con
print (empty_list2, "esta es la lista 2")  # CORCHETES 
print (type (empty_list2))

# Ejemplo 1
numbers = [1,2,3,4,5,6] # Lista de números
print("'numbers' es del tipo ", type(numbers)) # Imprime un texto + su 'type'

# Ejemplo 2
groceries = ["tomato", "carrot", "letuce"] # Una lista con 3 str de 'vegetales'
print (groceries [0])  # El índice va con [] y parte en 0, imprime "tomato"
print (numbers [3])    # Es 'la' COLECCION, imprime todos sus elementos 
print (len(groceries)) # LEN devuelve el largo de la lista con len, retorna 3

# Ejemplo 3
lastname = "Cordova" # Variable de tipo string, contiene "Cordova" 
mix_of_data_types_list = [1, "Jota", lastname, 2+5, 1-3j, 3.14] # Lista con distintos tipos de var 
print ("'mix_of_data_types_list' es del tipo-", type(mix_of_data_types_list)) # devuelve un 'list' 
                                                        
# Podemos almacenar cualquier 'mix' de datos u objetos, en Python TODO es un objeto

# Ejemplo 4
listadeletras = []                # Crea un objeto list llamado listadeletras vacío
for unaletra in "paralelepipedo": # Define una var 'unaletra' y recorre el string "paralelepípedo"
    listadeletras.append(unaletra)# Agrega cada caracter del string a 'listadeletras' usando el método 'append'
print (listadeletras)             # Imprime los valores de la lista que son los caracteres de la palabra 'paralelepípedo'', lo que sea
                                  # Salida esperada ['p', 'a', 'r', 'a', 'l', 'e', 'l', 'e', 'p', 'í', 'p', 'e', 'd', 'o']

# Ejemplo 5
# Crear una lista de 4 elementos y, para cada elemento, calcularle su potencia de 2, usando 
# el método tradicional, eso seria así, luego veremos con expresiones o por comprensión:
# Alternativa 1
lista_potencias = []            # Crea una lista llamada "lista_potencias"
for i in range(4):              # Ciclo for para recorrer lista de 4 elementos, va de 0 a 3, el índice lo llamamos "i"
    lista_potencias.append(i**2)# La lista "lista_potencias", la voy poblando con el dato calculado.
print(lista_potencias)          # Imprime los 4 valores almacendaos en la lista [0, 1, 4, 9]

# Ejemplo 6
# El ejemplo 5, usando listas por comprensión (es decir, fórmulas o expresiones), seria así:
lista_potencias2 = [i**2 for i in range(4)]                   # Usa un FOR
print ("Esta es la lista de potencias Nr2", lista_potencias2) # Imprime [0, 1, 4, 9]

# Ejemplo 7
# Lista con las potencias de 2 de los primeros 10 números, método tradicional:
# Alternativa 1
lista1_pot10_2 = []                # Creamos un objeto lista vacio []
for num in range (0, 11):          # Incluye el 1ro, pero no el últimmo. Recorremos el rangoUsando un ciclo FOR usando la var "num" en el tramo de 0-10, ambos incluidos
    lista1_pot10_2.append (num**2) # Llenamos la lista con potencias PARTIENDO DE 0, a 10 (11-1) 
print(lista1_pot10_2)              # Salida por pantalla [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Alternativa 2
# Usando listas por comprensión, seria así:
lista2_pot10_2 = [num2**2 for num2 in range(0, 11)] #Creamos la lista con los valores según condición
print("Aquí usamos una expresión para crear la lista de 10 nros. y sus potencias",lista2_pot10_2)
# R=> Aquí usamos una expresión para crear la lista de 10 nros. y sus potencias [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Con este método, es más simple modificar los elementos que van a la lista.

# Ejemplo 8
# Este ejemplo muestra como operan las posiciones en una lista (cada elemento es una posX)
lista = ["pos0", "pos1", "pos2", "pos3", "pos4", "pos5"]
print("Esta es la lista:\n", lista, "\n")
print("1° Mostrar 'lista[2:5]', significa la pos2, pero excluye la 5, ojo!\n", lista[2:5])  # tomamos del 2 al 5 (sin incluir el 5)
print("2° Mostrar 'lista[4:]', significa desde la pos4 hasta la última\n",lista[4:])  # tomamos del 4 hasta el final
print("3° Mostrar 'lista[:2]', significa desde el BOF hasta la pos2, excluye la pos2\n", lista[:2])  # tomamos desde el principio hasta el 2 (sin incluir)
print("4° Mostrar 'lista[1:6:2]', significa 1 por medio, desde la pos1, incluye la 5\n", lista[1:6:2]) # tomamos 1 de cada 2 elementos desde el 1 hasta el 6 (sin incluir)
print("5° Mostrar 'lista[4:1:-1]', significa orden desc de la pos4 a la 2, excluye la pos1",lista[4:1:-1])
print("6° Mostrar 'lista[:]', significa mostrar todos los elementos de la lista\n",lista[:])  # tomamos desde el principio hasta el final (es como hacer una copia de la lista)
print("7° Mostrar 'lista[::-1]', significa mostrar todos los elementos de la lista en orden inverso\n",lista[::-1])  # tomamos desde el final hasta el principip (orden inverso) 

# Ejemplo 9
# Usamos un truco para controlar la salida, un método de print llamado end
# 
for i in range (15):
    if i < 14:
        print (i, end=", ")
    else:
        print (i)

# Ejemplo 10
# Mismo ejemplo sin controlar la salida, cada linea se ejecuta y se apila.
for i in range (15):
    print (i)           # No agregué el print por espacio ...se ve muy feo

# Ejemplo 11
# Revisar otra formas de ordenar listas (pero en este archivo van muchas)
lista_desordenada = [5,7,2,8,3,6]
lista_desordenada.sort()            # Usamos el método SORT  
print ("Resultado esperado 2,3,5,6,7,8, lista generada :", lista_desordenada)
print (type(lista_desordenada)) # Verifico, como medida extra, el tipo de dato generado

# Ejemplo 12
# Lista negada = los inversos y lista doble = multiplicadas por algo
# Hay que acostumbrarse a usar 'trucos' para resolver la lógica de los problemas
lista = [10, 20, 30]
lista_negada = [ -e for e in lista ] # Es por comprensión. Genera los inversos de los elementos
lista_doble = [ e*2 for e in lista]  # Esta genera los elementos multiplicados por 2
print(lista_negada) # Todos negativos
print(lista_doble)  # Todos x 2

# Ejemplo 13 
# Ojo!! No se pueden negar valores float o strings. 
lista2 = [True, True, False, 5, 2-3j]   # Ojo con los BOOLEANOS
lista_negada2 = [ -e for e in lista2]   # Los inversos de los elementos numéricos
lista_doble2 = [ e*2 for e in lista2]   # Los elementos multiplicados por 2
print(lista_negada2) # Nótese la salida [-1, -1, 0, -5, (-2+3j)], los booleanos los tomo como 1 y 0 
print(lista_doble2)  # Nótese la salida [2, 2, 0, 10, (4-6j)], fijarse en los booleanos

# Ejemplo 14
# Usando 1 ciclo FOR, poblar 2 listas dependiendo de una condición y mostrar la información horizontal.
lista_i = []
lista_p = []
for i in range (1,11):
    n=(i%2)
    if n==1:
        lista_i.append (i)
    elif n==0:
        lista_p.append (i)
print ("Los números impares entre 1 y 10 son ", lista_i)
print ("Los números pares entre 1 y 10 son ", lista_p)

# Ejemplo 15
# Usos de 'enumerate' en listas, tuplas, diccionarios, cadenas
for i, val in enumerate(['A', 'B', 'C']): # ENUMERATE recorre la lista y su ÍNDICE
     print(i, val)
# 0 A
# 1 B
# 2 C

# En este caso imprime la posición, índice, o puntero, y el contenido de la posición, verticamente 
# Cómo o haría para mostrarlo horizontalmente?
#  
# Ejemplo 16

for i, val in enumerate(['A', 'B', 'C'], start=5): # Mismo anterior, pero cambia el valor del puntero que parte en 5
    print(i, val)
# 5 A
# 6 B
# 7 C La salida va de 5 a 7


# Ejemplo 17
# En este caso va de 5 a 14, se salta de a 3, y el puntero inicia en 1
for i, val in enumerate(range(5, 15, 3), start=1):
    print(f'Pos: {i} -> {val}')
# La salida va con los textos 'Pos: ' y '->'
# Pos: 1 -> 5
# Pos: 2 -> 8
# Pos: 3 -> 11
# Pos: 4 -> 14
print ("")

# Ejemplo 18
# Iterar 2 listas usando un FOR y ZIP
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)
for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)
    print(type(numero), type(texto))
# Número 1 Letra Uno
# <class 'int'> <class 'str'>
# Número 2 Letra Dos
# <class 'int'> <class 'str'>

# Ejemplo 19) zip() con n argumentos - Ejemplo con varias listas
# Como ZIP está definida como, zip(*iterables) o cualquier iterable,
# es posible pasar un número arbitrario de iterables como entrada.
# Es importante notar, que todas tienen la misma longitud, dos.
# Es necesario experimentar para tener una 'idea' cuando toque

numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles  = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)
for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)
# Note la forma en que organiza la salida de los datos en pares    
# 1 Uno One Un
# 2 Dos Two Deux

# Ejemplo 20 - Caso: Hacer zip() con listas de diferentes longitudes
# Podemos usar zip con iterables de diferentes longitudes.
# En este caso, el iterador se detiene, cuando la lista más pequeña se acaba.

numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]
for n, e in zip(numeros, espanol):
    print(n, e)
# Ojo!, sólo completa los dos primeros pares
# 1 Uno
# 2 Dos

# Ejemplo 21 - Caso: zip() con un argumento
# Por definición, se puede hacer, porque ZIP está definido para un 'n' 
# arbitrario de listas, ergo, también es posible usar un único valor.
# El resultado son tuplas de un elemento...raras, pero se puede.

numeros = [1, 2, 3, 4, 5]
zz = zip(numeros) # ZIP de si mismo
print (list(zz)) # R=> [(1,), (2,), (3,), (4,), (5,)]

# Ejemplo 22 - Caso: zip() con diccionarios
# Lo común es usar ZIP con listas, pero al estar definida para cualquier 
# clase iterable.
# Podemos usarla con DICCIONARIOS.

# Por ejemplo, si (a,b) toman los valores de las key del diccionario, no parece 
# muy interesante.

esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for a, b in zip(esp, eng):
    print(a, b)
# 1 1
# 2 2
# 3 3

# Sin embargo, si usamos la función items del tipo DICT, podemos acceder
# al key y al value de cada elemento.
# Se puede facilitar para modificar valores usando, e.g casteo de dict a list y viceversa
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)
# Nótese que en este caso ambas key k1 y k2 son iguales.
# 1 Uno One
# 2 Dos Two
# 3 Tres Three

# Ejemplo 23 - Caso: Deshacer el zip()
# Es posible deshacer un zip, en una sola línea de código.
# Supongamos que hemos usado zip para obtener 'c'.

a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print (list(c)) # R=> [(1, 'One'), (2, 'Two'), (3, 'Three')]
# ¿Es posible obtener a y b desde c? Sí, tan sencillo como:
c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)
print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')

# Uso de STRIP Ejemplo 24 - STRIP eliminar espacios, cadenas de texto, incluso comparar
# Este ejemplo es como un "A inter B"
colores  = ['yellow', 'wine', 'blue', 'green', 'red', 'brown', 'red']
sec_colr = ['blue', 'green', 'red']

strColores  = str(colores).strip("[]")
strSec_colr = str(sec_colr).strip("[]")

if strSec_colr in strColores:
    print("Si")
else:
    print("No")

# Ejemplo 24  - Usar listas como PILAS
# Los métodos de lista, facilitan usar una lista como una pila (stack), donde el 
# último elemento añadido es el primer elemento retirado (LIFO). Para agregar un
# elemento a la cima de la pila, utilizamos APPEND(). Para retirar un elemento de la
# cima de la pila, se utiliza POP() sin un índice explícito. Por ejemplo:

mi_pila = [3, 4, 5]
mi_pila.append(6)
mi_pila.append(7)
print (mi_pila) # R=> [3, 4, 5, 6, 7]
mi_pila.pop()   # R=> Elimina el 7, y lo guarda en memoria hasta que lo ocupe otro
print (mi_pila) # Chequeamos si está el 7 y no está en la lista R=> [3, 4, 5, 6]
mi_pila.pop()   # El siguiente elemento eliminado será el 6. R=> 6
mi_pila.pop()   # Ahora elimina el 5, R=> 5
print (mi_pila) # verificamos y vemos que se han borrado los elementos. R=> [3, 4]

# Ejemplo 25 - Usar listas como COLAS
# También es posible usar una lista como una cola, donde el primer elemento añadido
# es el primer elemento retirado (FIFO); sin embargo, las listas no son eficientes
# para este propósito. Agregar y sacar del final de la lista es rápido, pero 
# insertar o sacar del comienzo de una lista es lento (porque todos los otros 
# elementos tienen que ser desplazados en uno).
# Para implementar una cola, utiliza 'COLLECTIONS.DEQUE', el cual fue diseñado para
# añadir y quitar de ambas puntas de forma rápida. Por ejemplo:

from collections import deque

mi_Cola = deque(["Pedro", "Juan", "Diego"]) # Están Pedro, Juan y Diego en la cola
mi_Cola.append("Luis")                      # Llega Luis
print (mi_Cola)                             # R=> (['Pedro', 'Juan', 'Diego', 'Luis'])
mi_Cola.append("Jorge")                     # Llega Jorge
print (mi_Cola)                             # R=> (['Pedro', 'Juan', 'Diego', 'Luis', 'Jorge'])
print(mi_Cola.popleft())                    # El primero en llegar se va => Pedro
print(mi_Cola)                              # R=> ('Juan', 'Diego', 'Luis', 'Jorge'])
print(mi_Cola.popleft())                    # Ahora se va el segundo en llegar R=> Juan
print(mi_Cola)                              # R=> ('Diego', 'Luis', 'Jorge'])
                                            # La lista restante en orden de llegada

# Ejemplo 26 - Listas por Comprensión . MUY IMPORTANTE ENTENDERLO BIEN !!
# Permite usar expresiones y condiciones para poblar una lista.
# Sus usos comunes son para hacer nuevas colecciones donde cada elemento es el resultado
# de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable, o
# para crear un segmento de la secuencia de esos elementos para satisfacer una 
# condición determinada ==> Es muy parecido a EXRESIONES REGULARES (import re),
# que son fundamentales en ciencia de datos.

# Por ejemplo, queremos crear una lista de cuadrados, como:

cuadrados1 = []
for x in range(10):
    cuadrados1.append(x**2) # Agrega los cuadrados en el rango 0-10, a lista cuadrados
print (cuadrados1)          # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 

# Nótese que esto crea (o sobreescribe) una variable llamada x que sigue existiendo 
# luego de que el bucle haya terminado. sin embargo, podemos aplicar listas por 
# COMPRENSIÓN, poblando la lista de cuadrados sin efecto secundario haciendo:

cuadrados2 = list(map(lambda x: x**2, range(10))) # Usamos una función lambda y map
cuadrados3 = [x**2 for x in range(10)]            # otra expresión equivalente sería:
                                                  # lo cual es más conciso y legible.

# Una lista por comprensión, consta de corchetes rodeando una expresión seguida de la
# declaración FOR, y luego 0 o más declaraciones FOR o IF. El resultado será una 
# nueva lista que sale de evaluar la expresión, en el contexto de los FOR o IF que le 
# siguen. Por ejemplo, esta lista de comprensión combina los elementos de 2 listas 
# si no son iguales:

# Ejemplo 27 Lista Distintos
#
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] # R=> [(1, 3), (1, 4), (2, 3), 
                                                     # (2, 1), (2, 4), (3, 1), (3, 4)]

# y es equivalente a:

combinar_listaDistintos = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combinar_listaDistintos.append((x, y))
print (combinar_listaDistintos) # R=> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1),
                                # (3, 4)]
# Nótese como el orden de los for e if es el mismo en ambos pedacitos de código.
# Si la expresión es una tupla (como el (x, y) en el ejemplo anterior), debe estar entre paréntesis.

# Ejemplo 28 - Operaciones con vectores
vector1 = [-4, -2, 0, 2, 4] # Crear un nueva lista con los valores  *2
vector2 = [x*2 for x in vector1]    # Llenamos la lista, usando una expresión que calcula x^2
print ("La lista de los x^2, del Vector 1 es ", vector2)   # Comprobamos el resultado imprimiento la lista, OK! R=> [-8, -4, 0, 4, 8]
# Filtrar la lista para excluir los valores negativos
vector3 = [x for x in vector2 if x >= 0] # Esta expresión, llena la lista, separando positivos de negativos.
print (vector3)                          # Comprobamos el resultado imprimiento la lista, OK! R=> [0, 2, 4]
# Creamos una nueva lista, aplicado una función de valor absoluto (abs) a todos los elementos del vector1
vector4 = [abs(x) for x in vector1]      # Llenamos vector 4 con el resultado
print (vector4)                          # Comprobamos el resultado imprimiento la lista, OK! R=> [4, 2, 0, 2, 4]

# Ejemplo 29 Limpiar datos usando STRIP
# También usamos expresiones para tareas repetitivas.
# En este ejemplo se usa la función STRIP para recortar los espacios en blanco

fruta_fresca = ['  banana', '  mora ', 'kiwi  '] # Nótese que el 'raw data', viene con espacios a ambos lados del str
[cortar_espacios.strip() for cortar_espacios in fruta_fresca] # Al aplicar la función STRIP, se recortan los espacios
# La lista resultante queda R=> ['banana', 'mora', 'kiwi']

# Ejemplo 30 - Crear una lista de 2 tuplas como (número, su_cuadrado) 
# 
lista_cuad = [(x, x**2) for x in range(6)] # Recordar, va de 0 a 5, excluye el lim_sup del intervalo
print ('La lista de pares (x, x^2), es  ', lista_cuad)
# La lista de pares (x, x^2), es   [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# La expresión a comparar (x, x**2), debe estar entre paréntesis, de lo contrario se genera un error

# Ejemplo 31 - Aplanar una lista usando listas compuestas (listcomp) con dos 'FOR'

vec = [[1,2,3], [4,5,6], [7,8,9]]   # vec es un arreglo de listas y queremos ponerlas en una sola lista
flat_vec= [num for elem in vec for num in elem] # Nótese que en este caso no uso paréntesis, no es comparación o formula
print ("La lista 'aplanada' es ", flat_vec) # La lista esperada R=>[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplo 32 - Listas anidades con expresiones complejas
# Las listas por comprensión pueden contener expresiones complejas y funciones anidadas:

from math import pi # Importamos una librería "MATH" que nos permite hacer cálculos científicos y usar constantes  
pi_evol= [str(round(pi, i)) for i in range(1, 6)] # Creamos una lista con incrementales de pi
print ('Los valores incrementales de pi, son ', pi_evol)
# R=> Los valores incrementales de pi, son ['3.1', '3.14', '3.142', '3.1416', '3.14159']