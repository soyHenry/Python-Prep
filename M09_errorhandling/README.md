![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

## Manejo de Errores

### Pruebas de caja negra

Las pruebas de caja negra se basan en la especificación de la función o el programa, aquí debemos probar sus inputs y validar los outputs. Se llama caja negra por que no necesitamos saber necesariamente los procesos internos del programa, solo contrastar sus resultados.
Hay dos tipos de pruebas muy importantes:
* Pruebas Unitarias: se realizan pruebas a cada uno de los módulos para determinar su correcto funcionamiento.
* Pruebas de Integración: se valida que todos los módulos funcionan entre sí.

Es una buena práctica realizar las pruebas antes de crear código, esto es porque cualquier cambio que se realice a futuro los test estarán incorporados para determinar si los cambios cumplen lo esperado.
En Python existe la posibilidad de realizar estas pruebas gracias a la librería **unittest**.

```python
>>> import unittest
>>>
>>> def suma(num_1, num_2):
>>>     return num_1 + num_2
>>>
>>> class CajaNegraTest(unittest.TestCase):
>>> 
>>>     def test_suma_dos_positivos(self):
>>>         num_1 = 10
>>>         num_2 = 5
>>> 
>>>         resultado = suma(num_1, num_2)
>>> 
>>>         self.assertEqual(resultado, 15)
>>> 
>>>     def test_suma_dos_negativos(self):
>>>         num_1 = -10
>>>         num_2 = -7
>>> 
>>>         resultado = suma(num_1, num_2)
>>> 
>>>         self.assertEqual(resultado, -17)
>>>
>>> unittest.main(argv=[''], verbosity=2, exit=False)
test_suma_dos_negativos (__main__.CajaNegraTest) ... ok
test_suma_dos_positivos (__main__.CajaNegraTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.004s

OK
<unittest.main.TestProgram at 0x2226bd08400>
``` 

### Pruebas de caja de cristal

Se basan en el flujo del programa, por lo que se asume que conocemos el funcionamiento del programa, por lo que podemos probar todos los caminos posibles de una función. Esto significa que vamos a probar las ramificaciones, bucles for y while, recursiónes, etc.
Este tipo de pruebas son muy buenas cuando descubrimos un bug cuando corremos el programa, por lo que vamos a buscar el **bug** ó error de código gracias a que conocemos su estructura.

```python
>>> import unittest

>>> def es_mayor_de_edad(edad):
>>>     if edad >= 18:
>>>         return True
>>>     else:
>>>         return False

>>> class PruebaDeCristalTest(unittest.TestCase):
>>> 
>>>     def test_es_mayor_de_edad(self):
>>>         edad = 20
>>> 
>>>         resultado = es_mayor_de_edad(edad)
>>> 
>>>         self.assertEqual(resultado, True)
>>> 
>>>     def test_es_menor_de_edad(self):
>>>         edad = 15
>>> 
>>>         resultado = es_mayor_de_edad(edad)
>>> 
>>>         self.assertEqual(resultado, False)

>>> unittest.main(argv=[''], verbosity=2, exit=False)
test_es_mayor_de_edad (__main__.PruebaDeCristalTest) ... ok
test_es_menor_de_edad (__main__.PruebaDeCristalTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
<unittest.main.TestProgram at 0x2226bd153d0>
```

### Seguir el código paso a paso ó 'Debugging'

Los bugs son un problema que les sucede a todos, sin embargo si realizamos test a nuestro programa probablemente tendremos menos bugs, pero esto no es suficiente.
Existen unas reglas generales que nos ayudaran:
* Aprende a utilizar el print statement.
* Estudia los datos disponibles.
* Utiliza los datos para crear hipótesis y experimentos. Método científico.
* Ten una mente abierta. Si entendes el programa, probablemente no habrán bugs.
* Lleva un registro de lo que has tratado, preferentemente en la forma de tests.
* Debuguear es un proceso de búsqueda de los bugs, por lo que al diseñar nuestros experimentos debemos acotar el espacio de búsqueda en cada prueba. Una forma ágil de debugear es utilizando una búsqueda binaria con print statements, esto significa que ejecutamos la mitad del código, si no falla entonces sabemos que el problema está en la otra mitad, y en cada área que vamos acortando lo dividimos por mitades, de esta forma hallaremos rápidamente nuestro bug.

Existe un listado de errores comunes de los cuales también nos podemos apoyar:
* Encuentra a los sospechosos comunes (llamado a una función mal escrita, parámetros en orden incorrecto, etc.)
* En lugar de preguntarte por qué un programa no funciona, pregúntate por qué está funcionando de esta manera.
* Es posible que el bug no se encuentre donde crees que está.
* Explícale el problema a otra persona. De preferencia que no tenga contexto.
* Lleva un registro de lo que has tratado, preferentemente en la forma de tests.

### Manejo de excepciones

Los manejos de excepciones son muy comunes en la programación, no tienen nada de excepcional. Las excepciones de Python normalmente se relacionan con errores de semántica, también podemos crear nuestras propias excepciones, pero cuando una excepción no se maneja (unhandled exception), el programa termina en error.

Las excepciones se manejan con los keywords: **try**, **except**, **finally**. Se pueden utilizar también para ramificar programas.
No deben manejarse de manera silenciosa (por ejemplo, con print statements). Para crear tu propia excepción utiliza el keyword **raise**.

``` python
>>> def divide_elementos_de_lista(lista, divisor):
>>>     '''
>>>     Cada elemento de una lista es dividida por un divisor definido.
>>>     En caso de error de tipo ZeroDivisionError que
>>>     significa error al dividir en cero
>>>     la función devuelve la lista inicial
>>>     '''
>>>     try:
>>>         return [i / divisor for i in lista]
>>>     
>>>     except ZeroDivisionError as e:
>>>         print(e)
>>>         return lista
>>> 
>>> lista = list(range(10))
>>> divisor = 0
>>> 
>>> print(divide_elementos_de_lista(lista, divisor))
division by zero
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> divisor = 3
>>> print(divide_elementos_de_lista(lista, divisor))
[0.0, 0.3333333333333, 0.6666666666666, 1.0, 1.3333333333333, 1.6666666666667, 2.0, 2.3333333333335, 2.6666666666665, 3.0]
```

### Excepciones y control de flujo

Hasta ahora hemos visto como las excepciones nos permiten controlar los posibles errores que pueden ocurrir en nuestro código. Sin embargo, dentro de la comunidad de Python tienen otro uso: control de flujo.

¿Por qué es necesaria otra modalidad para controlar el flujo? Una razón muy específica: el principio EAFP (easier to ask for forgiveness than permission, es más fácil pedir perdón que permiso, por sus siglas en inglés).

El principio EAFP es un estilo de programación común en Python en el cual se asumen llaves, índices o atributos válidos y se captura la excepción si la suposición resulta ser falsa. Es importante resaltar que otros lenguajes de programación favorecen el principio LBYL (look before you leap, revisa antes de saltar) en el cual el código verifica de manera explícita las precondiciones antes de realizar llamadas.

``` python
#Python
def busca_pais(paises, pais):
'''
Paises es un diccionario. Pais es la llave.
Codigo con el principio EAFP.
'''

try:
    return paises[pais]
except KeyError:
     return None
```

``` javascript
// Javascript

/**
* Paises es un objeto. Pais es la llave.
* Codigo con el principio LBYL.
*/
function buscaPais(paises, pais) {
  if(!Object.keys(paises).includes(pais)) {
    return null;
  }

  return paises[pais];
}
``` 

Como se puede ver, el código de Python accede directamente a la llave y únicamente si dicho acceso falla, entonces se captura la excepción y se provee el código necesario. En el caso de JavaScript, se verifica primero que la llave exista en el objeto y únicamente con posterioridad se accede.

Es importante resaltar que ambos estilos pueden utilizarse en Python, pero el estilo EAFP es mucho más propio de este lenguaje.

``` python
#All possible errors

except TypeError:
    print("is thrown when an operation or function is applied to an object of an inappropriate type.")
except IndexError:
   	print("is thrown when trying to access an item at an invalid index.")
except KeyError:
    print("is thrown when a key is not found.")
except ImportError:
  	print("Raised when the imported module is not found.")
except StopIteration:
  	print("is thrown when the next() function goes beyond the iterator items.")
except ValueError:
  	print("is thrown when a function's argument is of an inappropriate type.")
except NameError:
  	print("is thrown when an object could not be found.")	
except ZeroDivisionError:
  	print("is thrown when the second operator in the division is zero.")
except KeyboardInterrupt:
  	print("is thrown when the user hits the interrupt key (normally Control-C) during the execution of the program.")
except MemoryError:
  	print("Raised when an operation runs out of memory.")
except FloatingPointError:
  	print("Raised when a floating point operation fails.")
except OverflowError:
  	print("Raised when the result of an arithmetic operation is too large to be represented.")
except ReferenceError:
  	print("Raised when a weak reference proxy is used to access a garbage collected referent.")
except TabError:
  	print("Raised when the indentation consists of inconsistent tabs and spaces.")
except SystemError:
  	print("Raised when the interpreter detects internal error.")
except RuntimeError:
  	print("Raised when an error does not fall under any other category.")
except:
 	print("Error detected can't be handled nor clasified.")
```

## Afirmaciones

Las afirmaciones son un mecanismo en la que podemos determinar si una afirmación se cumple o no se cumple y poder seguir adelante con la ejecución de nuestro programa o darle término.
Consiste en un método de programación defensiva, esto significa que nos estamos preparando para verificar que los tipos de inputs de nuestro programa es del tipo que nosotros esperamos. Estos también nos sirven para debuggear.
Para realizar una afirmación en nuestro programa lo hacemos con la expresión assert (expresion booleana), (mensaje de error).

``` python
>>> def primera_letra(lista_de_palabras):
>>>   primeras_letras = []
>>> 
>>>   for palabra in lista_de_palabras:
>>>     assert type(palabra) == str, f'{palabra} no es str'
>>>     assert len(palabra) > 0, 'No se permiten str vacíos'
>>> 
>>>     primeras_letras.append(palabra[0])
>>>   return primeras_letras
```

## Características de Python

- Es un lenguaje interpretado, no compilado.
- Usa tipado dinámico, lo que significa que una variable puede tomar valores de distinto tipo.
- Es fuertemente tipado, lo que significa que el tipo no cambia de manera repentina. Para que se produzca un cambio de tipo tiene que hacer una conversión explícita.
- Es multiplataforma, ya que un código escrito en macOS funciona en Windows o Linux y viceversa.


* Si tienes dudas sobre este tema, puedes consultarlas en el canal **#m9_errorhandling** de Slack

