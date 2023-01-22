Variables
a = 'Hola '
b = 'Mundo !'
print(a + b)
# Hola Mundo !
x = 3
y = 12
print(x + y)
15
print(a + x)
"""
"---------------------------------------------------------------------------"

TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_18232/136165486.py in <module>
----> 1 print(a + x)

TypeError: can only concatenate str (not "int") to str
"""
# Dividir "y" entre "x"
y = 9
x = 3
print(y/x)
3.0
# Potencia de "y" elevado a la "x"
y = 2
x = 4
print(y**x)
16
# Devolver el resto de la división
y = 13
x = 3
print(y%x)
1
# Ciclo IF/ELIF/ELSE
valor = 0
if (valor < 0):
    print('El número es negativo')
elif (valor > 0):
    print('El número es positivo')
else:
    print('El número es igual a cero')
# El número es igual a cero

# Ciclo FOR - Caso 1
for n in range(1,10): #Incluye el primero y excluye el último
    print(n, end(", "))

# Ciclo WHILE
n = 1
while (n < 10):
    print(n)
    n = n + 1
"""
1
2
3
4
5
6
7
8
9
"""
# Lista

# Caso 1 - Inicializa una lista y muestra la cantidad de elementos

edad = (3,1,0.2,8,7) #Declara un objeto lista y le asigna elementos
print (len(edad))    #Imprime la cantidad de elementos de la lista usando la función LEN
#5                   # La función retorno 5

# Caso 2 - Identificar el tipo de variable usando la función TYPE, retorno el tipo de dato
mi_lista = ['Rojo','Azul','Amarillo','Naranja','Violeta','Verde']
type(mi_lista)
# list
print(mi_lista)
['Rojo', 'Azul', 'Amarillo', 'Negro', 'Naranja', 'Violeta', 'Verde']
print(mi_lista[0:2])
['Rojo', 'Azul']
print(mi_lista[:2])
['Rojo', 'Azul']
print(mi_lista[1:])
['Azul', 'Amarillo']
mi_lista.insert(3,'Negro')
print(mi_lista.index('Azul'))
# 1
mi_lista.insert(3,'Negro')
mi_lista.extend(['Marrón','Gris'])
print(['a','b','c'] * 3)
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
print(mi_lista.index('Azul'))
# 1
mi_lista.remove('Blanco')

"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_10044/2480624766.py in <module>
----> 1 mi_lista.remove('Blanco')

ValueError: list.remove(x): x not in list
mi_lista.remove('Negro')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_10044/298389232.py in <module>
----> 1 mi_lista.remove('Negro')

ValueError: list.remove(x): x not in list
"""
ultimo = mi_lista.pop()
ultimo = mi_lista.pop()
print(ultimo)
# Gris
ultimo = mi_lista.pop()
ultimo
# 'Amarillo'
mi_tupla=tuple(mi_lista)
print(mi_tupla[1])
# Azul
'Rojo' in mi_tupla
# True
mi_tupla.count('Rojo')
# 1
print(mi_lista[:] * 3)
# ['Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris', 'Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris', 'Rojo', 'Azul', 'Amarillo', 'Negro', 'Marrón', 'Gris']
mi_tupla.count('Rojo')
# 1
mi_tupla='Gaspar', 5, 8, 1999
nombre, dia, mes, año = mi_tupla
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, " - Año: ", año)
# Nombre:  Gaspar  - Dia: 5  - Mes:  8  - Año:  1999
nombre = 'Darío'
edad = 39
print(nombre, edad)
print("Mi nombre es", nombre, ". Mi edad es", edad, "años")
print("Mi nombre es {}. Mi edad es {} años". format(nombre, edad))
# Darío 39
# Mi nombre es Darío . Mi edad es 39 años
# Mi nombre es Darío. Mi edad es 39 años

mi_diccionario = {  'Colores Primarios': ['Rojo','Azul','Amarillo'], 
                    'Colores secundarios': ['Naranja','Violeta','Verde'], 
                    'Clave3': 10,
                    'Clave4': False}
print(mi_diccionario['Colores secundarios'])
# ['Naranja', 'Violeta', 'Verde']

mi_diccionario={'Clave1':'Valor1', 'Clave2':{'numeros':[1,2,3,4,5]}}
print(mi_diccionario.keys())
# dict_keys(['Clave1', 'Clave2'])
print(mi_diccionario.values())
# dict_values(['Valor1', {'numeros': [1, 2, 3, 4, 5]}])
len (mi_diccionario)
# 2

edad = 60
edad_compa = 50
if (edad < edad_compa):
    print(edad)
    if (edad < 100):
        print(edad + 100)
    else:
        print(edad - 100)
else:
    print(edad_compa)
# 50

primeros_10 = [0,1,2,3,4,5,6,7,8,9]
print(primeros_10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in primeros_10:
    if (n%2 == 0):
        print(n)
        primeros_10[n]=0
print("\va de nuevo....\n")
"""
0
2
4
6
8
# va de nuevo....
"""

print(primeros_10)
# [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]

for n in primeros_10:
    print(primeros_10[n])
print("\va de nuevo....\n")
"""
0
1
0
3
0
5
0
7
0
9
va de nuevo....
"""

print(primeros_10[9])
# 9
primeros_10 = ['a','b','c','d']
primeros_10[4]
"""
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-21-1f7c241d828c> in <module>
----> 1 primeros_10[4]

IndexError: list index out of range
"""
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