#*******************************************************************
#*                                                                 *
#*                          TEORIA LISTAS                          *
#*                                                                 *
#*******************************************************************

# Una LIST, es un objeto, es una colección de cosas, pueden ser tareas,
# vegetales, nombres
# mercaderías, cualquier cosa.

# Dos formas paa declararlas e iniciaizarlas

# 1) Defino una variable y le asigno un tipo lista VACÍO con paréntesis
empty_list1 = list()     # Note que se debe indicar el tipo lista o lo considerará una TUPLA
print (empty_list1, "esta es la lista 1 con '()'")
print (type(empty_list1))

# 2) Defino una variable y sé que es del tipo lista por los corchetes '[]'
empty_list2 = []         # A la variable se le asigna una lista vacía con CORCHETES 
print (empty_list2, "esta es la lista 2")
print (type (empty_list2))

# Ejemplo 1
numbers = [1,2,3,4,5,6] # Lista de números
print("'numbers' es del tipo ", type(numbers)) # De devolver el texto+ type 'list'

# Ejemplo 2
groceries = ["tomato", "carrot", "letuce"] # Una lista con 3 strings de 'vegentales'
print (groceries [0])  # El puntero va con corchetes y parte de 0, imprime "tomato"
print (numbers [3])    # Es una COLECCION, imprime todos los elementos 
print (len(groceries)) # Conocer el largo de la la lista con len, devuelve 3

# Ejemplo 3
lastname = "cordova" # Variable de tipo string, contiene "cordova" 
mix_of_data_types_list = [1, "Jota", lastname, 2+5, 1-3j, 3.14] # Lista con distintos tipos de var
print ("'mix_of_data_types_list' es del tipo-", type(mix_of_data_types_list)) #devuelve 'list'
#podemos almacenar un mix de datos

# Ejemplo 4
listadeletras = []                # Crea un objeto list llamado listadeletras
for unaletra in "paralelepipedo": # Define una variable 'unaletra' y recorre el string "paralelepípedo"
    listadeletras.append(unaletra)# Agrega cada caracter del string a 'listadeletras' usando el método 'append'
print (listadeletras)             # Imprime los valores de la lista que son los caracteres de la palabra 'paralelepípedo'', lo que sea
                                  # Salida esperada ['p', 'a', 'r', 'a', 'l', 'e', 'l', 'e', 'p', 'i', 'p', 'e', 'd', 'o']

# Ejemplo 5
# Crear una lista de 4 elementos y, para cada elemento, calcularle la potencia de 2, usando 
# el método tradicional, eso seria así:
# Alternativa 1
lista_potencias = []            # Crea una lista llamada "lista_potencias"
for i in range(4):              # Ciclo for para recorrer lista de 4 elementos, va de 0 a 3, el índice lo llamamos "i"
    lista_potencias.append(i**2)# La lista "lista_potencias", la voy poblando con el dato calculado.
print(lista_potencias)          # Imprime los 4 valores almacendaos en la lista [0, 1, 4, 9]

# Ejemplo 6
# Entonces el ejemplo anterior usando listas de comprensión, eso seria así:
lista_potencias2 = [i**2 for i in range(4)]                   # Usa un for
print ("Esta es la lista de potencias Nr2", lista_potencias2) # Imprime [0, 1, 4, 9]

# Ejemplo 7
# Lista con las potencias de 2 de los primeros 10 números, método tradicional:
# Alternativa 1
lista1_pot10_2 = []                # Creamos un objeto lista vacio []
for num in range (0, 11):          # Incluye el primero y no el últimmo. Usando un ciclo FOR usando la var "num" en el tramo de 0-10, ambos incluidos
    lista1_pot10_2.append (num**2) # Llenamos la lista con potencias PARTIENDO DE 0, a 10 (11-1) 
print(lista1_pot10_2)              # Salida por pantalla [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Alternativa 2
#Entonces el ejemplo anterior usando listas de comprensión, eso seria así:
#lista2_pot10_2 = [num2**2 for num2 in range(0, 11)] #Creamos la lista con los valores según condición
#print("Este es el método 3-2, para crear la lista de 10 números y sus potencias",lista2_pot10_2)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#De este código anterior usted puede aprender que es posible modificar al vuelo los elementos los cuales van a formar la lista.

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
# Con este ejemplo usamos un truco para controlar la salida, un método de print llamado end
# 
for i in range (15):
    if i < 14:
        print (i, end=", ")
    else:
        print (i)

# Ejemplo 10
# Mismo ejemplo sin controlar la salida, cada linea se ejecuta y se apilan.
for i in range (15):
    print (i)

# Ejemplo 11
# Revisar otra formas de ordenar listas
lista_desordenada = [5,7,2,8,3,6]
lista_desordenada.sort()
print ("Resultado esperado 2,3,5,6,7,8, lista generada :", lista_desordenada)
print (type(lista_desordenada))

# Ejemplo 12
# Lista negada = los inversos y lista doble = multiplicadas por algo
lista = [10, 20, 30]
lista_negada = [ -e for e in lista ] # Los inversos de los elementos
lista_doble = [ e*2 for e in lista]  # Los elementos multiplicados por 2
print(lista_negada)
print(lista_doble)

# Ejemplo 13 
# Una lista de valores float, no se pueden negar strings
lista2 = [True, True, False, 5, 2-3j]
lista_negada2 = [ -e for e in lista2] # Los inversos de los elementos numéricos
lista_doble2 = [ e*2 for e in lista2]  # Los elementos multiplicados por 2
print(lista_negada2) # Nótese la salida [-1, -1, 0, -5, (-2+3j)], los booleanos los tomo como 1 y 0 
print(lista_doble2)  # Nótese la salida [2, 2, 0, 10, (4-6j)], fijarse en los booleanos

# Ejemplo 14
# Con un ciclo for, alimenta dos listas dependiendo de una condición y muestra la información horizontal.
lista_i = []
lista_p = []
for i in range (1,21):
    n=(i%2)
    if n==1:
        lista_i.append (i)
    elif n==0:
        lista_p.append (i)
print ("Los números impares entre 1 y 20 son ", lista_i)
print ("Los números pares entre 1 y 20 son ", lista_p)

# Ejemplo 15
# Usos de 'enumerate' en listas, tuplas, diccionarios, cadenas
for i, val in enumerate(['A', 'B', 'C']):
     print(i, val)
"""
0 A
1 B
2 C
"""

# En este caso imprime la posición o puntero, y e contenido de la posición, vertical 

# Ejemplo 16

for i, val in enumerate(['A', 'B', 'C'], start=5): # Mismo anterior, pero cambia el valor del puntero que parte en 5
    print(i, val)
""" 
5 A
6 B
7 C
"""
# La salida va de 5 a 7

# Ejemplo 17
# En este caso va de 5 a 14, se salta 3, y el puntero inicia en 1
for i, val in enumerate(range(5, 15, 3), start=1):
    print(f'Pos: {i} -> {val}')
"""
Pos: 1 -> 5
Pos: 2 -> 8
Pos: 3 -> 11
Pos: 4 -> 14
"""
# La salida va con los textos 'Pos: ' y '->'
print ("")

# Ejemplo