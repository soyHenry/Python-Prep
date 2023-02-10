class modulo_7:
    def __init__(self, lista):
        if (type(lista) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros.')  
        else:
            self.lista = lista

    def esPrimo(self, x):
        primo = True
        if (type(x) != int):
            raise ValueError('Error, el numero ingresado debe ser un entero. ')

        for i in range(2,x):
            if (x % i == 0):
                primo = False
            
        return primo

    def devolverPrimos(self):
        primos = []
        primos_boleano = []

        for e,i in enumerate(self.lista):
            if (self.esPrimo(i) == True):
                primos.append(i)
                primos_boleano.append(True)
            else:
                primos_boleano.append(False)

        return primos, primos_boleano

    def devolverRepetido(self, tipo):
        """ 
        Funcion que devuelve el menor o mayor nro repetido en un array de numeros.
        Listado: es el array de nros. 
        Tipo: vale 1 o 2, 1 indica que devuelve el menor nro repetido
        y 2 devuelve el mayor numero repetido.- 
        """ 
        if  (tipo != 1 and tipo !=2):
            raise ValueError('Tipo solo puede vale 1 o 2.')
        repetido = 0
        veces   = 0

        for i in self.lista:
            if (self.lista.count(i) >= veces):
                if (self.lista.count(i) == veces):
                    if (tipo == 1 and i < repetido):
                        repetido = i
                        
                    elif(tipo == 2 and i > repetido):
                        repetido = i    
                else: 
                    repetido = i
                    veces = self.lista.count(i)
        return repetido
        
    def resolverGrados(self, valor, origen, destino):
        """ Función que convierta entre grados Celsius, Farenheit y Kelvin. 
            Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
            origen y destino pueden valer 'F', 'C' o 'K'
        """ 
     
        if (destino != 'F' and destino !='C' and destino != 'K'):
            raise ValueError('El parametro del destino es inválido. Como valor esperado se espera: "F", "C" o "K".') 
           
           
        if (origen != 'F' and origen !='C' and origen != 'K'):
            raise ValueError('El parametro del origen es inválido. Como valor esperado se espera: "F", "C" o "K"')
            
            
        if (origen == 'F'):
            if (destino == 'F'):
                return valor
            elif(destino == 'C'):
                return ((valor - 32) * (5 / 9))
            else: # entonces destino = 'K'
                return ((valor - 32) * (5 / 9)) + 273.15

        elif(origen == 'C'):
            if (destino == 'C'):
                return valor
            elif(destino == 'F'):
                return (valor * 9 / 5) + 32 
            else: # entonces destino = 'K'
                return valor + 273.15

        else: #entocnes origen = 'K'
            if (destino == 'K'):
                return valor
            elif(destino == 'F'):
                return ((valor - 273.15) * 9 / 5) + 32 
            else: # entonces destino = 'C'
                return (valor - 273.15)
        
        
    def factorial(self, n):

        if (n < 1 or type(n) != int):
            return("No se acepta un número no entero o negativo ")
            
        if (n == 1):
            return 1
        else:
            return n * self.factorial(n-1)


    def devolverFactorial(self):
        listadofact = []
        for elemento in self.lista:
            listadofact.append(self.factorial(elemento))

        return listadofact