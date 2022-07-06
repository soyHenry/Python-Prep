![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

## Grabación de la Clase 9

<div class="iframeContainer">
  <iframe src="https://player.vimeo.com/video/687171116" allow="autoplay; fullscreen" allowfullscreen></iframe>
</div>

## Vinculación con Datos Externos

Es muy importante tener en cuenta que va a ser necesario interactuar con el usuario y trabajar con datos que están alojados en medios externos, puede tratarse de un sistema de archivos ó de una tabla en una base datos, entre otras fuentes.
Es posible realizar operaciones de interacción con el usuario y manipular archivos usando métodos para leer y escribir desde y hacia el sistema de archivos.

### Entrada / Salida

Se utilizan funciones ya integradas en el intérprete del lenguaje. Para solicitar información al usuario se utiliza **input**:

``` python
>>> color = input('¿Cuál es tu color favorito?: ')
¿Cuál es tu color favorito?: Azul
>>> print(color)
Azul
>>> nro = input('¿Cuál es el doble de 3?: ')
¿Cuál es el doble de 3?: 6
>>> if (int(nro) == 6):
>>>   print('Respuesta Correcta')
>>> else:
>>>   print('Respuesta Incorrecta')
```
<hr width="75%">
  <p align="center">
  Tips: Notar que input() devuelve un tipo de dato string, motivo por el cual al preguntar la igualdad con el 6, lo convertimos a entero
  </p>
<hr width="75%">

La **salida estándar** es la forma general de mostrar información por pantalla es mediante una consola de comando, generalmente podemos mostrar texto y variables separándolos con comas, para este se usa la sentencia **print**

``` python
>>> print("el resultado de raíz cuadrada de dos es:", (2**0.5))
el resultado de raíz cuadrada de dos es: 1.41421356237
```

Una forma esencial de escribir un programa es a través de archivos llamados scripts, que no son más que lotes de instrucciones. Luego se envía este archivo al intérprete como parámetro desde la terminal de comando (si es un lenguaje interpretado como Python) y éste ejecutará todas las instrucciones en bloque.
Una característica interesante de los scripts es que pueden recibir datos desde la propia terminal de comando en el momento de la ejecución, algo muy útil para agregar dinamismo a los scripts a través de parámetros o argumentos personalizables.
Para poder enviar información a un script y manejarla, tenemos que utilizar la librería de sistema **sys**. En ella encontraremos la lista **argv** que almacena los argumentos enviados al script.
Suponiendo que creamos un script llamado "ejemplo_parametros.py" que tenga el siguiente código:

``` python
import sys
# Comprobación de seguridad, ejecutar sólo si se reciben 2 
# argumentos realemente
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("ERROR: Introdujo uno (1) o más de dos (2) argumentos")
    print("SOLUCIÓN: Introduce los argumentos correctamente")
    print('Ejemplo: ejemplo_parametros.py "Texto" 5')
print("El argumento 0 es el nombre del archivo:", sys.argv[0])
```

Luego en la consola, realizar la ejecución del script, por ejemplo:<br>
python ejemplo_parametros.py 'Hola' 4

<hr width="75%">
  <p align="center">
  Tips: Notar que la lista de argumentos argv contiene en su elemento 0 el nombre del archivo.
  </p>
<hr width="75%">

### Manejo de Archivos

Un requisito muy común va a ser leer datos desde archivos de texto o también llamados secuenciales. Para esto Python incorpora un tipo integrado llamado **file**. Es importante notar que estos archivos siempre devuelven los datos como cadenas de caracteres, por lo tanto, de ser necesario, otros tipos deben ser convertidos.

* Crear un archivo a partir de datos presentes en una lista:

``` python
>>> import os
>>> lineas_archivo = ['Esto es un archivo de ejemplo','Segunda linea','Tercera linea']
>>> archivo = open('datos.txt', 'w')
>>> for linea in lineas_archivo:
>>>     archivo.write(linea+'\n')
>>> archivo.close()
```

Es importante cerrar el archivo, ya que si no lo hacemos, el sistema operativo interpreta que está en uso, tal como si estuviera abierto en cualquier editor de texto.

* Abrir un archivo, e iterar en él para leerlo:

``` python
>>> import os
>>> archivo = open('datos.txt', 'r')
>>> for linea in archivo:
>>>     print linea
>>> archivo.close()
Esto es un archivo de ejemplo
Segunda linea
Tercera linea
```

<hr width="75%">
  <p align="center">
  Tips: Notar que la función open tiene como primer parámetro el nombre del archivo y como segundo parámetro un carácter que indica el modo de apertura:<br>
  Con 'x' creará el archivo, sin embargo retorna error si ya existe<br>
  Con 'a' agregá contenido si el archivo existe, si no lo crea<br>
  Con 'w' crea el archivo directamente, si existe y tiene contenido lo pisa<br>
  </p>
<hr width="75%">


### Interactuar con el sistema de archivos

El módulo **os** de Python permite realizar operaciones dependiente del Sistema Operativo como crear una carpeta, listar contenidos de una carpeta, conocer acerca de un proceso, finalizar un proceso, etc.

* Crear una carpeta nueva
``` python
>>> import os
>>> os.makedirs("Mi_Carpeta")
```

* Listar el contenido de una carpeta
``` python
>>> import os
>>> os.listdir("./")
['Mi_Carpeta']
```

* Mostrar el actual directorio de trabajo
``` python
>>> import os
>>> os.getcwd()
'/home/usuario/python/'
```

* Mostrar el tamaño en bytes del archivo pasado como parámetro
``` python
>>> import os
>>> os.path.getsize("Mi_Archivo")
4096
```

* Verificar si es un archivo el parámetro pasado
``` python
>>> import os
>>> os.path.isfile("Mi_Archivo")
True
```

* Verificar si es una carpeta el parámetro pasado
``` python
>>> import os
>>> os.path.isdir("Mi_Carpeta")
True
```

* Cambiar directorio/carpeta

``` python
>>> import os
>>> os.chdir("Mi_Carpeta")
>>> os.getcwd()
'/home/usuario/python/Mi_Carpeta'
>>> os.listdir("./")
[]
>>> os.chdir("../")
>>> os.getcwd()
'/home/usuario/python'
```

* Renombrar un archivo
``` python
>>> import os
>>> os.rename("Mi_Archivo","Mi_Otro_Archivo")
>>> os.listdir("./")
['Mi_Otro_Archivo']
```

* Eliminar un archivo
``` python
>>> import os
>>> os.chdir("Mi_Carpeta")
>>> archivo = open(os.getcwd()+'/datos.txt', 'w')
>>> archivo.write("Hola Mundo!")
>>> archivo.close()
>>> os.getcwd()
'/home/usuario/python/Mi_Carpeta'
>>> os.listdir("./")
['datos.txt']
>>> os.remove(os.getcwd()+"/datos.txt")
>>> os.listdir("./")
[]
```

* Eliminar una carpeta
``` python
>>> os.rmdir("Mi_Carpeta")
>>> os.chdir("Mi_Carpeta")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 2] No such file or directory: 'Mi_Carpeta'
```

Lanza una excepción OSError cuando intenta acceder al directorio que previamente elimino y este no encuentra.

### Extra - Web Scrapping

Se utiliza esta técnica para extraer información desde sitios web, en primer lugar es necesario tener descargada una librería de Python, llamada Beautiful Soup que nos permite realizar esta acción:

``` python
>>> !pip install beautifulsoup4
>>> from bs4 import BeautifulSoup
>>> import urllib.request
```

Luego, vamos a extraer el HTML de un sitio web, por ejemplo de Wikipedia:

``` python
response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Python')
html = response.read()
```

Ahora, es necesario quitar todo lo que corresponda a código, y quedarse sólo con la parte del texto, que es lo que realmente interesa

``` python
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
```

En la variable 'text' ahora tenemos el texto del sitio web al que consultamos.



## Homework

Completa la tarea descrita en el archivo [README](https://github.com/soyHenry/Python-Prep/blob/main/09%20-%20Entrada-Salida%20y%20Manejo%20de%20Archivos/Prep_Course_Homework_09.md)

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
