#Ejericio 1

listadeletras = []                   # Crea un objeto list llamado lista
for unaletra in "paralelepipedo": # Define una variable car para recorrer el string "casa"
    listadeletras.append(unaletra)        # Agrega cada caracter del string en  la lista
print(listadeletras)                 # Imprime los valores de la lista que son los caracteres de la palabra casa o pera, lo que sea
                             # Salida esperada ['c', 'a', 's', 'a']

"""
#Ejercicio 2
# Lista de 4 elementos y para cada elemento calcularle la potencia de 2, usando el método tradicional, eso seria así:
#Alternativa 1

lista_potencias = []    #Crea una lista llamada "lista_potencias"
for i in range(4):     #ciclo for para recorrer lista de 4 elementos, va de 0 a 3, el índice lo llamamos "i"
    lista_potencias.append(i**2) #a la lista "lista_potencias", la voy poblando con el dato calculado.
print(lista_potencias)          #Imprime los 4 valores almacendaos en la lista #Obs: como no cambié el nombre, concatenó los valores de la lista al final
# [0, 1, 4, 9]

#Alternativa 2
# Entonces el ejemplo anterior usando listas de comprensión, eso seria así:
lista_potencias2 = [i**2 for i in range(4)]
print ("Esta es la lista de potencias Nr2", lista_potencias2)
# [0, 1, 4, 9]

#Ejercicio 3
#Lista con las potencias de 2 de los primeros 10 números, método tradicional:
"""
"""
Método 3-1
lista1_pot10_2 = []                #Creamos un objeto lista vacio []
for num in range (0, 11):          #incluye el primero y no el últimmo. Usando un ciclo FOR usando la var "num" en el tramo de 0-10, ambos incluidos
    lista1_pot10_2.append (num**2) #Llenamos la lista con potencias PARTIENDO DE 0, a 10 (11-1) 
print(lista1_pot10_2)

#[4, 9, 16]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Método 3-2
#Entonces el ejemplo anterior usando listas de comprensión, eso seria así:
#lista2_pot10_2 = [num2**2 for num2 in range(0, 11)] #Creamos la lista con los valores según condición
#print("Este es el método 3-2, para crear la lista de 10 números y sus potencias",lista2_pot10_2)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#De este código anterior usted puede aprender que es posible modificar al vuelo los elementos los cuales van a formar la lista.

# Ej
# Con este ejemplo se ve como funciona el conteo de posiciones en una lista (cada elemento es una posX)
lista = ["pos0", "pos1", "pos2", "pos3", "pos4", "pos5"]
print("Esta es la lista:\n", lista, "\n")
print("1° Mostrar 'lista[2:5]', significa la pos2, pero excluye la 5, ojo!\n", lista[2:5])  # tomamos del 2 al 5 (sin incluir el 5)
print("2° Mostrar 'lista[4:]', significa desde la pos4 hasta la última\n",lista[4:])  # tomamos del 4 hasta el final
print("3° Mostrar 'lista[:2]', significa desde el BOF hasta la pos2, excluye la pos2\n", lista[:2])  # tomamos desde el principio hasta el 2 (sin incluir)
print("4° Mostrar 'lista[1:6:2]', significa 1 por medio, desde la pos1, incluye la 5\n", lista[1:6:2]) # tomamos 1 de cada 2 elementos desde el 1 hasta el 6 (sin incluir)
print("5° Mostrar 'lista[4:1:-1]', significa orden desc de la pos4 a la 2, excluye la pos1",lista[4:1:-1])
print("6° Mostrar 'lista[:]', significa mostrar todos los elementos de la lista\n",lista[:])  # tomamos desde el principio hasta el final (es como hacer una copia de la lista)
print("7° Mostrar 'lista[::-1]', significa mostrar todos los elementos de la lista en orden inverso\n",lista[::-1])  # tomamos desde el final hasta el principip (orden inverso) 
"""
# EJ 5
# Con este ejemplo usamos un truco para controlar la salida, un método de print llamado end
# 
for i in range (15):
    if i < 14:
        print (i, end=", ")
    else:
        print (i)

"""
# Ej 6
# Mismo ejemplo sin controlar la salida, cada linea se ejecuta y se apilan.
#for i in range (15):
#    print (i)
"""
"""
# Revisar formas de ordenar listas
lista_desordenada = (5,7,2,8,3,6)
print (lista_desordenada)
print (lista_desordenada.sort())
"""