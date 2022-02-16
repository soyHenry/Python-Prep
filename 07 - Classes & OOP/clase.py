class calculador:
    '''
    Esta clase toma las funciones de ejercicios anteriores para utilizarlas en metodos, toma una lista
    '''
    def __init__(self, lista):
        self.lista = lista
    
    def es_primo(self):
        for x in self.lista:
            if self.__es_primo(x):
                print(x, "Es primo")
            else:
                print(x, "No es primo")

    def __es_primo(self, x):
        self.x = x
        if x == 1 or x == 0:
            return False
        primo = True
        j = 2
        while j < x:
            if x % j == 0:
                return False
            j += 1
        return primo

    def moda(self, max_rep):
        if max_rep == 'maximo':
            max_rep = True
        elif(max_rep == 'minimo'):
            max_rep = False
        lista_cont = {}
        for x in self.lista:
            n = 0
            for y in self.lista:
                if y == x:
                    n+=1
                lista_cont[x] = n

        for x in self.lista:
            if lista_cont[x] == 1:
                del lista_cont[x]
    
        if max_rep:
            return ((max(lista_cont, key=lista_cont.get),max(lista_cont.values())))
        else:
            return ((min(lista_cont, key=lista_cont.get),min(lista_cont.values())))
    
    def tempconv(self,o,d):
        for x in self.lista:
            self.__tempconv(x,o,d)

    def __tempconv(self,valor,origen,destino):
        self.valor = valor
        self.origen = origen
        self.destino = destino
        if origen == destino:
            return None
        if origen == "Celcius":
            if destino == "Farenheit":
                temp = (valor * 9/5) + 32
            if destino == "Kelvin":
                temp = valor + 273.15
        if origen == "Farenheit":
            if destino == "Celcius":
                temp = (valor - 32) * 5/9
            if destino == "Kelvin":
                temp = (valor - 32) * 5/9 + 273.15
        if origen == "Kelvin":
            if destino == "Celcius":
                temp = valor - 273.15
            if destino == "Farenheit":
                temp = (valor - 273.15) * 9/5 + 32
        if not valor:
            print("Parametros incorrectos")
        return print(valor,"°",origen[0],"=",temp,"°",destino[0])

    def factorial(self):
        for n in self.lista:
            print(self.__factorial(n))

    def __factorial(self, n):
        self.n = n
        if n < 0 or type(n) is not int:
            return print("Valor incorrecto")
        if n == 1:
            return 1
        else:
            fact = n
            for x in range(0,n):
                fact = n * self.__factorial(n-1)
            return fact