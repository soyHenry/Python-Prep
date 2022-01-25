#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:


lista = []
n = -15
while (n < 0):
    lista.append(n)
    n += 1
print(lista)


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:


n = 0
while (n < len(lista)):
    if (lista[n] % 2 == 0):
        print(lista[n])
    n += 1


# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:


for elemento in lista:
    if (elemento % 2 == 0):
        print(elemento)


# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:


for elemento in lista[:3]:
    print(elemento)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:


for i, e in enumerate(lista):
    print(i, e)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:


lista = [1,2,5,7,8,10,13,14,15,17,20]


# In[11]:


n = 1
while(n <= 20):
    if (not(n in lista)):
        lista.insert((n-1), n)
    n += 1
print(lista)


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:


fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n += 1
print(fibo)


# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:


sum(fibo)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:


primeros = 15
n = primeros - 5
while(n < primeros):
    print(fibo[n]/fibo[n-1])
    n += 1


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:


cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, c in enumerate(cadena):
    if c == 'n':
        print(i)


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:


dicc = {  'Ciudad': ['Buenos Aires','Caracas','Bogotá','Lisboa','Roma'], 
'País': ['Argentina','Venezuela','Colombia','Portugal','Italia'], 
'Continente' : ['América','América','América','Europa','Europa']}
for i in dicc:
    print(i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:


cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print(type(cadena))
cadena = list(cadena)
print(type(cadena))


# In[45]:


recorre = iter(cadena)
largo = len(cadena)
for i in range(0, largo):
    print(next(recorre))


# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:


lis1 = ['run','fly','sleep']
lis2 = ['correr','volar','dormir']
lisz = zip(lis1, lis2)
print(type(lisz))
print(list(lisz))


# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:


lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis2 = [i for i in lis if i % 7 == 0]
print(lis2)


# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:


lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]


# In[51]:


type(lis)


# In[57]:


cantidad = 0
for elemento in lis:
    if (type(elemento) == list):
        cantidad += len(elemento)
    else:
        cantidad += 1
print('La cantidad total de elementos es', cantidad)


# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:


for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
print(lis)

