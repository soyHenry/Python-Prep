![HenryLogo](https://henry-11ty-resources.s3.sa-east-1.amazonaws.com/Assets/logo-henry-white-lg.png)

<!-- el logo de Henry se oculta en el build -->

# Ejemplo de H1

#### Ejemplo de anexo del H1

Este readme corresponde al contenido de una clase o lección.

## Qué cambia en este layout?

Para el contenido de las clases se utiliza el layout `lesson` por default (no hace falta setearlo).

Este layout incluye:

### Tabla de contenidos

Se genera una TOC a la izquierda de la pantalla (solo en web) con links de navegación a los H2 y H3 encontrados en el contenido.

### Tiempo de lectura

Se utiliza la librería personalizada `henry-reading-time` para establecer un tiempo de lectura aproximado.

### Botón de Homework

En caso de que la clase tenga homework (existencia de la variable `homeworkUrl`) se genera un botón junto al tiempo de lectura, con link a la homework.

### Botón de Feedback

En caso de que la clase tenga un `feedbackID` (correspondiente a *AirTable*) renderiza un botón que lleva a dicho form.

## Imágenes

Cualquier imagen que queramos incluir debe estar dentro de la carpeta `assets` (es posible incluir subcarpetas) y por default va a tener **_BoxShadow_**.

![unaImagenConBoxShadow](/_src/assets/1.png)

Si no queremos que tenga _BoxShadow_, sólo necesitamos ponerle al Alt text el valor `no-box`.

![no-box](/_src/assets/1.png)

Es ùtil especialmente para imagenes con fondo transparente, logos, etc.

![no-box](/_src/assets/2.png)

Morbi ultricies euismod tortor, eu finibus massa. In vehicula diam iaculis, pulvinar leo sed, aliquet leo. Suspendisse at hendrerit nisi, vitae finibus enim. Donec id pretium urna. Ut ullamcorper tortor sit amet dolor blandit, quis venenatis urna tempus. Curabitur efficitur blandit blandit. Aliquam placerat justo leo, ut porttitor turpis gravida sed. Suspendisse varius varius urna quis faucibus. Proin lacus erat, mollis nec finibus eget, lobortis vel metus. In elit quam, euismod vitae magna condimentum, cursus condimentum tellus. Quisque vel dictum ante, vel laoreet dolor. Suspendisse eleifend ut nibh nec mollis. Pellentesque dignissim, tortor at pellentesque porttitor, nisi lorem viverra turpis, ut viverra enim ipsum bibendum arcu. Donec lacinia cursus consequat. Fusce quis ultrices magna.

## Contenido oculto en la web

Si queremos mostrar contenido al visualizar el markdown desde nuestro editor de texto, o desde GitHub, pero *NO* cuando generamos el sitio web, debemos utilizar un elemento HTML con la clase `hide`.

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
