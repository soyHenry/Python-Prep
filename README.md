![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# Prep Course

## Grabación de la Introducción

<div class="iframeContainer">
  <iframe src="https://player.vimeo.com/video/675579075" allow="autoplay; fullscreen" allowfullscreen></iframe>
</div>

## PASOS PARA RESOLVER EL HERNY CHALLENGE:

### 1. FORK

Primero debes forkear el repo que te indicaremos, haciendo click en el botón `fork` de arriba a la derecha.

Una vez que tengas una copia de este repo en tu cuenta de `github`, cloná el repo dentro de una nueva carpeta (asegurate de no utilizar la misma que el prep curse). Una vez clonado entrá a esa carpeta y ejecutá los siguientes comandos:

    python tests.py

>Si ves los tests fallando, estás listo para comenzar, si no lee bien el output para identificar el error.

### 2. RESOLVER EL HERNY CHALLENGE

Tu tarea es completar el código en `checkpoint.py` de tal forma que pasen la mayoría de los tests, incluido el extra credit.

### 3. ENTREGAR TU CHECKPOINT

Correr por ultima vez los tests y verificar cuantos pasan. Ten en cuenta que si te aparece "1 failed;1 total" es porque tienes un error de sintaxis: seguramente falta o sobra un corchete, paréntesis, dos puntos, etc.
Saca un print de pantalla de tus tests.
Luego, debes subir un commit a tu repo. Para hacerlo, debes ejecutar el siguiente comando:

    git add .
    git commit -m 'checkpoint commit'
    git push origin main

Una vez finalizado, chequea:
1. Que veas los cambios reflejados en el repo de tu cuenta de github (entrando a tu repo desde el browser.)
2.  Que no haya un require - solo debe haber codigo dentro de las funciones de cada ejercicio 