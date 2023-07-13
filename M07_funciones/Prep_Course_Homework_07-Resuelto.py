#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def verifica_primo(nro):
    es_primo = True
    for i in range(2, nro):
        if nro % i == 0:
            es_primo = False
            break
    return es_primo


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:


def extrae_primos_de_lista(lista):
    lista_primos = []
    for elemento in lista:
        if verifica_primo(int(elemento)):
            lista_primos.append(elemento)
    return lista_primos


# In[26]:


lis_completa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lis_primos = extrae_primos_de_lista(lis_completa)
lis_primos


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:


def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo


# In[36]:


lis = [1,1,5,6,8,10,22,5,6,4,11,9,5]
moda, repite = valor_modal(lis)
print('El valor modal es', moda, 'y se repite', repite, 'veces.')


# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:


def conversion_grados(valor, origen, destino):
    if (origen == 'celsius'):
        if (destino == 'celsius'):
            valor_destino = valor
        elif (destino == 'farenheit'):
            valor_destino = (valor * 9 / 5) + 32
        elif (destino == 'kelvin'):
            valor_destino = valor + 273.15
        else:
            print('Parámetro de Destino incorrecto')
    elif (origen == 'farenheit'):
        if (destino == 'celsius'):
            valor_destino = (valor - 32) * 5 / 9
        elif (destino == 'farenheit'):
            valor_destino = valor
        elif (destino == 'kelvin'):
            valor_destino = ((valor - 32) * 5 / 9) + 273.15
        else:
            print('Parámetro de Destino incorrecto')
    elif (origen == 'kelvin'):
        if (destino == 'celsius'):
            valor_destino = valor - 273.15
        elif (destino == 'farenheit'):
            valor_destino = ((valor - 273.15) * 9 / 5) + 32
        elif (destino == 'kelvin'):
            valor_destino = valor
        else:
            print('Parámetro de Destino incorrecto')
    else:
        print('Parámetro de Origen incorrecto')
    return valor_destino


# In[59]:


print('1 grado Celsius a Celsius:', conversion_grados(1, 'celsius', 'celsius'))
print('1 grado Celsius a Kelvin:', conversion_grados(1, 'celsius', 'kelvin'))
print('1 grado Celsius a Farenheit:', conversion_grados(1, 'celsius', 'farenheit'))
print('1 grado Kelvin a Celsius:', conversion_grados(1, 'kelvin', 'celsius'))
print('1 grado Kelvin a Kelvin:', conversion_grados(1, 'kelvin', 'kelvin'))
print('1 grado Kelvin a Farenheit:', conversion_grados(1, 'kelvin', 'farenheit'))
print('1 grado Farenheit a Celsius:', conversion_grados(1, 'farenheit', 'celsius'))
print('1 grado Farenheit a Kelvin:', conversion_grados(1, 'farenheit', 'kelvin'))
print('1 grado Farenheit a Farenheit:', conversion_grados(1, 'farenheit', 'farenheit'))


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:


metricas = ['celsius','kelvin','farenheit']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado', metricas[i], 'a', metricas[j],':', conversion_grados(1, metricas[i], metricas[j]))


# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:


def factorial(numero):
    if(type(numero) != int):
        return 'El numero debe ser un entero'
    if(numero < 0):
        return 'El numero debe ser pisitivo'
    if (numero > 1):
        numero = numero * factorial(numero - 1)
    return numero
print(factorial(3))
print(factorial(-2))
print(factorial(1.23))
print(factorial('6'))

