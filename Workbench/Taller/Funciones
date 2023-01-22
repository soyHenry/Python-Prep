#*******************************************************************
#*                                                                 *
#*            B I E N V E N I D O  A  F U N C I O N E S            *
#*                                                                 *
#*******************************************************************
# Una función es una operación o procedimiento que retorna un valor o acción
# Se declaran con la palabra reservada 'def' y se cierra con ':', debe incluir 'return' y la logica
# del cálculo o lo que hace la función.
# Operaciones o métodos habituales como insert, append, sort...son funciones, porque hacen o retornan cosas.
# Para usar la función, le paso los parámetros definidos, ojo con los tipos y el control de las excepciones

# Ejemplo 1
def misuma (a,b): # Esta es una función, toma dos enteros a,b y los suma
    return a+b    # El calculo viene después de la palabra return

res= misuma (2,3) # Uso la función, le paso los parámetros 2,3 y, el resultado lo almaceno en la variable res
print ("Resultado de sumar 2 y 3, es ", res)       # Puedo ver su contenido con un print

# Ejemplo 2
# min y max son funciones integradas en Python que nos devuelven
# los valores mínimo y máximo de un iterable (como las listas o las tuplas)
def min_y_max(lista): # Declaro la función y le digo que le pasaré un argumento de tipo lista
    return min(lista), max(lista) # Usando la funciones min y max que pertenecen a objetos iterables
                                  # obtengo los valores y los devuelvo

# ahora vamos a usar estas funciones
valor = misuma(10, 15)
print("Usando la función 'misuma', el resultado de sumar 10 y 15 es ", valor)

minimo, maximo = min_y_max([30, 10, 50, 40, 20])
print("Para el vector 30,10,50,40 y 20, los ",f'min y max son {minimo} y {maximo}')

# Ejemplo 3 #Lo veremos más adelante
# En este ejemplo, creamos una función que realiza un test unitario 
#def test_OrdenarDiccionario_03(self):
#    dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
#    valor_test = ch.OrdenarDiccionario(dicc, 'clave3', False)
#    valor_esperado = {'clave1':['b','a','c'], 'clave2':['barco','auto','casa'], 'clave3':[3,2,1]}  