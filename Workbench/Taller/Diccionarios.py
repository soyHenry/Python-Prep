#*******************************************************************
#*                                                                 *
#*                     TEORIA DICCIONARIOS                         *
#*                                                                 *
#*******************************************************************
# Un dict es una colección de pares, no ordenados, compuestos por una KEY y un VALUE (valor)
# La KEY debe ser HASHEABLE, INMUTABLE, ÚNICA, NO REPETIBLE, los valores pueden ser cualquier cosa MUTABLE.
# Un VALUE puede ser otro DICCIONARIO, TUPLA, LISTA, más los tipos clásicos, como BOOLEAN, etc.
# Otras caracteristicas: Similar al tipo MAPA en otros lenguajes, no confundir con función map(),
# aunque retorna un DICT. La funicón map() es para objetos iterables como listas.
# Método keys() => nom_dic.keys() retorna una clase especial llamada dict_keys, sólo nombra las keys,
# Para acceder a las KEYS, se debe pasar a LISTA ==> nom_var = list(nom_dic.keys()) 
# para poder iterar sobre cada LLAVE
# Método clear() => Borra todos los elementos del diccionario mi_dic.clear(), retorna {}
# Método del(key) => Elimina un elemento con su clave, le paso la clave como parámetro
# Método values() => devuelve todos los VALORES
# Método dict.items()=> Retorna tuplas (clave, valor), también se pasa a list siguen siendo TUPLAS.
# Función in retorna bool si encuentra valor de una clave "mi_key" in "mi_dic"
# Sólo sirve para claves, y es un booleano, TRUE o FALSE, si quiero preguntar po un valor, agregro 
# VALUE de esta forma "mi_valor" in "mi_dic.value".
# Recorridos en diccionarios



# Inicialización de DICCIONARIOS (dict)
# El constructor dict y argumentos.    Ej: dict(color='Azul', num=4)
# Constructor dict y pares de valores. Ej: dict([('color', 'Azul'), ('num', 4)])
# Usando un literal de pares separados por ':' y rodeado por {}. Ej: {'color': 'Azul', 'num': 4}
# 

# Ejemplo 1
# Este es un dic de 4 elementos o pares cualquiera str, int, str y str.
# Obtenemos sus claves y las pasamos a una lista
d = {1: 'str cualquiera', 89: 'soy un valor', 'clave a': 'b', 'clave c': 27} # Inicializa el dict
listkey_d = list(d.keys()) # Hay que convertirlo a lista para acceder a las keys como índice
print (listkey_d) # Ahora veo los índices y los puedo trabajar como LISTA
print ("'D' es del tipo ", type (d)) # Retorna <class 'dict'>
print ("'listkey_d' es del tipo ", type (listkey_d)) # Retorna <class 'list'>, se ve la diferencia
print ("El nombre de la clave en la posición 1 es ", listkey_d [1], " y es de tipo", type(listkey_d [1]))
print ("El nombre de la clave en la posición 3 es ", listkey_d [3], " y es de tipo", type(listkey_d [3])) 
print ("")

# Ejemplo 2
# Crea un diccionario con 4 pares lógicos, colores primarios, colores secundarios, clave 3 y clave 4

mi_dic = {'Colores Primarios': ['Rojo','Azul','Amarillo'], 
          'Colores secundarios': ['Naranja','Violeta','Verde'], 
          'Clave3': 10,
          'Clave4': False}
mi_dic_keys = list (mi_dic.keys()) # Obtenemos las keys y las pasamos a una list "mi_dic_keys"
print (mi_dic_keys) # Imprime la lista
print (type (mi_dic_keys)) # Imprime el tipo de la variable mi_dic_keys, retorna <class 'list'>
print ("Los colores de la clave ", mi_dic_keys [1], "son ", mi_dic['Colores secundarios'])
print ("")
print (mi_dic.keys())

print ("Los colores de la clave ", mi_dic_keys [0], "son ", mi_dic['Colores Primarios'])
print ("El valor de la clave 3", mi_dic_keys [2], "es ", mi_dic['Clave3'])
print ("El valor de la clave 4", mi_dic_keys [3], "son ", mi_dic['Clave4'])

# Ejemplo 3
dd2 = dict (width=4, members=['1', False], name='Pepe') # 3 elementos, 1 int, 1 dict, un str
print ("El contenido de 'dd2' es ", dd2) # # Retorna {'width': 4, 'members': ['1', False], 'name': 'Pepe'}
print (dd2.values()) # Retorna 4, ['1', False], "Pepe"


# Ejemplo 4
print("")
dict2 = {} # Inicializa un diccionario vacío
print ("El contenido de 'dict2' debe ser vacío ", dict2) # Mostrará {}
# El contenido de 'dict2' debe ser {}

# Ejemplo 5
print ("")
# Observar varias formas de declarar diccionarios
{'1': 'primero', '2': 'segundo', 'tercero': 4 * 5 * 6} # Tres pares, str-str, str-str y str-int
{'1': 'primero', '2': 'segundo', 'tercero': 120} # Igual que el anterior, pero el último no es una operación
{str(x): x + 1 for x in range(5)} # Clave es un str x, el valor de x+1 en el rango 0-5
{'0': 1, '1': 2, '2': 3, '3': 4, '4': 5} # 4 pare, str-int, str-int, str-int, str-int 
dict(enumerate(range(5), start=10))
{10: 0, 11: 1, 12: 2, 13: 3, 14: 4}
[(x, chr(x)) for x, idx in enumerate(range(5), start=65)]
[(65, 'A'), (66, 'B'), (67, 'C'), (68, 'D'), (69, 'E')]
#Este ejemplo crea un diccionario compuesto por un int (start=65), y el valor es un str que se calcula
# usando la función chr(), al pasarle el valor de x, retornará 5 letras sucesivas entre 65 y 69 (5 valores)
letters = [(x, chr(x)) for x, idx in enumerate(range(5), start=65)]
dict(letters)
print (letters)
{65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E'}

# Ejemplo 6
# Este es un diccionario
# Se define como nombre_dic = dict(pos=valor, key=valor, valor=valor), hay otras formas
#  
miprimer_dic = dict(tipo='Moto', marca='Honda', power=599)
print(list(enumerate(miprimer_dic))) #convertimos el dict en lista.
#[(0, 'tipo'), (1, 'marca'), (2, 'power')]
print("")
print ("Inicio del ciclo for")
# En este ejemplo iteramos los elementos de un diccionario y me muestran los pares según posición
# Usamos el método "enumerate" que pertenece al tipo list, para recorrer el dict convertido en lista
#  
print ("caso con f")
for idx, key in enumerate(miprimer_dic): # El enumerador de la forma ind, key, recorre el diccionario
    print(f'Pos: {idx} - dict_key {key} - value {miprimer_dic[key]}')
    #print('Pos: {idx} - dict_key {key} - value {miprimer_dic[key]}')
print("")
print ("caso sin f")
for idx, key in enumerate(miprimer_dic): # El enumerador de la forma ind, key, recorre el diccionario
    #print(f'Pos: {idx} - dict_key {key} - value {miprimer_dic[key]}')
    print('Pos: {idx} - dict_key {key} - value {miprimer_dic[key]}')

#Pos: 0 - dict_key tipo - value Moto
#Pos: 1 - dict_key marca - value Honda
#Pos: 2 - dict_key power - value 599

# Ejemplo 7
# Consultar a un dicc, si una clase existe => retorna un booleano TRUE o FALSE
# Ojo si preguntas por un valor, puede existir, pero retornará FALSE
# Si quiero preguntar por un valor, agrego el método .value()

print ("")
letters2 = [(x, chr(x)) for x, idx in enumerate(range(5), start=65)]
dd = dict(letters2)
print ("Este es el diccionario dd", dd)
mi_key1=65
print (type(letters2))
if mi_key1 in dd:
    print ("La clave ", mi_key1," existe")
else:
    print ("La clave ", mi_key1, ". No existe")
print ("")

restaurant = {"Hamburguesa": 100, "Pizza": 50, "Jugo": 30}
if "Hamburguesa" in restaurant:
    print ("SI está")
else:
    print ("NO está")
print (restaurant)