#*******************************************************************
#*                                                                 *
#*            MIX DE EJERCICIOS Y REVISIÓN DE EJEMPLOS             *
#*                  CON COMENTARIOS Y CITAS                        *
#*******************************************************************
# 
# Ej 1) Cocatenar cadenas de caracteres, deben ser del mismo tipo (str+str)

a = 'Hola '
b = 'Mundo !'
# Ej 2) Sumar dos enteros, puedo imprimir directo el resultado

print(a + b)

# Ej 3) Mismo ejemplo, almaceno en variable
x = 3
y = 12
print(x + y) # 15

# Ej 4) Manejo de errores por tipo, no sumar tipos distintos.
# print(a + x)==> Da un error porque son de distinto tipo, concatencación
# a= string       Para que funcione, puedo cambiar el tipo a str(3)
# x= int          quedaría como 'Hola 3'

# Ej 5) Dividir "y" entre "x"
y = 9
x = 3
print(y/x) # => 3.0

# Ej 6) Potencia de "y" elevado a la "x"
y = 2
x = 4
print(y**x) # si elevo a 0.5, Python entiende que es raíz cuadrada igual que 1/2
# R=> 16

# Ej 7) Devolver el resto de la división
y = 13
x = 3
print(y%x) # Sirve para todas las operaciones en que deba detectar pares, impares, primos

# Ej 8) Ciclo IF/ELIF/ELSE
valor = 0                           # Inicializo un contador para entrar al ciclo
if (valor < 0):
    print('El número es negativo')
elif (valor > 0):
    print('El número es positivo')
else:
    print('El número es igual a cero') # R=> El número es igual a cero

# Ej 9) Ciclo FOR - Simple (ver ciclos listas dobles)
for n in range(1,11): #Incluye el primero y excluye el último
    print(n,(')'))

# Ej 10) Ciclo WHILE - Simple con un contador
n = 1           # Contador definido en 0
while (n < 10): # Mientras n sea menor que 10, haga lo que está dentro
    print(n)    # Imprimir el contenido de la variable en cada ciclo
    n = n + 1   # El contador es la condición de termino. Al llegar a 11, no entra el nuevo ciclo.

# Ej 11) Lista Simple - Inicializa una lista y obtener la cantidad de elementos con LEN

edad = (3,1,0.2,8,7) # Declara un objeto lista y le asigna elementos, la lista es mutable, no ordenada
print (len(edad))    # Imprime la cantidad de elementos de la lista usando la función LEN
#5                   # La función retornó 5

# Ej 12) Lista - Retornar tipo de variable usando TYPE, isertar con INSERT, pegar dos listas con EXTEND, 
# eliminar un elemento con REMOVE, retornar un elemento usando su índice con INDEX[]y modificadores en la salida

mi_lista = ['Rojo','Azul','Amarillo','Naranja','Violeta','Verde'] # Lista de 6 elementos
type(mi_lista) # la lista, como objeto es de tipo list, pero sus objetos no, pueden ser de cualquier tipo.
# R => list
print(mi_lista) # Imprime los elementos de la lista, en el orden que están...se pueden ordenar
# R=> ['Rojo', 'Azul', 'Amarillo', 'Negro', 'Naranja', 'Violeta', 'Verde']
print(mi_lista[0:2]) # Imprimo la lista desde el índice 0, al 2, es decir el 0 y el 1, excluye el 2
# R=> ['Rojo', 'Azul']
print(mi_lista[:2]) # Imprime la lista desde el inicio, hasta el indice, desde el 0 al 1, excluye el 2
# R=> ['Rojo', 'Azul']
print(mi_lista[1:]) # Imprime la lista desde la posición 1, hasta el final, excluye la posición 0. 
# R=> ['Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
mi_lista.insert(3,'Negro') # INSERT, inserta un elemento en la posición del índice dado.
print(mi_lista.index('Azul')) #Retorna el valor (int) del índice cuando halla la coincidencia, este caso=1.
print(mi_lista [1]) # => Azul, retorna el valor del elemento en el indice, en este caso [1]= Azul
mi_lista.insert(3,'Negro') # Inserta el elemento 'Negro', en la posición 3.
mi_lista.extend(['Marrón','Gris']) # EXTEND, 'pega' la lista ('Marrón','Gris'), al final de mi_lista
print(['a','b','c'] * 3 ) # Igual que la concatenación, puedo 'multiplizar str =>['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
mi_lista.remove('Blanco') # Recorre la lista, si existe el elemento, lo borra 1 vez, si no, da ERROR (not in list).
ultimo = mi_lista.pop()   # Remueve el último elemento de la lista 
print(ultimo)             # Conserva el último elemento eliminado con POP, si ejecuto otra vez, elimina el anterior.

# Ej 13) Tuplas - Operaciones de cambio de tipo, recorrer la tupla, contar elementos, imprimir, asignar
mi_tupla=tuple(mi_lista)  # La lista fue 'casteada?, se le ambio el tipo a TUPLE (lista INMUTABLE)
print(mi_tupla[1])        # Se accede a sus elementos igual que la lista, NO SE PUEDE ORDENAR R=> Index 1 = Azul
'Rojo' in mi_tupla        # Puedo hacer evaluaciones BOOLEANAS (T/F), está el elemento en la tupla, retorna T/F =>T
mi_tupla.count('Rojo')    # Puedo contar los elementos que coinciden con un valor, retorna 1 entero
print(mi_lista[:] * 3)    # Concatena la lista veces, igual que los strings. 
# R=> ['Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris', 'Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris', 'Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris']
mi_tupla='Gaspar', 5, 8, 1999    # Crea una tupla a partir asignarle elementos
nombre, dia, mes, año = mi_tupla # Asigna los valores de la tupla a variables
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, " - Año: ", año) # Imprime el contenido de las variables
# R=> Nombre:  Gaspar  - Dia: 5  - Mes:  8  - Año:  1999

# Ej 14) Formateo de impresión - 3 casos (sólo variables, con texto y con formato)
nombre = 'Darío'        # Inicializo var nombre con el str 'Darío'
edad = 39               # Inicializo var edad con el int 39
print(nombre, edad)     # Caso 1) Imprimo el contenido de las variables. Puede ser cualquier variable.
print("Mi nombre es", nombre, ". Mi edad es", edad, "años") # Caso 2) Impresión tradicional con variables.
print("Mi nombre es {}. Mi edad es {} años". format(nombre, edad)) # Caso 3) Impresión con FORMATO
# Caso 1) Darío 39
# Caso 2) Mi nombre es Darío . Mi edad es 39 años
# Casi 3) Mi nombre es Darío. Mi edad es 39 años

# Ej 15) Diccionarios - Creación y operaciones (pares de elementos, {key:elemento})
mi_diccionario = {  'Colores Primarios': ['Rojo','Azul','Amarillo'],        # Crear con {key:Elm, key:Elm...}
                    'Colores secundarios': ['Naranja','Violeta','Verde'],   # Elm= Cualquier cosa, mutable
                    'Clave3': 10,                                           # Key= Hasheable, inmutable
                    'Clave4': False}
print (mi_diccionario['Colores secundarios'])   # Lo puedo acceder por sus claves o índices y retorna los VALORES
# R=> ['Naranja', 'Violeta', 'Verde']           # Para la clave dad, retorno los elementos respectivos

mi_diccionario = {'Clave1':'Valor1', 'Clave2':{'numeros':[1,2,3,4,5]}} # Dic key1=str y val1=str, key2=str, val2=lista
print (mi_diccionario.keys())  # Retorna R=> dict_keys(['Clave1', 'Clave2'])
print(mi_diccionario.values()) # Retorna R=> dict_values(['Valor1', {'numeros': [1, 2, 3, 4, 5]}])
len (mi_diccionario) # R=> 2, la función LEN es útil cuando se debe recorrer el DICT 

# Ej 16) Ciclo IF/ELIF/ELSE

edad = 60
edad_compa = 50
if (edad < edad_compa):     # Compara dos números, y establece dos condiciones
    print(edad)
    if (edad < 100):
        print(edad + 100)
    else:
        print(edad - 100)    
else:
    print(edad_compa)       # No cumple ninguna e imprime el contenido de la var edd_compa R=> 50

# Ej 17) Recorre una lista con un ciclo FOR y extrae los PARES

primeros_10 = [0,1,2,3,4,5,6,7,8,9]
print(primeros_10) # R=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
outlist = []                                # Esta lista acumula los valores encontrados
for n in primeros_10:                       # For 'var' in 'lista/tupla/dict'
    if (n%2 == 0):                          # Uso la función resto para reconocer los PARES  
        outlist.append(n)                   # Los guardo en una lista para poder mostrarlos horizontalmente 
print ('Los pares son', outlist)            # R=> Los pares son [0, 2, 4, 6, 8]

# Ej 18) Recorrer una lista con su índice y ver error fuera de rango

print(primeros_10[9])           # R=> 9, el valor existe dentro del rango
primeros_10 = ['a','b','c','d'] # Esta lista de str, tiene 4 elm, índices del 0 al 3.
primeros_10[4]                  # Al intentar accesar a una posición que NO existe, retornará un error (out of range)

# Ej 19) Uso de la función SEQUENCE - Recorre un rango 
n = 40
sequence = [0,1]
for i in range(2,n):
    sequence.append(sequence[i-1]+sequence[i-2])
print (sequence)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 
# 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 
# 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986]

mi_diccionario = {  'Colores Primarios': ['Rojo','Azul','Amarillo'], 
                    'Colores secundarios': ['Naranja','Violeta','Verde'], 
                    'Clave3': 10,
                    'Clave4': False}
print(mi_diccionario['Colores secundarios'])
# ['Naranja', 'Violeta', 'Verde']

mi_diccionario['Clave3']=2

mi_diccionario
{'Argentina': 'Buenos Aires', 'Italia': 'Roma', 'Inglaterra': 'Londres'}
mi_diccionario['Clave5']='Otro ejemplo'
mi_tupla=("Argentina", "Italia", "Inglaterra")
mi_diccionario={mi_tupla[0]:"Buenos Aires", mi_tupla[1]:"Roma", mi_tupla[2]:"Londres"}
mi_diccionario={'Clave1':'Valor1', 'Clave2':(1,2,3,4,5)}
type(mi_diccionario['Clave2'])
# tuple
mi_diccionario={'Clave1':'Valor1', 'Clave2':{'numeros':[1,2,3,4,5]}}
type(mi_diccionario['Clave2'])
# dict
mi_diccionario={'Clave1':'Valor1', 'Clave2':[1,2,3,4,5]}
type(mi_diccionario['Clave2'])
# list
print(mi_diccionario.keys())
# dict_keys(['Clave1', 'Clave2'])
print(mi_diccionario.values())
# dict_values(['Valor1', [1, 2, 3, 4, 5]])
len(mi_tupla)
# 3

def imprimir_valor_variable(var):
    print('El valor de la variable es' + str(var))
imprimir_valor_variable(mi_lista)
# El valor de la variable es['Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris']

def ordenar_dos_numeros(num1, num2):
        if (num1 > num2):
            return num2, num1
        else:
            return num1, num2

ordenar_dos_numeros(8,1)
# (1, 8)

def factorial(numero):
# Devuelve el factorial
     if (numero > 1):
        numero = numero * factorial(numero - 1)
        return numero

factorial(3)
# 6
#help(factorial)
#Help on function factorial in module __main__:

#factorial(numero)
# Devuelve el factorial

def dividir(dividendo, divisor = 1):
    if (divisor == 0):
        return 'No se puede dividir por cero'
    else:
        return dividendo / divisor
print(dividir(10))
# 10.0
print(divisor)
"""
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_10044/1862935505.py in <module>
----> 1 print(divisor)

NameError: name 'divisor' is not defined
"""

divisor = 5
def dividir(dividendo):
    if (divisor == 0):
        return 'No se puede dividir por cero'
    else:
        return dividendo / divisor
print(dividir(10))
# 2.0
print(divisor)
# 5

divisor = 5

def dividir(dividendo, divisor = 1):
    if (divisor == 0):
        return 'No se puede dividir por cero'
    else:
        return dividendo / divisor

print(dividir(10))
# 10.0

print(divisor)
# 5

lambda_producto = lambda x, y: x * y
lambda_producto(3, 4)
# 12

class Animal:
    '''
    En esta clase se crean los animales
    '''
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color
    def mePresento(self):
        print('Hola, soy ', self.especie, ', de color', self.color, ' y tengo ', self.edad, ' años')
    def cumplirAños(self):
        self.edad = self.edad + 1

a1 = Animal('Ratón', 2, 'Marrón')

print(a1.especie)
print(a1.edad)

a2 = Animal('Liebre', 3, 'Gris')
print(a2.especie)
print(a2.edad)
# Ratón
# 2
# Liebre
# 3

a1.mePresento()
# Hola, soy  Ratón , de color Marrón  y tengo  2  años
a2.mePresento()
# Hola, soy  Liebre , de color Gris  y tengo  3  años
a1.cumplirAños()
a1.mePresento()
# Hola, soy  Ratón , de color Marrón  y tengo  3  años

# Caja Negra
import unittest
def suma(num_1, num_2):
    return num_1 + num_2
class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

unittest.main(argv=[''], verbosity=2, exit=False)

"""
" test_suma_dos_negativos (__main__.CajaNegraTest) ... ok
" test_suma_dos_positivos (__main__.CajaNegraTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.004s

OK
<unittest.main.TestProgram at 0x2226bd08400>
if __name__ == '__main__':
    unittest.main()
"""
#Caja de Cristal

import unittest
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)
    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)
unittest.main(argv=[''], verbosity=2, exit=False)

"""
test_suma_dos_negativos (__main__.CajaNegraTest) ... ok
test_suma_dos_positivos (__main__.CajaNegraTest) ... ok
test_es_mayor_de_edad (__main__.PruebaDeCristalTest) ... ok
test_es_menor_de_edad (__main__.PruebaDeCristalTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.006s

OK
<unittest.main.TestProgram at 0x2226bd153d0>
if __name__ == '__main__':
    unittest.main()
"""

# Python

def busca_pais(paises, pais):
# Paises es un diccionario. Pais es la llave.
# Codigo con el principio EAFP (Easier to Ask Forgiveness than Permission/Mejor pedir perdón que pedir permiso)
# Otro LBYL (Look Before You Leap/Piensa antes de actuar 🤐).
    
    try:
        return paises[pais]
    except KeyError:
        return None

def divide_elementos_de_lista(lista, divisor):

    '''
    Cada elemento de una lista es dividida por un divisor definido.
    En caso de error de tipo ZeroDivisionError que
    significa error al dividir en cero
    la función devuelve la lista inicial
    '''
    try:
        return [i / divisor for i in lista]
    
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))
# division by zero
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

divisor = 3
print(divide_elementos_de_lista(lista, divisor))
# [0.0, 0.3333333333333333, 0.6666666666666666, 1.0, 1.3333333333333333, 
# 1.6666666666666667, 2.0, 2.3333333333333335, 2.6666666666666665, 3.0]

lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1

"""
5
4
9
2
"""

lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)

"""
5
4
9
2
"""
from collections import Iterable
cadena = "Hola"
numero = 3
print("cadena", isinstance(cadena, Iterable))
print("numero", isinstance(numero, Iterable))

"""
cadena True
numero False
C:\Users\lopez\AppData\Local\Temp/ipykernel_10044/1562366592.py:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.10 it will stop working
  from collections import Iterable
"""

print(list("Hola"))
# ['H', 'o', 'l', 'a']
print(sum([1, 2, 3]))
# 6
print("-".join("Hola"))
# H-o-l-a

mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(i)
"""
a
b
c
"""

libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
"""
página1
página2
página3
página4
print(next(marcapaginas))
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_10044/1391636315.py in <module>
----> 1 print(next(marcapaginas))

StopIteration: 
14 % 3
2
14 // 3
4
"""
a = [1,2]
b = a.copy()
b.append(3)
print(a)
# [1, 2]

print(b)
# [1, 2, 3]
b.append(4)
print(a)
# [1, 2, 3]
print(b)
# [1, 2, 3, 4]
x = 7
# 7 & 7
# 2
print(x)
# 2
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)
type(c)
# zip
list(c)
[(1, 'Uno'), (2, 'Dos')]
frase = "El perro de san roque no tiene rabo"
errores = [i for i in frase if i == 'r']
print(errores)
# ['r', 'r', 'r', 'r']
n = 40 
sequence = [0,1] 
for i in range(2,n): 
    sequence.append(sequence[i-1]+sequence[i-2]) 
    print (sequence)

"""2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
4 << 1
8"""