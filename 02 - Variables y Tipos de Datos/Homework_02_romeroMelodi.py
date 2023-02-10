## Variables
## 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
mivariable = 8
print(mivariable)

## 2) Imprimir el tipo de dato de la constante 8.5
miconstante = 8.5
print(type(miconstante))

## 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(mivariable))

## 4) Crear una variable que contenga tu nombre
minombre = 'Melodi'

## 5) Crear una variable que contenga un número complejo
micomplejo = 5 + 2j

## 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(micomplejo))

## 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
mipi = 3.1416

## 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable1 = 'True'
variable2 = True
## No son lo mismo, uno es String y la otra Boolean

## 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(variable1)) 
print(type(variable2))

## 10) Asignar a una variable, la suma de un número entero y otro decimal
suma = 4 + 3.5

## 11) Realizar una operación de suma de números complejos
a = 3 + 5j
b = 4 + 6j
sumac =  a + b

## 12) Realizar una operación de suma de un número real y otro complejo
mireal = 4.67
micomplejo = 4 + 3j
misuma = mireal + micomplejo

## 13) Realizar una operación de multiplicación
8*8

## 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

## 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27/4
print(cociente)

## 16) De la división anterior solamente mostrar la parte entera
parteentera = 27//4
print(parteentera)

## 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27%4
print(resto)

## 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4*parteentera + resto)

## 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print(minombre + variable1)

## 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
## No son lo mismo, lo mismo que pasa en el punto 8 son distintos tipos de datos. Uno es String y el otro entero.

## 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
int("2") == 2

## 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3.8') # Arroja error porque se debe reemplazas la coma por punto para que tome el string como float.

## 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
mivariable3 = 3
mivariable3 -= 3

print(mivariable3)

## 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
resultado =  1 << 2
print(resultado)
# Da ese reusltado al mover 2 bits del 1 expresado en el sistema binario. El sistema binario es un sistema de numeracion de 0 ceros y 1 nos que represente los numeros. Es el lenguaje de las computadoras.-

## 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# No esta permitido porque son  distintos datos. Si daria el resultado 4, si son del mismo tipo.
print(int(2) + int('2'))

print(float(2) + float('2'))

print(str(2) + str('2'))
## 26) Realizar una operación válida entre valores de tipo entero y string

print('mi nombre es'+ minombre + 'y mi nro favorito es: '+ str(mipi))