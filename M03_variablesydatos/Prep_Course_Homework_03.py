#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
x = 2
print(x) # funcion para recuperar el dato de una variable

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
type(8.5) # type para imprimir el tipo de dato




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(x)




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = 'Gabriel' # asignamos un string o cadena de texto



# 5) Crear una variable que contenga un número complejo

# In[3]:

suma = 5 + 9j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(suma)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

cadena= 'True'
booleano = True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print('la v')

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

a = 3 + 3.4 # un numero real con un numero flotante (decimal)
print(a)


# 11) Realizar una operación de suma de números complejos

# In[2]:


b = 2j + 1j # operacion de numeros complejos


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:


i = 3 + 4j # es un numero real sumando un numero complejo


# 13) Realizar una operación de multiplicación

# In[5]:


o = 2 * 4
print(o)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

a = 2** 8
print(a)
bool(a)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:


u = 27 / 4
print(u)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:


27 // 4 # obtenemos la parte entera 6



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


27 % 4 # obtenemos el resto 3


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

4 * 6 + 3



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

a = "hola"
b = " gabriel"
a + b



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


"2" == 2 #evaluando una condicion 


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:


2 == int("2")


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float("3.8") # por que no se puede convertir el string en flotante por que tiene un , y no un .
print(a)


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:


a = 3
a -= 1
a


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1 << 2
# es un sistema de numeracion donde los numeros son representados unicamente por dos cifras (0) y (1)


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:



float(2) + float("2.2")
int(2) + int("2")

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

a = 'repetir '
b = 4
print(a * b + ' hasta que la variable ' + str(b) + ' diga')


# %%
