![HenryLogo](https://henry-11ty-resources.s3.sa-east-1.amazonaws.com/Assets/logo-henry-white-lg.png)

# Introducción a la Programación

## ¿Qué es la Programación?

En la imagen, se representa un pequeño robot abeja en una esquina del cuadrilátero, y en la otra una flor. El objetivo del robot abeja es llegar hasta la flor, esquivando los arbustos que hay de por medio. Para esto, hay que decirle cómo se debe mover, pero puede saltar de a un casillero por vez y la forma en que se le puede "decir" es a travez de instrucciones. Esas instrucciones son "arriba", "abajo", "izquierda" y "derecha". Y por supuesto, teniendo en cuenta que debe moverse dentro del cuadrilátero.

Ahora bien, surgen algunas preguntas:

* ¿Cuántas instrucciones son necesarias?

* Al ser más de una instrucción ¿Es importante el orden en que se ejecutan?

* ¿Hay más de una forma, en que el robot abeja pueda llegar a la flor?

* ¿Hay un camino más óptimo?

* ¿Cómo puedo medir si un camino es más óptimo que otro?

![unaImagenConBoxShadow](../_src/assets/01_imagen01.jpg)

Cualquiera de las siguiente, podrían ser una solución:
* Derecha, Derecha, Arriba, Arriba, Derecha, Derecha, Arriba, Arriba, Arriba, Derecha, Derecha, Arriba
* Derecha, Derecha, Derecha, Derecha, Derecha, Derecha, Arriba, Arriba, Arriba, Izquierda, Izquierda, Arriba, Arriba, Derecha, Arriba, Derecha
* Arriba, Derecha, Derecha, Arriba, Arriba, Arriba, Arriba, Arriba, Derecha, Derecha, Derecha, Derecha, Arriba

Lo importante, en principio, es que notemos que al resolver el problema planteado, lo que estamos haciendo, utilizando un pensamiento lógico, es precisamente, <b>programación</b>

Entonces, <b>programar, es armar una secuencia lógica de pasos a seguir, en pos de cumplir un objetivo.</b> En el ejemplo visto, tuvimos un contexto que nos marcaba las posibilidades y restricciones del problema, por ejemplo moverse dentro del cuadrílatero ó no chocar con los arbustos. Y también un conjunto de instrucciones disponibles, que definian el lenguaje que teníamos que usar, para que el robot comprenda las instrucciones. Lo que usamos fue un lenguaje formal, muy básico y que fue suficiente para resolver el problema. Éstos lenguajes, se denominan lenguajes de programación, nos permiten plasmar esas instrucciones necesarias para darle una solución al problema que queremos resolver, generando así un programa (ó software).

Los primeros lenguajes de programación se escribían en instrucciones que podían interpretar las computadores muy facilmente, pero que resultaban menos amigables a las personas, tales como el lenguaje ensamblador (o Assembler) o Fortran, desarrollado en 1955. Con el tiempo, esto fue cambiando, se fueron desarrolando lenguajes de programación de más alto nivel y con diferentes aplicaciones, que por lo general eran comerciales o científicas, pero tambien con fines educativos, es decir, lenguajes desarrollados para aprender a programar, y consecuentemente, también sea más sencillo. 

Éste último, es el caso de <b>Python</b>, que nace a finales de la década del 80, fue pensado para principiantes por su facilidad de aprendizaje y uso. Su código era compacto pero legible. Con el correr de los años fue incluyendo mejoras hasta llegar tambien a ser de licencia libre. Hoy por hoy, es usado desde en simples "scripts", hasta grandes servidores web que proveen servicio ininterrumpido las 24hs. Es utilizado para la programación de interfaces gráficas y bases de datos. Además tiene una amplia aceptación por científicos que hacen aplicaciones para las supercomputadores más rápidas del mundo y por los niños que recién están comenzando a programar.

## Sintaxis

Para el ejemplo se uso un lenguaje con el que era posible determinar los pasos a seguir por el robot abeja hasta llegar a la flor, y nos fue suficiente para poder entender como resolveríamos el problema. El hecho es que, los lenguajes de programación que utilizamos, deben ser más específicos todavía, necesitamos tener un nivel de detalle mayor en nuestras instrucciones, por ejemplo, en lugar de la instruccion "Arriba", podría ser, especificar la cantidad de celdas que hay que moverse, e incluso qué implica "moverse", que seguramente será cambiar el estado de la propia abeja. Por otro lado tambien habrá un marco de referencia, es decir, el tablero de juego, en sí mismo, es una estructura de datos que debemos conocer, saber donde hay ubicado un arbusto y donde no, saber cuales son los límites, y que pasa si con las instrucciones que le damos a la abeja, hacemos que rebase esos límites. 
Para solventar esa complejidad, necesitamos un set de instrucciones un poco más complejo y tener la posibilidad de representar esas estructuras de datos, es decir, representar la realidad, de hecho, todos los datos son una representación de la realidad.
La sintaxis de un programa, consiste en un conjunto de palabras reservadas a instrucciones específicas, con una estructura específica, tal y como funciona un lenguaje como el que usamos los humanos para comunicarnos, como el español o el inglés. Los lenguajes de programación tambien tienen su sintaxis, que esta compuesta por diferentes elementos, como ser variables para representar el dato de la realidad, sentencias para representar las instrucciones ó estructuras de control que conforman el cuerpo del programa.

## Variables

Una variable es un espacio de memoria donde guardamos un dato, ese espacio de memoria a la vez recibe un nombre:

![unaImagenConBoxShadow](../_src/assets/02_imagen01.jpg)

## Tipos de Datos
## Operaciones entre Variables




```python
```