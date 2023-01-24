![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

<!--# ANALYTICS:-->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-161500899-3">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-161500899-3');
</script>

<!--# GOOGLE TAG MANAGER-->
<!--# HEAD-->
<!-- Google Tag Manager -->
<script>
  (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-5Z2JFWV');
</script>
<!-- End Google Tag Manager -->
<!--# BODY-->
<!-- Google Tag Manager (noscript) -->
<noscript>
  <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5Z2JFWV"
height="0" width="0" style="display:none;visibility:hidden">
  </iframe>
</noscript>
<!-- End Google Tag Manager (noscript) -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LHV5X0V6Y9"><script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-LHV5X0V6Y9');
</script>

# Primeros Pasos

## Grabación de la Clase 1

<div class="iframeContainer">
  <iframe src="https://player.vimeo.com/video/683356760" allow="autoplay; fullscreen" allowfullscreen></iframe>
</div>

#### Preparando tu computadora
Antes de comenzar deberás descargar en tu computadora las siguientes herramientas de trabajo:
1. Editor de texto
2. Git
3. Github
4. Python

Luego deberás realizar la clonación del [repositorio](https://github.com/soyHenry/Python-Prep). Te explicamos cómo hacerlo en el tutorial: 


<div class="iframeContainer">
  <iframe src="https://player.vimeo.com/video/638636752" title="Instructivo de Primeros Pasos" allow="autoplay; fullscreen"></iframe>
</div>

> **Importante**: Github cambió el método de autenticación, ahora es por PAT (Personal Access Token), para crearlo pueden seguir este [link](https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Pueden elegir expiration infinita para hacerlo una sóla vez.

## SLACK

Slack es una plataforma de comunicación que utilizamos en Henry para estar conectados. Por este medio podrás recibir comunicados y mantener conversaciones con toda la comunidad de Henry. 

### ¿Cómo usar SLACK?

A continuación te mostramos cómo funciona: 
<div class="iframeContainer">
 <iframe src="https://player.vimeo.com/video/548902078?h=e82a766bab&title=0&byline=0&portrait=0&speed=0&badge=0&autopause=0&player_id=0&app_id=58479" width="1264" height="720" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Prep Course - Intro a Slack"></iframe>
</div>

Para ingresar al espacio de Slack del Prep Course de Henry, por favor revisa el los mails que recibiste al avanzar con el proceso de admisión dado que ahí encontrarás el link de acceso

> Gracias [Nico Constantin (FT#12)](https://github.com/NicoConstantin) por el video y la explicación!

## Editores de Texto

Para poder escribir código que pueda ser interpretado por un lenguaje de programación, necesitamos utilizar un editor de texto.

Hay varios, puedes probarlos y optar por el que te sientas más a gusto.

A continuación veremos una lista de los más populares:

## Sublime Text

![Sublime Text](/_src/assets/00-PrimerosPasos/sublimeText_screen.png)

Es un editor de texto liviano, que cuenta con una serie de plugins para adaptarlo a las necesidades de cada desarrollador.

Es multiplataforma, por lo que se puede instalar tanto en Windows, como Linux y OS X.

Para instalarlo, realizaremos los siguientes pasos:

#### En Windows o en OS X

1. Nos dirigimos a la página oficial de [Sublime Text](https://www.sublimetext.com).

2. Al ingresar, detectará automáticamente el sistema operativo que tenemos, y nos sugerirá descargar el instalador apropiado.

3. Presionamos el botón **_Download_**.

4. Elegimos la opción adecuada según nuestro sistema operativo e iniciamos la descarga.

![Sublime Text Download](/_src/assets/00-PrimerosPasos/sublimeText_download.png)

5. Finalizada la descarga, ejecutamos el instalador, seleccionamos las opciones **_siguiente, siguiente, etc_**, hasta completar el proceso.

#### En Linux, en la distribución Ubuntu y derivados

1. Nos dirigimos al sitio oficial de Sublime Text. Aquí encontrarás las instrucciones para instalarlo:

[Descargar Sublime Text para Linux](https://www.sublimetext.com/docs/3/linux_repositories.html)

2. En la terminal, ejecutamos el siguiente comando, para instalar la clave GPG:

```shell
wget -q0 - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

3. Para asegurarnos de que `apt` esté configurado para trabajar con orígenes https, ejecutamos:

```shell
sudo apt-get install apt-transport-https
```

4. Luego para agregar el repositorio estable, ejecutamos:

```shell
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

5. Finalmente, procedemos a instalar el programa:

```shell
sudo apt-get install sublime-text
```

Ahora, si en el **Menú de inicio** buscamos **Sublime text**, veremos la siguiente imagen:

![Sublime Text Linux](/_src/assets/00-PrimerosPasos/sublimeText_linux.png)

## Atom

![Atom Site](/_src/assets/00-PrimerosPasos/atom_site.png)

Es un editor de código abierto, disponible tanto para Windows, como Linux y para OS X.

Tiene integrada una consola de Git y Github, para llevar un control de versiones de tus proyectos.
Para comenzar el proceso de instalación, realizamos los siguientes pasos:

En Windows, Linux o en OS X, nos dirigimos al sitio oficial, mediante el siguiente enlace:

<https://atom.io/>

Al ingresar, el navegador detecta automáticamente el instalador que necesitamos bajar, según nuestro sistema operativo.

Allí, presionamos el botón Download para almacenarlo en nuestra computadora.

#### En Windows

Una vez finalizada la descarga, hacemos doble click en el instalador y esperamos a que finalice el proceso de instalación.

#### En Ubuntu y derivados

Descomprimimos el instalador, hacemos doble click, y nos dirigimos a: `/usr/bin/atom`

Al hacer doble click, se abrirá el editor.

## Visual Studio Code

![VSC Console](/_src/assets/00-PrimerosPasos/vsc_console.png)

Es un editor desarrollado por Microsoft.

Tiene integrado el control de versiones mediante Git y Github para tener un seguimiento de tus proyectos. Brinda una cantidad de extensiones que facilitan el trabajo de un desarrollador.

Para descargarlo, nos dirigimos al sitio oficial, en la sección Download y descargamos el instalador según nuestro Sistema Operativo:

<https://code.visualstudio.com/download>

![VSC Download](/_src/assets/00-PrimerosPasos/vsc_download.png)

Una vez finalizada la descarga, procedemos a ejecutar el instalador.

## Git

### ¿Qué es Git?

Git es un sistema de control de versiones, distribuido y open source. Un control de versiones es un sistema que registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo, de modo que puedas recuperar versiones específicas más adelante.

### Instalación

#### Para Mac y Linux

Ver estos enlaces:

<https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git>

<https://www.youtube.com/watch?v=PSULlxUk744>

<https://www.youtube.com/watch?v=oV0spTF71AI>

#### Para Windows

Ingreso a <https://git-scm.com> y descargo la última versión.

![installGit](/_src/assets/00-PrimerosPasos/instalar_window.png)

Una vez descargado, se abre el archivo .exe y van a visualizar la siguiente ventana

![installGit](/_src/assets/00-PrimerosPasos/1.png)

Clickeamos “Next” hasta que llegamos a esta parte:

![installGit](/_src/assets/00-PrimerosPasos/2.png)

En este momento de la instalación, si quieren, pueden elegir el editor de texto que van a usar. (Importante, ténganlo instalado antes de instalar Git)

Seguimos clickeando “Next” y luego “Install”

![installGit](/_src/assets/00-PrimerosPasos/3.png)

Por último, ¡finalizar! Si seleccionan la opción "Launch Git Bash", una vez que finalizan la instalación se va a abrir la consola

![installGit](/_src/assets/00-PrimerosPasos/4.png)

Otra forma de abrir la consola es haciendo click derecho sobre el escritorio y elegir la opción "Git Bash Here"

![installGit](/_src/assets/00-PrimerosPasos/consola.png)

Una vez instalado Git van a poder visualizar la consola: ingresamos el comando `git --version` para chequear que está instalado. Si ven la consola así, ya están listos para comenzar a trabajar!

![installGit](/_src/assets/00-PrimerosPasos/5.png)

## GitHub

### ¿Qué es GitHub?

Es una red para almacenar tus repositorios, sería un repositorio de repositorios. Es uno de los tantos disponibles en internet, y el más popular. GitHub **NO** es lo mismo que Git, aunque funcionen muy bien juntos. Github es un lugar donde podés compartir tu código o encontrar otros proyectos. También actúa como portfolio para cualquier código en el que hayas trabajado.

### Comenzando

1. Para comenzar nos creamos una cuenta --- > <https://github.com> 🚀

![GitHub-Register](/_src/assets/00-PrimerosPasos/github_register.png)

2. Una vez registrados, ingresamos con usuario y contraseña:

![GitHub-Login](/_src/assets/00-PrimerosPasos/github_login.png)

3. Listo! Ahora vemos una página de inicio como la siguiente:

![GitHub-Home](/_src/assets/00-PrimerosPasos/github_home.png)

A la izquierda tenemos un acceso rápido a **mis repositorios**.

En el centro vemos la actividad de los usuarios a quienes seguimos.

En la parte superior derecha, vemos nuestra imagen de perfil. Desde ahí podemos desplegar opciones para gestionar nuestro perfil, repositorios y configuración. Si accedemos a nuestro perfil encontramos algo parecido a esto:

![GitHub-profile](/_src/assets/00-PrimerosPasos/github_profile.png)

Podemos poner una foto de perfil, editar el nombre, agregar la ubicación, link y organizaciones a las que pertenecemos. En el centro podemos fijar los repositorios que queremos mostrar para que estén visibles en nuestro perfil.

Más abajo se muestra un diagrama de todas las contribuciones que vamos haciendo a los repositorios.

Si accedemos a la pestaña de arriba que dice `repositorios` veremos una lista de todos ellos. Cuando elegimos un repositorio para ver, nos lleva a una página como esta:

![GitHub-repo](/_src/assets/00-PrimerosPasos/github_repo.png)

Así se ve un repositorio. Arriba a la izquierda tenemos el `nombre de usuario/nombre del repo`.

En el centro podemos ver todos los archivos que tiene dentro el repo. El botón verde que dice `Code` es importante, si clickeamos ahí vamos a poder obtener la url del repo, para así poder **_clonarlo_** (esto lo veremos más adelante).

Arriba a la derecha encontramos tres botones. `Watch` nos permite seguir un repositorio, mientras que con `Star` podemos marcar como favorito un repo que nos guste. Por último tenemos `Fork`, este es **muy** importante, lo vamos a necesitar cuando hagamos el **_Challenge!_**

Ya tenemos todo para empezar... Éxitos!!! 🍀

## Principales Objetivos de Aprendizaje para esta Clase

- Conocer de qué se trata programar
- Conocer para qué sirve un lenguaje de programación 


## Python

### ¿Qué es Python?

Es un lenguaje de programación sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites

### Instalación 

Si estás usando Windows:

Python 3.7 (o superior)
1. Para obtener el instalador dirígete a [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Descarga el instalador y ejecútalo en tu computadora.
3. Habilita la casilla de verificación en Install launcher for all users y Add Python 3.8 to PATH. A continuación presiona en Install Now. Windows te solicitará permisos para instalar Python en tu computadora.
4. Al finalizar la instalación se abrirá una ventana, en ella deberás presionar en la opción Disable path length limit. Windows te solicitará permisos para realizar este cambio.

Si estás usando Mac:

Mac OS X suele tener python instalado por defecto. Para verificarlo abrí la terminal, en el buscador de tu Mac, y escribí Python. Comprobar que está correctamente instalado: 

```bash
Python
Python 2.7.13 (default, Mar 25 2021, 18:52:10) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Si no te figura o queres descargar la última versión dirígete a: [https://es.wikibooks.org/wiki/Python/Instalaci%C3%B3n_de_Python/Python_en_Mac_OS_X](https://es.wikibooks.org/wiki/Python/Instalaci%C3%B3n_de_Python/Python_en_Mac_OS_X)

Si estás usando Linux:

En una distribución estándar Linux dispone por defecto el intérprete Python instalado, para comprobar la correcta instalación solamente debería ejecutar el comando en la consola:

```bash
python
Python 2.7.13 (default, Sep 26 2018, 18:42:22)
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Si le muestra los mensajes anteriores está correctamente instalado el intérprete Python en su Linux.

Si al ejecutar el comando anterior muestra el mensaje:

```bash
python
bash: python: no se encontró la orden
```

Esto es debido a que no tiene instalado el intérprete, así que debe ejecutar el siguiente comando:
```bash
sudo apt-get install -y python-dev
```

De nuevo vuelva a ejecutar en su consola de comando el comando python. Ya están listos para comenzar a trabajar

# Temario del Curso

1) Introducción a la programación
2) Variables y Tipos de Datos
3) Flujos de Control
4) Estructuras de Datos
5) Iteradores e Iterables
6) Funciones
7) Clases y POO
8) Manejo de Errores
9) Vinculación con datos externos

## Repositorio del curso

https://github.com/soyHenry/Python-Prep

# Introducción a la Programación

## ¿Qué es la Programación?

Comencemos con un ejemplo, en la imagen se representa un pequeño robot abeja en una esquina del cuadrilátero, y en la otra esquina una flor. El objetivo del robot abeja es llegar hasta la flor, esquivando los arbustos que hay de por medio. Para esto, hay que decirle cómo se debe mover, pero solo puede saltar de a un casillero por vez. La forma en que se le puede "decir" es a través de instrucciones y esttas son: "arriba", "abajo", "izquierda" y "derecha". Por supuesto, teniendo en cuenta que debe moverse dentro del cuadrilátero.

Ahora bien, surgen algunas preguntas:

* ¿Cuántas instrucciones son necesarias?

* Al ser más de una instrucción ¿Es importante el orden en que se ejecutan?

* ¿Hay más de una forma, en que el robot abeja pueda llegar a la flor?

* ¿Hay un camino óptimo?

* ¿Cómo puedo medir si un camino es el óptimo con respecto a otros caminos?

![unaImagenConBoxShadow](../_src/assets/01_imagen01.jpg)

Cualquiera de las siguiente, podrían ser una solución:
* Derecha, Derecha, Arriba, Arriba, Derecha, Derecha, Arriba, Arriba, Arriba, Derecha, Derecha, Arriba
* Derecha, Derecha, Derecha, Derecha, Derecha, Derecha, Arriba, Arriba, Arriba, Izquierda, Izquierda, Arriba, Arriba, Derecha, Arriba, Derecha
* Arriba, Derecha, Derecha, Arriba, Arriba, Arriba, Arriba, Arriba, Derecha, Derecha, Derecha, Derecha, Arriba

Lo importante, en principio, es que notemos que al resolver el problema planteado, lo que estamos haciendo, utilizando un pensamiento lógico, es precisamente, **programación**

Entonces, **programar, es armar una secuencia lógica de pasos a seguir, en pos de cumplir un objetivo.** En el ejemplo visto, tuvimos un contexto que nos marcaba las posibilidades y restricciones del problema, por ejemplo moverse dentro del cuadrilátero ó no chocar con los arbustos. Y también un conjunto de instrucciones disponibles, que definian el lenguaje que teníamos que usar, para que el robot comprenda las instrucciones. Lo que usamos fue un lenguaje formal, muy básico y que fue suficiente para resolver el problema. Éstos lenguajes, se denominan lenguajes de programación, nos permiten plasmar esas instrucciones necesarias para darle una solución al problema que queremos resolver, generando así un programa (o software).

Los primeros lenguajes de programación se escribían en instrucciones que podían interpretar las computadoras muy fácilmente, pero que resultaban menos amigables a las personas, tales como el lenguaje ensamblador (o Assembler) o Fortran, desarrollado en 1955. Con el tiempo, esto fue cambiando, se fueron desarrollando lenguajes de programación de más alto nivel y con diferentes aplicaciones, que por lo general eran comerciales o científicas, pero también con fines educativos, es decir, lenguajes desarrollados para aprender a programar, y consecuentemente, más sencillos. 

Éste último, es el caso de **Python**, que nace a finales de la década del 80 y fue pensado para principiantes por su facilidad de aprendizaje y uso. Su código era compacto pero legible. Con el correr de los años fue incluyendo mejoras hasta llegar también a ser de licencia libre. Hoy por hoy, es usado desde simples "scripts", hasta grandes servidores web que proveen servicio ininterrumpido las 24hs. Es utilizado para la programación de interfaces gráficas y bases de datos. Además tiene una amplia aceptación por científicos que hacen aplicaciones para las supercomputadoras más rápidas del mundo y por los niños que recién están comenzando a programar.
La generalización del Big Data en los últimos años, seguida de la explosión de la Inteligencia Artificial, Machine Learning y el surgimiento de la Ciencia de Datos como un nuevo área de trabajo con especialistas propios, ha revolucionado el panorama ya que muchas de las nuevas herramientas que han surgido han sido desarrolladas en Python o nos ofrecen Python como la forma predilecta de interactuar con ellas.
Podemos hablar de tecnología para Big Data como PySpark, de herramientas para Data Science como Pandas, NumPy, Matplotlib o Jupyter. De herramientas del procesamiento del lenguaje natural como NLTK, y por último el área de Deep Learning como Tensorflow, MXNet o Scikit-Learn.

## Sintaxis de un lenguaje de programación

Para el ejemplo se utilizó un lenguaje con el que era posible determinar los pasos a seguir por el robot abeja hasta llegar a la flor, y nos fue suficiente para poder entender cómo resolver el problema. El hecho es que, los lenguajes de programación que utilizamos, deben ser más específicos todavía, necesitamos tener un nivel de detalle mayor en nuestras instrucciones, por ejemplo, en lugar de la instrucción "Arriba", podría ser, especificar la cantidad de celdas que hay que moverse, e incluso qué implica "moverse", que seguramente será cambiar el estado de la propia abeja. 
Por otro lado también habrá un marco de referencia, es decir, el tablero donde se mueve la abeja y está la flor, en sí mismo, es algo que debemos conocer, saber donde hay ubicado un arbusto y donde no, saber cuales son los límites, y que pasa si con las instrucciones que le damos a la abeja, hacemos que rebase esos límites.
Para solventar esa complejidad, necesitamos un **set de instrucciones** un poco más complejo para poder interactuar con el computador y una forma de representar los datos de la realidad, es decir, dimensiones del tablero donde se mueve la abeja, posición de la abeja, posición de la flor, ubicaciones de los arbustos. Esto se hace mediante lo que se conoce como **estructuras** de datos, las cuales permiten representar la realidad. De hecho, todos **los datos son una representación de la realidad**.
La sintaxis de un programa, consiste en un conjunto de palabras reservadas a instrucciones, con una estructura específica, tal y como funciona un lenguaje como el que usamos los humanos para comunicarnos, como el español o el inglés. Los lenguajes de programación también tienen su sintaxis, que está compuesta por diferentes elementos, como ser variables para representar el dato de la realidad, sentencias para representar las instrucciones o estructuras de control que conforman el cuerpo del programa.

## El Zen de Python 

Para conocer mejor el lenguaje que estaremos aprendiendo les compartimos una colección de los 19 principios que influyen en el diseño del lenguaje Python. De alguna manera, muestran la filosofía del mismo:

1) Bello es mejor que feo.
2) Explícito es mejor que implícito.
3) Simple es mejor que complejo.
4) Complejo es mejor que complicado.
5) Plano es mejor que anidado.
6) Espaciado es mejor que denso.
7) La legibilidad es importante.
8) Los casos especiales no son lo suficientemente especiales como para romper las reglas.
9) Sin embargo la practicidad gana a la pureza.
10) Los errores nunca deben pasar silenciosamente.
11) A menos que se silencien explícitamente.
12) Frente a la ambigüedad, evitar la tentación de adivinar.
13) Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
14) A pesar de que esa manera no sea obvia a menos que seas Holandés (el creador lo era)
15) Ahora es mejor que nunca.
16) A pesar de que nunca es muchas veces mejor que ahora mismo.
17) Si la implementación es difícil de explicar, es una mala idea.
18) Si la implementación es fácil de explicar, puede que sea una buena idea.
19) Los namespaces son una gran idea, ¡tengamos más de esos!

## Recursos adicionales

* [Introducción al Pensamiento Computacional] (https://github.com/karlbehrensg/introduccion-pensamiento-computacional)
* [Entrenamiento Básico] (https://entrenamiento-python-basico.readthedocs.io/es/latest)
* [El Libro de Python] (https://ellibrodepython.com/)
* [Python para todos] (https://www.py4e.com)
* [Curso Python Videos] (https://youtu.be/G2FCfQj-9ig)
* [Visualizar tu código] (https://memlayout.com/)
* [Visualizar tu código] (https://pythontutor.com/visualize.html#mode=edit)

## Homework

Instalar Visual Studio Code, GitHub y Python para poder comenzar!

Si tienes dudas sobre este tema, puedes consultarlas en el canal #python de Slack

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
