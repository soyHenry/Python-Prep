# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaDivisibles(numero, tope):
    '''
    Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24,30]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    #Tu código aca:
    lista_rango = list(range(numero,tope+1))
    lista_num_divisibles = []
    
    if numero > tope:
        print(lista_num_divisibles)
        return lista_num_divisibles
    if numero <= 0:
        print(str(numero) + ', que corresponde a ser el divisor, NO puede ser = 0.')
        return None

    for i in lista_rango:
        if (i % numero) == 0:
            lista_num_divisibles.append(i)
            lista_num_divisibles.sort(reverse=False)
    print(lista_num_divisibles)        
    return lista_num_divisibles

#ListaDivisibles(6,30)
#ListaDivisibles(10,5)
#ListaDivisibles(7,50)

#O.K. - Revisado y testeado!


def Exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
    Recibe dos argumentos:
        numero: El número base en la operación exponencial
        exponente: El número exponente en la operación exponencial
    Ej:
        Exponente(10,3) debe retornar 1000
    '''
    #Tu código aca:
    exponente = numero**exponente
    print(exponente)
    return exponente

#Exponente(10,3)

#O.K. - Revisado y testeado!


def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.                       Listo!
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    #Tu código aca:
    listaplana = list()

    if type(lista) != list:
        print('No es una lista.')
        return None
    
    for elemento in lista:
        if type(elemento) != list:
            listaplana.append(elemento)
        if type(elemento) == list:
            for elemento2 in list(elemento):
                if type(elemento2) != list:
                    listaplana.append(elemento2)
                if type(elemento2) == list:
                    listaplana.extend(ListaDeListas(elemento2))
   
   
   
    print(listaplana)
    return listaplana


#ListaDeListas([1,2,['a','b'],[10]])
#ListaDeListas(108)
#ListaDeListas([[1,2,[3]],[4]])
#ListaDeListas([[1,2,[3,[6,6,6,[7,[['iri'],8,9,[11]],],6,6]]],[4]])          #extra prueba


def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo. ok
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
        Factorial(0) debe retornar 1
    '''
    #Tu código aca:
    if (type(numero) != int) or (numero < 0):
        print('El numero no pertence a los enteros positivos.')
        return None

    import math

    factorial = math.factorial(numero)
    print(factorial)
    return factorial  

#Factorial(9)
#Factorial(4)
#Factorial(-2)
#Factorial(0)

# O.K. tested & ok


def ListaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como parámetro, siendo ambos inclusivos.
    
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, 
    debe retornar nulo. ok
    
    En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía. ok

    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    #Tu código aca:
    
        # 1. En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, 
        # debe retornar nulo.
    
    if(type(desde or hasta) != int) or ((desde or hasta) < 0):
        print('Valores no son enteros reales positivos.')
        return None

        # 2. En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
        # debe retornar una lista vacía.    
        # entiendo que hay un error en la consigna, si no deberíamos utilizar valores absolutos  ya que la cuenta seria regresiva en -1, -2, -3 etc
        # y supongo que lo que no quiere es que hagamos esto. obtener un desplazamiento negatico coodenada final(hasta) menos inicial(desde)..

    if desde > hasta:
        print('Parametros incorrectos.El valor "desde" debe ser menor que "hasta".')
        return []

    
        # 3. Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
        #    pasados como parámetro, siendo ambos inclusivos.

        #           3.1 Desde" y "hasta" pasados como parámetro, siendo ambos inclusivos.
    
    lista_a_analizar = range(desde,hasta+1)
    lista_ya_analizados = []
    es_primo = True
    lista_primos = []
    import math
    
    for elemento in lista_a_analizar:
        for i in range(2,elemento):
            if (elemento % i == 0):
                es_primo = False
                break
            else:
                es_primo = True
                lista_primos.append(elemento)
                break

    print(lista_primos)
    return lista_primos
    
#ListaPrimos(7,15) 
#ListaPrimos(100,99) 
#ListaPrimos(1,7) 
#ListaPrimos(4,150)  #prueba extra

# O.K. tested & Chequed!



  

def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    
    En caso de que el parámetro no sea de tipo lista debe retornar nulo. ok

    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,2),(4,1)]
    '''
    #Tu código aca:

    # 1. Esta función recibe como parámetro una lista ; En caso de que el parámetro no sea de tipo lista debe retornar nulo. ok
    if type(lista) != list:
        print('El parámetro ingresado no es una Lista.')
        return None

    # 2.  Devuelve una lista de tuplas donde cada 
    #     tupla contiene un valor de la lista original y las veces que se repite.
    #     Los valores de la lista original no deben estar repetidos.
    #     Debe respetarse el orden original en el que aparecen los elementos. 
    lista_ya_analizados = list()
    for elemento in lista:
        if (type(elemento) != list):
            
            if (elemento not in lista_ya_analizados):
                lista_ya_analizados.append(elemento)
            else:
                pass

        if type(elemento) == list:
            ListaRepetidos(elemento)
    print('Lista de elementos unicos encontrados:')
    print(lista_ya_analizados)

    lista_cant_de_repeticiones = []
    
    for elemento2 in lista_ya_analizados:
        cantidad_de_repes_del_elemento2 = lista.count(elemento2)
        lista_cant_de_repeticiones.append(cantidad_de_repes_del_elemento2)
    
    print(lista_cant_de_repeticiones)

    #conversion a tupla 
    respuesta = list(zip (lista_ya_analizados,lista_cant_de_repeticiones))
    print(respuesta)
    return respuesta


#ListaRepetidos([])
#ListaRepetidos(['hola', 'mundo', 'hola', 13, 14])
#ListaRepetidos([1,2,2,4])
#ListaRepetidos(ListaDeListas([1,[2,3,4,2,['l','k','j'],1,'q','w',],2,2,4,]))        #extra prueba

# O.K. Tested ok chequed



def ClaseVehiculo(tipo, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Vehiculo, 
    la cual debe tener los siguientes atributos:

        Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
        Color:      Un valor de tipo de dato string.
        Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
    
    y debe tener el siguiente método:
    
        Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
                    propiedad Velocidad y luego retornarla.
                    Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                    Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
    
    Recibe dos argumento:
        tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
        color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
    
    Ej:
        a = ClaseVehículo('auto','gris')
        a.Acelerar(10) -> debe devolver 10
        a.Acelerar(15) -> debe devolver 25
        a.Acelerar(-10) -> debe devolver 15
    '''
    #Tu código aca:
    lista_tipos_permitidos = ['auto','camioneta','moto']
    
    # Validaciones al crear la CLASE:
    
    if tipo not in lista_tipos_permitidos:
        print('Error al crear la clase, este tipo de vehiculo no se permite crear, solo estos se pueden: ("auto", "camioneta", "moto").')
        print('Error al crear vehiculo.')
        return None
    
    if type(color) != str:
        print('El dato "color" no es un str.')
        print('Error al crear vehiculo.')
        return None

    tipo = tipo
    color = color
    
    # Creando un vehiculo
    # Para ello debe existir primero la clase dentro de la funcion.
    # de manera que siempre exista dentro del paquete de la funcion si esta se exporta.
    class Vehicle:
        '''
        Clase Veiculos dentro de funcion crear vehiculo.
        '''
        def __init__(self,tipo,color,velocidad = float(0)):
        
            self.tipo = tipo
            self.color = color
            self.velocidad = float() 
            self.incremento_velocidad = float(0)

        def Acelerar(self,incremento_velocidad = float(0)):
            """
            Este método recibe un parámetro con el valor que debe incrementar a la
            propiedad Velocidad y luego retornarla.
            
            Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
            
            Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
            """
            velocidad_inicial = self.velocidad
            velocidad_final = velocidad_inicial + incremento_velocidad

            if velocidad_final > 100:
                velocidad_final  = 100
                self.velocidad = velocidad_final
                return self.velocidad
            elif velocidad_final < 0:
                velocidad_final = 0
                self.velocidad = velocidad_final
                return self.velocidad
            else:
                self.velocidad = velocidad_final
                return self.velocidad

        def PropiedadesDelVehiculo(self,tipo,color,velocidad):
            print(tipo)
            print(color)
            print(velocidad)
            return tipo , color, velocidad

    vehiculo_creado = Vehicle(tipo,color)
    return vehiculo_creado

#a = ClaseVehiculo('auto','gris')
#print(a)
#print(a.Acelerar(10))
#print(a.Acelerar(15))
#print(a.Acelerar(-10)) 
    
# O.K. tested ok checked



def OrdenarDiccionario(diccionario_par, clave, descendente=bool(True)):
    '''
    Esta función recibe como parámetro un diccionario, 
    cuyas listas de valores tienen el mismo tamaño y
    sus elementos enésimos están asociados.
    
    Y otros dos parámetros que indicanla clave por la cual debe ordenarse y si es descendente o ascendente.
    
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    
    Si el parámetro diccionario no es un tipo de dato diccionario ok
    ó el parámetro clave no se encuentra dentro de las claves del diccionario, debe devolver nulo. ok
    
    Ej:
    
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    
    
    # Si el parámetro diccionario no es un tipo de dato diccionario 
    # ó el parámetro clave no se encuentra dentro de las claves del diccionario, debe devolver nulo.  

    if (type(diccionario_par) != dict)  | (clave not in diccionario_par):
        print('El parámetro recibido como diccionario, no lo es en cuanto a tipo de dato.')
        print('O la clave ingresada no se encuentra dentro de las claves posivbles del diccionario.')
        return None

    # valido longitud en ambas deirecciones de la matriz diccionario:
    #cantidadd de claves como de elementos, a su vez, dentro de las claves.')

    """
    dicc = {    'clave1':   ['c','a','b'],
                'clave2':   ['casa','auto','barco'],
                'clave3':   [1,2,3]}

        OrdenarDiccionario(dicc, 'clave1')
    """


    for i in diccionario_par:
        if i == clave:
            for j in diccionario_par:
                if descendente == False:
                    diccionario_par[j].sort()
                if descendente == True:
                    diccionario_par[j].sort(reverse=True)
                    
                
    print(diccionario_par)
    return diccionario_par


# OrdenarDiccionario(dicc, 'clave3',True)
# OrdenarDiccionario(dicc, 'clave3',False)
# OrdenarDiccionario(dicc, 'clave1',True)
#OrdenarDiccionario(dicc, 'clave4',False)

#checked OK. tested OK.