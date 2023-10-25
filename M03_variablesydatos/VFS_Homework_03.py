# Ejercicio 1
miVarInt = 6 #int
print("Ejercicio 1")
print(miVarInt)

# Ejercicio 2
print("Ejercicio 2")
print(type(8.5))

# Ejercicio 3
print("Ejercicio 3")
print(type(miVarInt))

# Ejercicio 4
miNombre = "Vero" #str

# Ejercicio 5
miComplejo = 3+5j #complejo

# Ejercicio 6
print("Ejercicio 6")
print(type(miComplejo))

# Ejercicio 7: Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math
miNroPiRedondeado = round(math.pi,4)

# Ejercicio 8
miTrueStr = "True" #str
miTrueBool = True
#no es lo mismo, son distintos tipos de datos

# Ejercicio 9
print("Ejercicio 9")
print(type(miTrueStr))
print(type(miTrueBool))

# Ejercicio 10 - Asignar a una variable, la suma de un número entero y otro decimal
miVar10 = 7 + 2,4

# Ejercicio 11 - Realizar una operación de suma de números complejos
miVar11 = (5+3j) + (5-3j)

# Ejercicio 12 - Realizar una operación de suma de un número real y otro complejo
miVar12 = 4.8 + 2-1j

# Ejercicio 13 - Realizar una operación de multiplicación
miVar13 = 4*3

# Ejercicio 14 - Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

# Ejercicio 15 - Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print("Ejercicio 15")
miCociente = 27/4
print(miCociente)

# Ejercicio 16 - De la división anterior solamente mostrar la parte entera
print("Ejercicio 16")
miDivisionEntera = 27//4
print(miDivisionEntera)

# Ejercicio 17 - De la división de 27 entre 4 mostrar solamente el resto
print("Ejercicio 17")
miResto = 27%4
print(miResto)

# Ejercicio 18 - Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print("Ejercicio 18")
miNuevo27 = 4 * miDivisionEntera + miResto

# Ejercicio 19 - Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("Ejercicio 19")
miAlfanumerica = "H0l4" + "_Mund0"

# Ejercicio 20 - Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
"2" == 2

# Ejercicio 21 - Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
int("2") == 2
"2" == str(2)

# Ejercicio 22 - ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3.8') #Arroja error porque el separador decimal es el punto, no la coma.

# Ejercicio 23 - Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
miVariable23 = 3
miVariable23 -= 2

# Ejercicio 24 - Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1<<2 # Desplazamiento a la izquierda dos posiciones 1 se convierte en 100 (porque rellena con ceros el desplazamiento). El 100 en binario es 4.

# Ejercicio 25 y 26 - Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
2 + '2'

miVariable25Suma = 2 + int('2') # Así, si funciona como suma de enteros.
miVariable25Concantena = str(2) + '2' # Así, si funciona como suma de enteros.
print(miVariable25Suma)
print(miVariable25Concantena)

# Ejercicio 26 - Realizar una operación válida entre valores de tipo entero y string
# Ver resolución del ejercicio 25. Ya está hecho.