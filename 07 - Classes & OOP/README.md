![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

## Clases y objetos (POO)

El alto grado de planificación y previsión que requiere la programación es contrario a la propia realidad. El hombre aprende y crea a través de la experimentación, no de la planeación. La Orientación a Objetos (POO) brinda estos métodos de experimentación, y logra que los lenguajes sean de más alto nivel, es decir, más cercanos a como los humanos pensamos el mundo. Es decir, vemos la realidad como objetos que se interrelacionan y realizan acciones, y esto, es lo que se intenta emular en la POO.
Hasta 1966 la programación fue exclusivamente lineal, hasta que surgieron lenguajes como Simula, SmallTalk, C++, Ada, Delphi o Java. Hoy el lenguaje más popular es Python y su filosofía hace hincapié en la legibilidad de su código. 

### Objeto

Una estructura de datos que eventualmente tiene funciones asociadas, que están agrupados por razones de consistencia y comodidad conforman un **objeto**.
En la composición de un objeto tenemos entonces **propiedades** (datos) y **métodos** (funciones asociadas).

### Clase

Hay una diferencia muy importante entre un objeto y una variable, y es que mientras que la variable 'se crea', el objeto 'se instancia', lo que implica, ademas de su creación propiamente dicha, que su creación se realiza en base a una definición preliminar, disponibilizando en memoria, no solo la estructura de datos asociada sino sus métodos. Por medio de esta mecánica, además, se puede instanciar más de un solo objeto con la misma definicion. Esta definición, es una generalización del objeto, es decir que especifica que estructura de datos va a tener y qué métodos asociados. Esto lo que se conoce como **clase**

### Pilares de la Programación Orientada a Objetos

* **Abstracción**: Es cuando separamos los datos de un objeto para luego generar un molde (una clase).
* **Encapsulamiento**: Se utiliza cuando es necesario que ciertos métodos o propiedades sean inviolables o inalterables.
Un ejemplo del encapsulamiento podría ser una cuenta de banco, donde el usuario no puede simplemente aumentar su balance de dinero, si no que debe depender de unos métodos previamente validados para aumentar dicho balance (depósitos, transferencias, etc).
* **Herencia**: Permite crear nuevas clases a partir de otras. Si tuviéramos una clase “Autos” y quisiéramos crear unas clases “Auto deportivo” o “Auto clásico”, podríamos tomar varias propiedades y métodos de la clase “Autos”. Esto nos da una jerarquía de padre e hijo.
* **Polimorfismo**: Proviene de Poli = muchas, morfismo = formas. Se utiliza para crear métodos con el mismo nombre pero con diferente comportamiento.

### Ejemplos:

* Clase Animal<br>
&nbsp;&nbsp;- Especie<br>
&nbsp;&nbsp;- Edad<br>
&nbsp;&nbsp;- Color<br>
&nbsp;&nbsp;- Correr()<br>
&nbsp;&nbsp;- Dormir()<br>

Se instancian distintos objetos a partir de una clase:

* Objeto1<br>
&nbsp;&nbsp;- Especie: 'Perro'<br>
&nbsp;&nbsp;- Edad: 3<br>
&nbsp;&nbsp;- Color: 'Blanco'<br>
&nbsp;&nbsp;- Correr()<br>
&nbsp;&nbsp;- Dormir()<br>

* Objeto2
&nbsp;&nbsp;- Especie: 'Caballo'<br>
&nbsp;&nbsp;- Edad: 8<br>
&nbsp;&nbsp;- Color: 'Marrón'<br>
&nbsp;&nbsp;- Correr()<br>
&nbsp;&nbsp;- Dormir()<br>

* A partir de la sentencia **class** y el nombre de creamos la clase.
* La función **__init__()** es el **constructor** de la clase, esta función se ejecuta cuando se instancia el objeto.
* La clase posee atributos (especie, edad, color) y métodos que manipulan esos atributos (mePresento, cumplirAños).

``` python
>>> class Animal:
>>> '''
>>> En esta clase se crean los animales
>>> '''
>>> def __init__(self, especie, edad, color):
>>>     self.especie = especie
>>>     self.edad = edad
>>>     self.color = color
>>> def mePresento(self):
>>>     print('Hola, soy ', self.especie, ', de color', self.color, ' y tengo ', self.edad, ' años')
>>> def cumplirAños(self):
>>>     self.edad = self.edad + 1
>>> 
>>> a1 = Animal('Ratón', 2, 'Marrón')
>>> print(a1.especie)
Ratón
>>> print(a1.edad)
2
>>> a2 = Animal('Liebre', 3, 'Gris')
>>> print(a2.especie)
Liebre
>>> print(a2.edad)
3
``` 

Creamos los objetos a1 y a2. Al hacerlo se envían los parámetros de inicialización de sus atributos.
Utilizamos sus métodos para mostrar los atributos y/o modificarlos.
Este formato de clases, objetos, métodos y parámetros es muy común en Python y lo utilizamos cada vez que invocamos alguna de sus **librerías**

``` python
>>> a1.mePresento()
Hola, soy  Ratón , de color Marrón  y tengo  2  años
>>> a2.mePresento()
Hola, soy  Liebre , de color Gris  y tengo  3  años
>>> a1.cumplirAños()
>>> a1.mePresento()
Hola, soy  Ratón , de color Marrón  y tengo  3  años
```

## Librerías

Las librerías son proyectos con metodos o funciones puntuales, el cual es posible anexar a otros proyectos y complementarlo usando sus metodos especificos para una determinada solución. Son trozos de código hechos por terceros. Facilita mucho la programación y hace que nuestro programa sea más sencillo de hacer y luego de entender. También llamadas 'Frameworks', consiste en archivos de código a los que se invoca al proncipio de nuestro propio código.

### Módulos

Un módulo en Python es un archivo con extensión ".py" que alberga un conjunto de funciones, variables o clases y que puede ser usado por otros módulos. Nos permiten reutilizar código y organizarlo mejor en namespaces. Por ejemplo, podemos definir un módulo mimodulo.py con dos funciones suma() y resta().


``` python
>>> # mimodulo.py
>>> def suma(a, b):
>>>     return a + b
>>> 
>>> def resta(a, b):
>>>     return a - b
```

Una vez definido, dicho módulo puede ser usado o importado en otro código usando **import**, con lo que se puede acceder a todo el contenido.

``` python
>>> # otromodulo.py
>>> import mimodulo
>>> 
>>> print(mimodulo.suma(4, 3))
7
>>> print(mimodulo.resta(10, 9))
1
``` 

También podemos importar únicamente los componentes que nos interesen como mostramos a continuación.

``` python
>>> from mimodulo import suma, resta
>>> 
>>> print(suma(4, 3))   # 7
>>> print(resta(10, 9)) # 1
```

Por último, podemos importar todo el módulo haciendo uso de *, sin necesidad de usar mimodulo.*.

``` python
>>> from mimodulo import *
>>> 
>>> print(suma(4, 3))
7
>>> print(resta(10, 9))
1
```

### Consideraciones

Los módulos o librerías, permiten que Python pueda ser utilizado en diferentes entornos:

- **Desarrollo Web**: Existen frameworks como Django, Pyramid, Flask o Bottle que permiten desarrollar páginas web a todos los niveles.
- **Ciencia y Educación**: Debido a su sintaxis tan sencilla, es una herramienta perfecta para enseñar conceptos de programación a todos los niveles. En lo relativo a ciencia y cálculo numérico, existen gran cantidad de librerías como SciPy o Pandas.
- **Desarrollo de Interfaces Gráficos**: Gran cantidad de los programas que utilizamos tienen un interfaz gráfico que facilita su uso. Python también puede ser usado para desarrollar GUIs con librerías como Kivy o pyqt.
- **Desarrollo Software**: También es usado como soporte para desarrolladores, como para testing.
- **Machine Learning**: En los último años ha crecido el número de implementaciones en Python de librerías de aprendizaje automático como Keras, TensorFlow, PyTorch o sklearn.
- **Visualización de Datos**: Existen varias librerías muy usadas para mostrar datos en gráficas, como matplotlib, seaborn o plotly.
Finanzas y Trading: Gracias a librerías como QuantLib o qtpylib y a su facilidad de uso, es cada vez más usado en estos sectores.

### Rutas y Uso de sys.path

Normalmente los módulos que importamos están en la misma carpeta, pero es posible acceder también a módulos ubicados en una subcarpeta. Imaginemos la siguiente estructura:

``` bash
.
├── ejemplo.py
├── carpeta
│   └── modulo.py
```

Donde modulo.py contiene lo siguiente:

``` python
>>> # modulo.py
>>> def hola():
>>> 	print("Hola")
```

Desde nuestro ejemplo.py, podemos importar el módulo modulo.py de la siguiente manera:

``` python
>>> from carpeta.modulo import *
>>> print(hola())
Hola
```

Es importante notar que Python busca los módulos en las rutas indicadas por el **sys.path**. Es decir, cuando se importa un módulo, lo intenta buscar en dichas carpetas. Puedes ver tu sys.path de la siguiente manera:

``` python
>>> import sys
>>> print(sys.path)
```

Como es obvio, verás que la carpeta de tu proyecta está incluida, pero ¿y si queremos importar un módulo en una ubicación distinta? Pues bien, podemos añadir al sys.path la ruta en la que queremos que Python busque.

``` python
>>> import sys
>>> sys.path.append(r'/ruta/de/tu/modulo')
``` 

Una vez realizado esto, los módulos contenidos en dicha carpeta podrán ser importados sin problema como hemos visto anteriormente.

Por otro lado, es posible cambiar el nombre del módulo usando **as**. Imaginemos que tenemos un módulo moduloconnombrelargo.py.

``` python
>>> # moduloconnombrelargo.py
>>> hola = "hola"
```

En vez de usar el siguiente import, tal vez queramos asignar un nombre más corto al módulo.

``` python
>>> import moduloconnombrelargo
>>> print(moduloconnombrelargo.hola)
```

Podemos hacerlo de la siguiente manera con as:

``` python
>>> import moduloconnombrelargo as m
>>> print(m.hola)
``` 

La función **dir()** nos permite ver los nombres (variables, funciones, clases, etc) existentes en nuestro namespace. Si probamos en un módulo vacío, podemos ver como tenemos varios nombres rodeados de __. Se trata de nombres que Python crea por debajo.

``` python
>>> print(dir())
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
```

Por ejemplo, __file__ es creado automáticamente y alberga el nombre del archivo .py.

``` python
>>> print(__file__)
/tu/ruta/tufichero.py
```

Imaginemos ahora que tenemos alguna variable y función definida en nuestro script. Como era de esperar, dir() ahora nos muestra también los nuevos nombres que hemos creado, y que por supuesto pueden ser usados.

``` python
>>> mi_variable = "Python"
>>> def mi_funcion():
>>>     pass
>>> print(dir())
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'mi_funcion', 'mi_variable']
``` 

Por último, vamos a importar el contenido de un módulo externo. Podemos ver que en el namespace tenemos también los nombres resta y suma, que han sido tomados de mimodulo.

``` python
>>> from mimodulo import *
>>> print(dir())
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'resta', 'suma']
```

El uso de dir() también acepta parámetros de entrada, por lo que podemos por ejemplo pasar nuestro modulo y nos dará más información sobre lo que contiene.

``` python
>>> import mimodulo
>>> print(dir(mimodulo))
['__builtins__', '__cached__', '__doc__', '__file__','__loader__', '__name__', '__package__', '__spec__', 'resta', 'suma']
>>> print(mimodulo.__name__)
mimodulo
>>> print(mimodulo.__file__)
/tu/ruta/mimodulo.py
```

Importar un módulo puede lanzar la excepción "ImportError", cuando se intenta importar un módulo que no ha sido encontrado. Se trata de ModuleNotFoundError.

``` python
>>> import moduloquenoexiste
ModuleNotFoundError: No module named 'moduloquenoexiste'
``` 

Dicha excepción puede ser capturada para evitar la interrupción del programa.
Un problema muy recurrente es cuando creamos un módulo con una función como en el siguiente ejemplo, y añadimos algunas sentencias a ejecutar.

``` python
>>> # modulo.py
>>> def suma(a, b):
>>>     return a + b
>>> c = suma(1, 2)
>>> print("La suma es:", c)
```

Si en otro módulo importamos nuestro modulo.py, tal como está nuestro código el contenido se ejecutará, y esto puede no ser lo que queramos.


``` python
>>> # otromodulo.py
>>> import modulo
La suma es: 3
```

Dependiendo de la situación, puede ser importante especificar que únicamente queremos que se ejecute el código si el módulo es el __main__. Con la siguiente modificación, si hacemos import modulo desde otro módulo, este fragmento ya no se ejecutará al ser el módulo main otro.

``` python
>>> # modulo.py
>>> def suma(a, b):
>>>     return a + b
>>> if (__name__ == '__main__'):
>>>     c = suma(1, 2)
>>>     print("La suma es:", c)
```

Es importante notar que los módulos solamente son cargados una vez. Es decir, no importa el número de veces que llamemos a import mimodulo, que sólo se importará una vez.
Si queremos que el módulo sea recargado, tenemos que ser explícitos, haciendo uso de reload.

``` python
>>> import mimodulo
>>> import importlib
>>> importlib.reload(mimodulo)
>>> importlib.reload(mimodulo)
``` 

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