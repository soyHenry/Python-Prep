![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

<!-- el logo de Henry se oculta en el build -->

# Título de la clase

#### Anexo del título

Este readme corresponde al contenido de una clase o lección.

## Data de cada clase

La ***data*** relacionada a esta clase se incluye en un archivo con su mismo nombre, pero con la extensión ***.json***:

```json
{
  "lessonTitle": "Primera clase", // Se muestra en la ventana del navegador y en la navbar.
  "feedbackID": "01-lesson1", // El pre-fill correspondiente a esta clase para el form de airtable (opcional).
  "permalink": "/Tema_Uno/", // La ruta generada en el sitio estático para esta clase.
  "quizzID" : "6057d0a5656c8d23c2e60e3e", // El indentificador correspondiente al quizz de la  clase actual (opcional).
  "homeworkUrl": "https://github.com/soyHenry/Prep-Course/tree/main/05-JS-IV/homework", // La ruta a la carpeta del homework correspondiente a esta clase, en GitHub (opcional).
  "eleventyNavigation": {
    "key": "Tema 1", // El nombre corto con que queremos que aparezca en la nav esta clase.
    "order": 1 // El nro de posición en el que queremos que aparezca esta clase en la nav.
  }
}
```

Para el contenido de las clases utilizamos el layout `lesson`. No hace falta setearlo, es el layout por default.

## Qué cambia en este layout?

Este layout incluye:

### Tabla de contenidos

Se genera una TOC a la izquierda de la pantalla (solo en web) con links de navegación a los H2 y H3 encontrados en el contenido.

### Tiempo de lectura

Se utiliza la librería personalizada `henry-reading-time` para establecer un tiempo de lectura aproximado.

### Botón de Quizz

En caso de que la clase tenga ***quizz*** (existencia de la variable `quizzID`) se genera un botón a continuación del tiempo de lectura, con el link correspondiente.

### Botón de Homework

En caso de que la clase tenga ***homework*** (existencia de la variable `homeworkUrl`) se genera un botón a continuación del de quizz, con el link correspondiente.

### Botón de Feedback

En caso de que la clase tenga un `feedbackID` (correspondiente a *AirTable*) renderiza un botón que lleva a dicho form.

## Imágenes

Cualquier imagen que queramos incluir debe estar dentro de la carpeta `assets` (es posible incluir subcarpetas) y por default va a tener **_BoxShadow_**.

![unaImagenConBoxShadow](/_src/assets/1.png)

Si no queremos que tenga _BoxShadow_, sólo necesitamos ponerle al Alt text el valor `no-box`.

![no-box](/_src/assets/1.png)

Es ùtil especialmente para imagenes con fondo transparente, logos, etc.

![no-box](/_src/assets/2.png)

## Contenido oculto en la web

Si queremos mostrar contenido al visualizar el markdown desde nuestro editor de texto, o desde GitHub, pero **NO** cuando generamos el sitio web, debemos utilizar un elemento HTML con la clase `hide`.

Por ejemplo, debemos incluir un link al feedback para quienes esten viendo el contenido desde el editor, pero no queremos que aparezca en la web porque ya tenemos un botón para ello.

Acá tenemos un div con la clase hide, que en la web no se muestra:

<table class="hide" width="100%" style='table-layout:fixed;'>
  <tr>
    <td>
      <a href="https://airtable.com/shrSzEYT4idEFGB8d?prefill_clase=05-JS-IV">
        <img src="https://static.thenounproject.com/png/204643-200.png" width="100"/>
        <br>
        Hacé click acá para dejar tu feedback sobre esta clase.
      </a>
    </td>
  </tr>
</table>

## Homework

Al final de cada lección generalmente ponemos un enlace a la homework. Al haber un H2 con el texto "Homework" el mismo tendrá un estilo propio.
