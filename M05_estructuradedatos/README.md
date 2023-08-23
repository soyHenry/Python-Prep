![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)


## Principales Objetivos de Aprendizaje para esta Clase

- Conocer la diferencia entre una variable y una estructura de datos
- Manejar el tipo de dato lista en Python

## Estructuras de datos

Anteriormente se mencionó que un dato representa la realidad, y se presentó el concepto de variable, que es un elemento que nos permite guardar un dato dentro de nuestro programa. Sin embargo, rápidamente vamos a llegar a la conclusión de que una variable puede llegar a quedar insuficiente para ciertas representaciones. Ante esta situación, en los lenguajes de programación tenemos estructuras de datos más complejas, en el caso de Python contamos con listas, tuplas y diccionarios.

### Lista

Una estructura de datos muy importante en Python es la lista, que consiste en una serie de elementos ordenados.
Esos elementos pueden ser de distinto tipo, e incluso pueden ser de tipo lista también.<br>

Operaciones con listas:
* Creacion 
```python
mi_lista = ['Rojo','Azul','Amarillo','Naranja','Violeta','Verde']
```
* Imprimir
```python
print(mi_lista)
```
* Ver el tipo de dato 
```python
type(mi_lista)
```

Las listas, así como otras estructuras de datos que se verán en adelante, tienen varios elementos, motivo por el cual cuando se quiere acceder en específico se requiere de un **índice** que va a hacer referencia al elemento dentro de la lista:

* Imprimir el tercer elemento de la lista (el índice comienza en cero)
```python
print(mi_lista[2])
```
* Acceder a un rango dentro de la lista (el límite inferior se incluye y el superior se excluye)
```python
print(mi_lista[0:2])
```
* Al no poner primer valor, Python asume que es un 0
```python
>>> print(mi_lista[:2])
['Rojo', 'Azul']
```
* Al no poner segundo valor, Python asume que se trata de todos los elementos a partir del primero 
```python
 >>> print(mi_lista[0:])
 ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
 ```
* Agregar un elemento al final de la lista (Si el elemento ya existe va a quedar duplicado)
```python
mi_lista.append('Blanco') 
```
* Agregar un elemento especificando el índice 
```python
 >>> mi_lista.insert(3,'Negro')
 >>> print(mi_lista[:])
['Rojo', 'Azul', 'Amarillo', 'Negro', 'Naranja', 'Violeta', 'Verde']
```
* Concatenar una nueva lista a la lista previamente creada 
```python
mi_lista.extend(['Marrón','Gris'])
```
* Encontrar el índice de un valor específico 
```python
>>> print(mi_lista.index('Azul'))
1
```
* Eliminar un elemento de la lista (Si el elemento no existe va a arrojar un error)
```python 
>>> mi_lista.remove('Blanco') 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_10044/308548076.py in <module>
----> 1 mi_lista.remove('Blanco')

ValueError: list.remove(x): x not in list
>>> mi_lista.remove('Negro') 
```
* Extraer y recuperar el último elemento de la lista 
```python 
>>> ultimo = mi_lista.pop()
>>> print(ultimo)
Gris
```
* Multiplicar la lista 3 veces 
```python 
>>> print(['a','b','c'] * 3)
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
```
* Ordenar una lista de menor a mayor
```python 
>>> lista= [1,4,3,6,8,2]
>>> lista.sort()
>>> print(lista)
[1,2,3,4,6,8]
```
* Ordenar una lista de mayor a menor
```python 
>>> lista= [1,4,3,6,8,2]
>>> lista.sort(reverse=True)
>>> print(lista)
[8,6,4,3,2,1]
```

### Tupla

Son una estructura similar a las listas, la diferencia está en que no se pueden modificar una vez creadas, es decir que son **inmutables**:

* Convertir una lista a tupla 
```python 
mi_tupla=tuple(mi_lista)
```
* Imprimir el índice 1 de la tupla 
```python 
>>> print(mi_tupla[1])
Azul
```
* Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
```python
>>> 'Rojo' in mi_tupla
True
```
* Evaluar las veces que está un elemento específico 
```python
>>> mi_tupla.count('Rojo')
1
```
* Tupla con un solo elemento 
```python
mi_tupla_unitaria = ('Blanco',)
```
* Empaquetado de tupla, tupla sin paréntesis 
```python
mi_tupla='Gaspar', 5, 8, 1999
```
* Desempaquetado de tupla, se guardan los valores en orden de las variables 
```python
>>> nombre, dia, mes, año = mi_tupla
>>> print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, " - Año: ", año)
Nombre:  Gaspar  - Dia: 5  - Mes:  8  - Año:  1999
```
* Convertir una tupla en una lista 
```python
mi_lista=list(mi_tupla)
```

### Diccionario

Un diccionario tiene una organización de 'clave' y 'valor':

* Crear un diccionario 
```python
mi_diccionario = {  'Colores Primarios': ['Rojo','Azul','Amarillo'], 
                    'Colores secundarios': ['Naranja','Violeta','Verde'], 
                    'Clave3': 10,
                    'Clave4': False}
```
* Imprimir un valor a través de su clave 
```python
>>> print(mi_diccionario['Colores secundarios'])
['Naranja', 'Violeta', 'Verde']
```
* Agregar un valor 
```python
mi_diccionario['Clave5']='Otro ejemplo'
```
* Cambiar un valor 
```python
mi_diccionario['Clave3']=2
```
* Eliminar un elemento de un diccionario a través de su clave 
```python
del mi_diccionario['Clave4']
```
* Utilizar una tupla como clave de un diccionario 
```python
mi_tupla=("Argentina", "Italia", "Inglaterra")
mi_diccionario={mi_tupla[0]:"Buenos Aires", 
                mi_tupla[1]:"Roma", 
                mi_tupla[2]:"Londres"}
```
* Colocar una tupla dentro de un diccionario 
```python
mi_diccionario={'Clave1':'Valor1', 'Clave2':(1,2,3,4,5)}
```
* Colocar una lista dentro de un diccionario (Notar que la diferencia está en el paréntesis '()' y el corchete '[]')
```python
 mi_diccionario={'Clave1':'Valor1', 'Clave2':[1,2,3,4,5]} 
 ```
* Colocar un diccionario dentro de un diccionario 
```python
mi_diccionario={'Clave1':'Valor1', 'Clave2':{'numeros':[1,2,3,4,5]}}
```
* Imprimir las claves del diccionario 
```python
 >>> print(mi_diccionario.keys())
 dict_keys(['Clave1', 'Clave2'])
 ```
* Imprimir los valores del diccionario 
```python
 >>> print(mi_diccionario.values())
 dict_values(['Valor1', {'numeros': [1, 2, 3, 4, 5]}])
 ```
* Imprimir la longitud del diccionario 
```python
 >>> len(mi_diccionario)
 2
 ```
<hr width="75%">
  <p align="center">
  Tips: La funcionalidad **del** permite eliminar cualquier estructura de datos y la funcionalidad **len** permite obtener el tamaño de la estructura de datos
  </p>
<hr width="75%">

* Si tienes dudas sobre este tema, puedes consultarlas en el canal **#m09_errorhandling** de Slack