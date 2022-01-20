![HenryLogo](https://henry-11ty-resources.s3.sa-east-1.amazonaws.com/Assets/logo-henry-white-lg.png)

## Variables

Una variable es un espacio de memoria donde guardamos un dato, ese espacio de memoria a la vez recibe un nombre:

![unaImagenConBoxShadow](../_src/assets/02_imagen01.jpg)

Y esto conforma la estructura de datos más simple que podemos encontrar.

Por otro lado existen ciertas normas a la hora de nombrar variables:

* El nombre no puede empezar con un número
* No se permite el uso de guiones del medio -
* No se permite el uso de espacios.
* No usar nombres reservados para Python. Las palabras reservadas son utilizadas por Python internamente, por lo que no podemos usarlas para nuestras variables o funciones.

### Constantes

Sin embargo, cuando ese dato no lo alojamos en una variable y lo utilizamos directamente, recibe el nombre de constante.

### Tipos de Datos

Es importante notar, que podemos encontrarnos con datos de tipos distintos, es decir numéricos, alfanuméricos o booleanos.

En Python tenemos los siguientes:
 * Enteros: El conjunto de números enteros
 * Floats: El conjunto de números reales o de punto flotante
 * Cadenas o Strings: Es texto, caracteres alfanuméricos que se introducen entre comillas dobles o simples
 * Booleanos: Representan Verdadero ó Falso
 * Complejos: El conjunto de números complejos

Todo valor que pueda ser asignado a una variable tiene asociado un tipo de dato y esto establece qué operaciones se pueden realizar sobre la misma.

### Operaciones entre Variables

Con diferentes tipos de datos podemos hacer diferentes tipos de operaciones. Y hay operaciones no permitidas entre variables de diferentes tipos de datos.

Tipos de datos numéricos:

| Operacion | Operador | Ejemplo |
| :---      |  :----:  |    ---: |
| Suma      | + | 3 + 5.5 = 8.5 |
| Resta   | -  | 4 - 1 = 3  |
| Multiplicación | *  | 4 * 2 = 8  |
| Potenciación | 4<sup>2</sup>  | 4**2 = 16  |
| División (Cociente) | /  | 4 / 2 = 2  |
| División (parte entera) | //  | 14 // 3 = 4  |
| División (resto) | %  | 14 % 3 =  2 |

Operadores relacionales

| Operacion | Operador | Ejemplo |
| :---      |  :----:  |    ---: |
| == | Igual | 10 == 3 = False |
| != | Distinto | 10 != 3 = True |
| >	| Mayor	| 10 > 3 = True |
| < | Menor	| 10 < 3 = False |
| >= | Mayor o igual | 10 >= 3 = True |
| <= | Menor o igual | 10 <= 3 = False |

Operaciones de asignación:

| Operacion | Operador | Ejemplo |
| :---      |  :----:  |    ---: |
| =   | x=7  | x=7  |
| +=  | x+=2  | x=x+2 = 9  |
| -=  | x-=2  | x=x-2 = 5  |
| *=  | x*=2  | x=x*2 = 14  |
| /=  | x/=2  | x=x/2 = 3.5  |
| %=  | x%=2  | x=x%2 = 1  |
| //=  | x//=2  | x=x//2 = 3  |
| **=  | x**=2  | x=x**2 = 49  |
| &=  | x&=2  | x=x&2 = 2  |
| ^=  | x^=2  | x=x^2 = 5  |
| >>=  | x>>=2  | x=x>>2 = 1  |
| <<= | x<<=2 | x=x<<=2 = 28  |


Operacion: |=   <br>
Operador: x|=2  <br>
Ejemplo: x=x|2 = 7  <br>

Cuando tratamos con texto, podemos hacer otras operaciones:

| Operacion | Operador | Ejemplo |
| :---      |  :----:  |    ---: |
| Concatenar | + | 'hola ' + 'mundo !' = 'hola mundo!' |
| Multiplicar | * | 'ja ' + 3 = 'ja ja ja' |

Algunos ejemplos en Python:

```python
>>> a = 'Hola '
>>> b = 'Mundo !'
>>> print(a + b)
Hola Mundo !

>>> x = 3
>>> y = 12
>>> print(x + y)
15

>>> print(a + x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_18232/136165486.py in <module>
----> 1 print(a + x)

TypeError: can only concatenate str (not "int") to str
```

Notar que en la operaciones que no están permitidas arroja un error, que es muy descriptivo. En este caso no es posible sumar un valor entero con un valor alfanumérico.

```python
>>> # Dividir "y" entre "x"
>>> y = 9
>>> x = 3
>>> print(y/x)
3.0

>>> # Potencia de "y" elevado a la "x"
>>> y = 2
>>> x = 4
>>> print(y**x)
16

>>> # Devolver el resto de la división
>>> y = 13
>>> x = 3
>>> print(y%x)
1
```

Notar que anteponiendo el caracter numeral (#) es posible agregar comentarios en el código.

Operaciones Lógicas

Son operaciones en las que entran en uso el tipo de datos booleano, es decir, que nos permiten representar valores verdadero ó falso. Para verlo mejor, es necesario recurrir a lo que llamamos tablas de verdad.
Veremos muy comunmente representar verdadero con un "1" y falso con un "0".

Tabla del operador lógico "and", se verifican que A y B sean verdaderas.  
| A | B | A and B |
| :- | :--: | -: |
| 1 | 0 | 0 |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

Tabla del operador lógico "or", se verifican que A ó B sean verdaderas. 
| A | B | A or B |
| :- | :--: | -: |
| 1 | 0 | 1 |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

Tambien es posible representar la negación, con el operador not()

Tabla del operador lógico "Or Exclusiva", se verifica ((A and not(B)) or (not(A) and B))
| A | B | A "or exclusiva" B |
| :- | :--: | -: |
| 1 | 0 | 1 |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

## Homework

Completa la tarea descrita en el archivo [README](https://github.com/soyHenry/Prep-Course/tree/main/02-JS-I/homework)

<table class="hide" width="100%" style='table-layout:fixed;'>
  <tr>
    <td>
      <a href="https://airtable.com/shrSzEYT4idEFGB8d?prefill_clase=00-PrimerosPasos">
        <img src="https://static.thenounproject.com/png/204643-200.png" width="100"/>
        <br>
        Hacé click acá para dejar tu feedback sobre esta clase.
      </a>
    </td>
  </tr>
</table>