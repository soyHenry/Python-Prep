#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 12
print(a)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
type(8.5)




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(a)





# 4) Crear una variable que contenga tu nombre

# In[2]:
mi_nombre='Nayivis'




# 5) Crear una variable que contenga un número complejo

# In[3]:
num_complejo = 5 + 2i





# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
type(num_complejo)





# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
var1='True'
var2=True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print('la variable 1 es de tipo : ,'type(var1),  'la variable 2 es de tipo: ' , type(var2))





# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

var = 5 + 1,23



# 11) Realizar una operación de suma de números complejos

# In[2]:
a = 2 + 3j
b = 4 + 3j
print ('la suma de los numeros complejos es ', a+b)





# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
a = 2 + 3,4
print (a)




# 13) Realizar una operación de multiplicación

# In[5]: 
print( 3 * 4)





# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]: 
print(2**8)




# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]: 
a= 27 / 4
print( a)





# 16) De la división anterior solamente mostrar la parte entera

# In[9]: 
print(27 // 4)





# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27 % 4)





# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print( 6 * 4 + 3)





# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
a = 'Santa '
b = 'Marta '
print ( a + b )





# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
'2' == 2
# son diferentes porque na es de tipo entero y la otra de tipo string




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
2== int('2')




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
#arroja error porque cadena tiene un formato no valido para formato float, se le debe quitar la coma y ponerle .




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
a = 3
a -= 1
print (a)





# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

"""La operación 1<<2 da como resultado 4 porque el operador << es un desplazamiento a la izquierda en lenguaje binario, lo que significa que toma el número binario de 1 y desplaza sus bits dos posiciones a la izquierda. El número binario de 1 es 01 (si imaginamos que es de 2 bits), y al desplazarlo dos posiciones a la izquierda, el resultado binario es 100, que en decimal es 4.
Paso 1: Representa el número 1 en binario. Para simplificar, pensemos en 1 como 01.
Paso 2: Aplica el desplazamiento a la izquierda <<2. Esto significa que mueves todos los bits del número dos posiciones hacia la izquierda. Las posiciones que quedan vacías a la derecha se rellenan con 0.01 se convierte en 100 (dos posiciones a la izquierda).
Paso 3: Convierte el resultado binario 100 a decimal.El valor posicional de cada bit es: \((1\times 2^{2})+(0\times 2^{1})+(0\times 2^{0})=4+0+0=4\)"""



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
# no está permitido porque las variables son de difrentes tipos
# si los las dos variables fueran del mismo tipo no arrojaría ese resultado




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
int(2) + int ('2')



