#*******************************************************************
#*                                                                 *
#*                     SIMULACRO HENRY CHALLENGE                   *
#*                                                                 *
#*******************************************************************

def ListaDivisibles(numero, tope):
    '''
    Esta  función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    #Tu código aca:
    lista=[]
    for i in range((tope)):
        if (i+1)%numero==0:
            lista.append(i+1)

    return lista

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
    exp=numero**exponente
    return exp

def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    #Tu código aca:
    if type(lista) != list:
        return None
    else:
        lista_final=[]
        for elem in lista:
            if isinstance(elem, list):
                lista_final.extend(ListaDeListas(elem))
            else:
                lista_final.append(elem)
        return lista_final



    #return 'Funcion incompleta'

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
        Factorial(0) debe retornar 1
    '''
    #Tu código aca:
    if (type(numero) != int):
        return None
    if (numero < 0):
        return None
    factorial = 1
    for n in range(1, (numero)+1):
        factorial = factorial * n
    return factorial
    #return 'Funcion incompleta'

def ListaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como parámetro, siendo ambos inclusivos.
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
    En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía.
    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    #Tu código aca:
    lista=[]
    if (type(desde) != int or type(hasta) != int):
        return None
    if (desde < 0 or hasta < 0):
        return None
    if (desde > hasta):
        return lista    
    def esPrimo(num):
        if num==2:
            return True
        for n in range (2,num):
            if(num%n!=0):
                continue
            else:
                return False
        return True
    for i in range(desde,(hasta+1)):
        if esPrimo(i):
            lista.append(i)

    return lista    
    

def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,1),(4,1)]
    '''
    #Tu código aca:
    l=[]
    if type(lista) != list:
        return None
    while len(lista)>0:
        elemento=lista[0]
        cuenta=lista.count(lista[0])
        l.append((elemento,cuenta))
        for i in range(lista.count(lista[0])):
            lista.remove(elemento)
            continue
    return l

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
    class Vehiculo:
        def __init__(self, tipo, color):
            if (tipo=='auto' or tipo =='camioneta' or tipo=='moto'):
                self.Tipo = tipo
            else:
                raise TypeError ('el tipo de vehículo tiene que ser auto, camioneta o moto')
            self.Color = color
            self.Velocidad = 0

        def Acelerar(self, acel):
            self.Velocidad += acel
            if self.Velocidad < 0:
                self.Velocidad=0
            if self.Velocidad>100:
                self.Velocidad=100
            return self.Velocidad
    
    a = Vehiculo(tipo, color)    
    return a


def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento descendente y 
                        ascendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[3,1,2]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['c','b','a'],
                                                                'clave2':['casa','barco','auto'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    if type(diccionario_par) != dict:
        return None
    diccion_lista=[]
    diccion_lista=list(diccionario_par.keys())
    if clave not in diccion_lista:
        return None
    for key, value in diccionario_par.items():
        value.sort(reverse=descendente)
    
    return diccionario_par   

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if (type(numero) != int):
        return None
    if (numero < 1):
        return None
    factorial = 1
    while(numero > 1):
        factorial = factorial * numero
        numero -= 1
    return factorial

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    if (type(valor) != int):
        return None
    for i in range(2, (int(valor / 2) + 1)):
        if valor % i == 0:
            return False
    return True
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self, especie, color):
            self.Especie = especie
            self.Color = color
            self.Edad = 0

        def CumplirAnios(self):
            self.Edad += 1
            return self.Edad
    
    a = Animal(especie, color)    
    return a


# Caso 1
# El constructor de la clase Emprendedor recibe nombre (str), apellido (str),
# libros (lista), mascotas (lista).

# a) Inicializar la clase con sus atributos

class Emprendedor:
    """En esta clase se crean emprenderes"""
    mascotas = [] # Acumulará las mascotas del Emprendedor
    libros   = [] # Es una lista de libros del Emprendedor
    def __init__(self, nombre, apellido, libros, mascotas):
        self.nombre   = nombre
        self.apellido = apellido
        self.libros   = libros
        self.mascotas = mascotas

# b) Crear un Método que agregue una mascota (mascota) a la lista, no debe 
#    retornar nada. Mascotas es una lista
# 

    def addMascotas (self, newPet):
        self.mascotas.add()
        
        